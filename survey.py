"""CSC148 Assignment 1

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Misha Schwartz, Mario Badr, Christine Murad, Diane Horton, Sophia Huynh
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh and Jaisie Sin

=== Module Description ===

This file contains classes that describe a survey as well as classes that
described different types of questions that can be asked in a given survey.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, List
from criterion import HomogeneousCriterion, InvalidAnswerError
if TYPE_CHECKING:
    from criterion import Criterion
    from grouper import Grouping
    from course import Student


class Question:
    """ An abstract class representing a question used in a survey

    === Public Attributes ===
    id: the id of this question
    text: the text of this question

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str
    # TODO: Make sure this is a proper abstract type for all parts

    def __init__(self, id_: int, text: str) -> None:
        """ Initialize a question with the text <text>
        Precondition: text is not the empty string
        """
        self.id = id_
        self.text = text

    def __str__(self) -> str:
        """
        Return a string representation of this question that contains both
        the text of this question and a description of all possible answers
        to this question.

        You can choose the precise format of this string.
        """
        raise NotImplementedError

    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff <answer> is a valid answer to this question.
        """
        raise NotImplementedError

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """ Return a float between 0.0 and 1.0 indicating how similar two
        answers are.

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """
        raise NotImplementedError


class MultipleChoiceQuestion(Question):
    # TODO: make this a child class of another class defined in this file
    """ A question whose answers can be one of several options

    === Public Attributes ===
    id: the id of this question
    text: the text of this question
    _options: a list of the possible (text) options for this question

    === Representation Invariants ===
    text is not the empty string
    No two elements in options are the same string
    Options contains at least two elements
    """

    id: int
    text: str
    _options: List[str]

    def __init__(self, id_: int, text: str, options: List[str]) -> None:
        """
        Initialize a question with the text <text> and id <id> and
        possible answers <options>.

        === Precondition ===
        No two elements in <options> are the same string
        <options> contains at least two elements
        Text is not the empty string
        """
        Question.__init__(self, id_, text)
        self._options = []

        self._options.extend(options)

    def __str__(self) -> str:
        """
        Return a string representation of this question including the
        text of the question and a description of the possible answers.

        You can choose the precise format of this string.
        """
        return_str = "Q[{}]: {} ".format(self.id, self.text)

        i = 1
        for option in self._options:
            if i != 1:
                return_str += ", "
            return_str += "Opt " + str(i) + ": " + option
            i += 1

        return return_str

    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff <answer> is a valid answer to this question.

        An answer is valid if its content is one of the possible answers to this
        question.
        """
        to_check = answer.content

        return to_check in self._options

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return 1.0 iff <answer1>.content and <answer2>.content are equal and
        0.0 otherwise.

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question.
        """
        if answer1.content == answer2.content:
            return 1.0
        else:
            return 0.0


class NumericQuestion(MultipleChoiceQuestion):
    # TODO: make this a child class of another class defined in this file
    """ A question whose answer can be an integer between some
    minimum and maximum value (inclusive).

    === Public Attributes ===
    id: the id of this question
    text: the text of this question
    _options: upper and lower bounds of possible answer, saved as str

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str
    _options: List[str]

    def __init__(self, id_: int, text: str, min_: int, max_: int) -> None:
        """
        Initialize a question with id <id_> and text <text> whose possible
        answers can be any integer between <min_> and <max_> (inclusive)

        === Precondition ===
        min_ < max_
        """
        MultipleChoiceQuestion.__init__(self, id_, text, [str(min_), str(max_)])

    # __str__ to be inherited

    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff the content of <answer> is an integer between the
        minimum and maximum (inclusive) possible answers to this question.
        """
        to_check = answer.content

        if not isinstance(to_check, int):
            return False

        return int(self._options[0]) <= to_check <= int(self._options[1])

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return the similarity between <answer1> and <answer2> over the range
        of possible answers to this question.

        Similarity calculated by:

        1. first find the absolute difference between <answer1>.content and
           <answer2>.content.
        2. divide the value from step 1 by the difference between the maximum
           and minimum possible answers.
        3. subtract the value from step 2 from 1.0

        Hint: this is the same calculation from the worksheet in lecture!

        For example:
        - Maximum similarity is 1.0 and occurs when <answer1> == <answer2>
        - Minimum similarity is 0.0 and occurs when <answer1> is the minimum
            possible answer and <answer2> is the maximum possible answer
            (or vice versa).

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """
        step_1 = abs(answer1.content - answer2.content)
        step_2 = step_1 / (int(self._options[1])-int(self._options[0]))
        similarity = 1.0 - step_2

        return similarity


