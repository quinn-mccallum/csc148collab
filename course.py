"""CSC148 Assignment 1

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh and Jaisie Sin

=== Module Description ===

This file contains classes that describe a university course and the students
who are enrolled in these courses.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Optional, Dict
if TYPE_CHECKING:
    from survey import Answer, Survey, Question


def sort_students(lst: List[Student], attribute: str) -> List[Student]:
    """
    Return a shallow copy of <lst> sorted by <attribute>

    === Precondition ===
    <attribute> is a attribute name for the Student class

    >>> s1 = Student(1, 'Misha')
    >>> s2 = Student(2, 'Diane')
    >>> s3 = Student(3, 'Mario')
    >>> sort_students([s1, s3, s2], 'id') == [s1, s2, s3]
    True
    >>> sort_students([s1, s2, s3], 'name') == [s2, s3, s1]
    True
    """
    return sorted(lst, key=lambda s: getattr(s, attribute))


class Student:
    """
    A Student who can be enrolled in a university course.

    === Public Attributes ===
    id: the id of the student
    name: the name of the student
    _answers: a dictionary with question.id keys and Answer object values

    === Representation Invariants ===
    name is not the empty string
    all answers are valid for the questions in _answers
    """

    id: int
    name: str
    _answers: Dict[int, Answer]
    # TODO: ask about storing Question object v. question id.
    # TODO: 2 different question objects with same question id? what to do???

    def __init__(self, id_: int, name: str) -> None:
        """ Initialize a student with name <name> and id <id>
        Representation Invariant: name is not empty string"""
        self.id = id_
        self.name = name
        self._answers = {}

    def __str__(self) -> str:
        """ Return the name of this student """
        return self.name

    def has_answer(self, question: Question) -> bool:
        """
        Return True iff this student has an answer for a question with the same
        id as <question> and that answer is a valid answer for <question>.
        """
        if question.id in self._answers:
            if question.validate_answer(self._answers[question.id]):
                return True
        return False

    def set_answer(self, question: Question, answer: Answer) -> None:
        """
        Record this student's answer <answer> to the question <question>.
        Do nothing if answer is not valid for this question.
        """
        # Validate answer for question
        if question.validate_answer(answer):
            self._answers[question.id] = answer

    def get_answer(self, question: Question) -> Optional[Answer]:
        """
        Return this student's answer to the question <question>. Return None if
        this student does not have an answer to <question>
        """
        if question.id in self._answers:
            return self._answers[question.id]
        return None


class Course:
    """
    A University Course

    === Public Attributes ===
    name: the name of the course
    students: a list of students enrolled in the course

    === Representation Invariants ===
    - No two students in this course have the same id
    - name is not the empty string
    """

    name: str
    students: List[Student]

    def __init__(self, name: str) -> None:
        """
        Initialize a course with the name of <name>.
        precondition = name is not an empty string
        """
        self.name = name
        self.students = []

    def enroll_students(self, students: List[Student]) -> None:
        """
        Enroll all students in <students> in this course.

        If adding any student would violate a representation invariant,
        do not add any of the students in <students> to the course.
        """

        # check representation invariants
        duplicate_students = False

        # for every possible student,
        for possible_student in students:

            # for every existing student,
            for existing_student in self.students:

                # check if their id's are the same
                if possible_student.id == existing_student.id:
                    duplicate_students = True

        # add students
        if duplicate_students is False:
            self.students.extend(students)

    def all_answered(self, survey: Survey) -> bool:
        """
        Return True iff all the students enrolled in this course have a valid
        answer for every question in <survey>.
        """
        questions = survey.get_questions()
        for student in self.students:
            for question in questions:
                answer = student.get_answer(question)
                if answer is None:
                    return False
                if not answer.is_valid(question):
                    return False

        return True

    def get_students(self) -> Tuple[Student, ...]:
        """
        Return a tuple of all students enrolled in this course.

        The students in this tuple should be in order according to their id
        from lowest id to highest id.

        Hint: the sort_students function might be useful
        """
        ids = []
        tup = []

        for student in self.students:
            ids.append(student.id)

        ids.sort()

        for idd in ids:
            for student in self.students:
                if idd == student.id:
                    tup.append(student)

        return tuple(tup)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'survey']})