class YesNoQuestion(MultipleChoiceQuestion):
    # TODO: make this a child class of another class defined in this file
    """ A question whose answer is either yes (represented by True) or
    no (represented by False).

    === Public Attributes ===
    id: the id of this question
    text: the text of this question
    _options: str version of True, False

    === Representation Invariants ===
    text is not the empty string
    """
    id: int
    text: str

    def __init__(self, id_: int, text: str) -> None:  # TODO fix this warning
        """
        Initialize a question with the text <text> and id <id>.
        """
        MultipleChoiceQuestion.__init__(self, id_, text, ['True', 'False'])

    def __str__(self) -> str:
        """
        Return a string representation of this question including the
        text of the question and a description of the possible answers.

        You can choose the precise format of this string.
        """
        # possible answers
        p_a = "Opt 1: True, Opt 2: False"

        return "Q[{}]: {}  {}".format(self.id, self.text, p_a)

    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff <answer>'s content is a boolean.
        """
        to_check = answer.content

        return isinstance(to_check, bool)

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return 1.0 iff <answer1>.content is equal to <answer2>.content and
        return 0.0 otherwise.

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """
        if answer1.content == answer2.content:
            return 1.0
        else:
            return 0.0


class CheckboxQuestion(MultipleChoiceQuestion):
    # TODO: make this a child class of another class defined in this file
    """ A question whose answers can be one or more of several options

    === Public Attributes ===
    id: the id of this question
    text: the text of this question
    _options: Possible options, as text

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str
    _options: List[str]

    # __init__ to be inherited

    # __str__ to be inherited

    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff <answer> is a valid answer to this question.

        An answer is valid iff its content is a non-empty list containing
        unique possible answers to this question.
        """
        to_check = answer.content

        # Check if the answer content is a list
        if not isinstance(to_check, List):
            return False

        # Check if the list is not empty
        if len(to_check) == 0:
            return False

        # Check if the content is unique
        if len(to_check) != len(set(to_check)):
            return False

        # Check if all answers possible
        for possible_answer in to_check:
            if possible_answer not in self._options:
                return False

        return True

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return the similarity between <answer1> and <answer2>.

        Similarity is defined as the ratio between the number of strings that
        are common to both <answer1>.content and <answer2>.content over the
        total number of unique strings that appear in both <answer1>.content and
        <answer2>.content

        For example, if <answer1>.content == ['a', 'b', 'c'] and
        <answer2>.content == ['c', 'b', 'd'], the strings that are common to
        both are ['c', 'b'] and the unique strings that appear in both are
        ['a', 'b', 'c', 'd'].

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """

        common_answers = []

        for a1 in answer1.content:
            for a2 in answer2.content:
                if a1 == a2 and a1 not in common_answers:
                    common_answers.append(a1)

        size_unique = len(set(answer1.content + answer2.content))

        similarity = len(common_answers) / size_unique

        return similarity


class Answer:
    """ An answer to a question used in a survey

    === Public Attributes ===
    content: an answer to a single question
    """
    content: Union[str, bool, int, List[str]]

    def __init__(self,
                 content: Union[str, bool, int, List[Union[str]]]) -> None:
        """Initialize an answer with content <content>
        new_answer = Answer("Apple")
        new_answer = Answer(True)
        """
        # TODO: this seemed too easy
        self.content = content

    def is_valid(self, question: Question) -> bool:
        """Return True iff self.content is a valid answer to <question>"""
        return question.validate_answer(self)


class Survey:
    """
    A survey containing questions as well as criteria and weights used to
    evaluate the quality of a group based on their answers to the survey
    questions.

    === Private Attributes ===
    _questions: a dictionary mapping each question's id to the question itself
    _criteria: a dictionary mapping a question's id to its associated criterion
    _weights: a dictionary mapping a question's id to a weight; an integer
              representing the importance of this criteria.
    _default_criterion: a criterion to use to evaluate a question if the
              question does not have an associated criterion in _criteria
    _default_weight: a weight to use to evaluate a question if the
              question does not have an associated weight in _weights

    === Representation Invariants ===
    No two questions on this survey have the same id
    Each key in _questions equals the id attribute of its value
    Each key in _criteria occurs as a key in _questions
    Each key in _weights occurs as a key in _questions
    Each value in _weights is greater than 0
    _default_weight > 0
    """

    _questions: Dict[int, Question]
    _criteria: Dict[int, Criterion]
    _weights: Dict[int, int]
    _default_criterion: Criterion
    _default_weight: int

    def __init__(self, questions: List[Question]) -> None:
        """
        Initialize a new survey that contains every question in <questions>.
        This new survey should use a HomogeneousCriterion as a default criterion
        and should use 1 as a default weight.
        """
        self._questions = {}
        self._criteria = {}
        self._weights = {}
        self._default_criterion = HomogeneousCriterion()
        self._default_weight = 1

        for q in questions:
            if q.id not in self._questions:
                self._questions[q.id] = q

    def __len__(self) -> int:
        """ Return the number of questions in this survey """
        return len(self._questions)

    def __contains__(self, question: Question) -> bool:
        """
        Return True iff there is a question in this survey with the same
        id as <question>.
        """
        return question.id in self._questions

    def __str__(self) -> str:
        """
        Return a string containing the string representation of all
        questions in this survey

        You can choose the precise format of this string.
        """
        return_str = ""
        first_question = True

        for question in self._questions:
            if not first_question:
                return_str += ', '

            return_str += str(self._questions[question])
            first_question = False

        return return_str

    def get_questions(self) -> List[Question]:
        """ Return a list of all questions in this survey """
        qlist = []
        for q in self._questions:
            qlist.append(self._questions[q])

        return qlist

    def _get_criterion(self, question: Question) -> Criterion:
        """
        Return the criterion associated with <question> in this survey.

        Iff <question>.id does not appear in self._criteria, return the default
        criterion for this survey instead.

        === Precondition ===
        <question>.id occurs in this survey
        """
        # check if question not in criteria
        if question.id not in self._criteria:
            return self._default_criterion

        # otherwise return
        else:
            return self._criteria[question.id]

    def _get_weight(self, question: Question) -> int:
        """
        Return the weight associated with <question> in this survey.

        Iff <question>.id does not appear in self._weights, return the default
        weight for this survey instead.

        === Precondition ===
        <question>.id occurs in this survey
        """
        # Check if question has a custom weight
        if question.id in self._weights:
            return self._weights[question.id]
        # Return the default weight
        else:
            return self._default_weight

    def set_weight(self, weight: int, question: Question) -> bool:
        """
        Set the weight associated with <question> to <weight> and return True.

        If <question>.id does not occur in this survey, do not set the <weight>
        and return False instead.
        """
        # Check if question exists
        if question.id not in self._questions:
            return False

        # Set the weight
        self._weights[question.id] = weight
        return True

    def set_criterion(self, criterion: Criterion, question: Question) -> bool:
        """
        Set the criterion associated with <question> to <criterion> and return
        True.

        If <question>.id does not occur in this survey, do not set the <weight>
        and return False instead.
        """
        if question.id not in self._questions:  # AttributeError: 'int' object
            return False                        # has no attribute 'id'
        else:
            self._criteria[question.id] = criterion
            return True

    def score_students(self, students: List[Student]) -> float:
        """
        Return a quality score for <students> calculated based on their answers
        to the questions in this survey, and the associated criterion and weight
        for each question .

        This score is determined using the following algorithm:

        1. For each question in <self>, find its associated criterion, weight,
           and <students> answers to this question. Use the score_answers method
           for this criterion to calculate a quality score. Multiply this
           quality score by the associated weight.
        2. Find the average of all quality scores from step 1.

        If an InvalidAnswerError would be raised by calling this method, or if
        there are no questions in <self>, this method should return zero.

        === Precondition ===
        All students in <students> have an answer to all questions in this
            survey
        """
        if len(self._questions) == 0:
            return 0.0

        try:
            sum_scores = 0
            # num_students = len(students)
            num_questions = len(self._questions)

            # Get each question id in self._questions
            for qid in self._questions:

                # Set the criterion & weight associated with each question
                crit = self._get_criterion(self._questions[qid])
                weight = self._get_weight(self._questions[qid])

                # Empty list to store all the answers for the questions
                # List resets to empty for each new question
                answers = []

                for student in students:
                    # Append each answer to question by each student to answers
                    # list
                    answers.append(student.get_answer(self._questions[qid]))

                # Call the score_answers method of criterion w/ Question object
                # and the list of answers. Multiply the score by the weight.
                # Append the score to scores.
                this_score = crit.score_answers(self._questions[qid], answers)
                sum_scores += this_score * weight

                # Get the average of the scores
            return sum_scores / num_questions

        except InvalidAnswerError:
            return 0.0

    def score_grouping(self, grouping: Grouping) -> float:
        """ Return a score for <grouping> calculated based on the answers of
        each student in each group in <grouping> to the questions in <self>.

        If there are no groups in <grouping> this score is 0.0. Otherwise, this
        score is determined using the following algorithm:

        1. For each group in <grouping>, get the score for the members of this
           group calculated based on their answers to the questions in this
           survey.
        2. Return the average of all the scores calculated in step 1.

        === Precondition ===
        All students in the groups in <grouping> have an answer to all questions
            in this survey
        """
        # Get groups from grouping
        groups_to_score = grouping.get_groups()
        num_groups = len(groups_to_score)
        total_score = 0

        # If grouping comes back empty
        if len(groups_to_score) == 0:
            return 0.0

        # for each group
        for group_to_score in groups_to_score:
            students_to_score = group_to_score.get_members()
            total_score += self.score_students(students_to_score)

        average_score = total_score / num_groups
        return average_score


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing',
                                                  'criterion',
                                                  'course',
                                                  'grouper']})
