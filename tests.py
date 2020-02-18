# TODO: put all your tests in this file (you can delete this line)
from course import *
from survey import *
from criterion import *
from grouper import *


# Step 2
class TestStudent:
    def test_student__str__(self) -> None:
        """Test student initializer and __str__ implementation"""
        tom = Student(0, "Thomas")
        assert tom.name == "Thomas"
        assert tom.id == 0
        assert tom.__str__() == "Thomas"

    def test_student_attributes(self) -> None:
        """Test the public attributes of Student"""
        student = Student(1, 'John')
        assert student.name == 'John'
        assert student.id == 1

    # Student.has_answer()
    def test_student_has_answer_return_true(self) -> None:
        """Test that the has_answer method returns True when the Student
        has an Answer to the Question"""
        student = Student(1, 'John')
        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer('a')
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer(["yes", "sometimes"])
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(3)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer(True)
        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)
        student.set_answer(q4, a4)
        assert len(student._answers) == 4
        assert student.has_answer(q1) is True
        assert student.has_answer(q2) is True
        assert student.has_answer(q3) is True
        assert student.has_answer(q4) is True

    def test_student_has_answer_return_false(self) -> None:
        """ """
        student = Student(1, 'John')
        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer("z")
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer('yes')
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(7)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer("True")
        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)
        student.set_answer(q4, a4)
        assert len(student._answers) == 0
        assert student.has_answer(q1) is False
        assert student.has_answer(q2) is False
        assert student.has_answer(q3) is False
        assert student.has_answer(q4) is False

    # Student.set_answer()
    def test_student_set_answer_base_case(self) -> None:
        """Test set_answer base case"""
        student = Student(1, 'John')
        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer('a')
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer(["yes", "sometimes"])
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(3)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer(True)
        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)
        student.set_answer(q4, a4)
        assert len(student._answers) == 4
        assert student._answers[1] == a1
        assert student._answers[5] == a2
        assert student._answers[2] == a3
        assert student._answers[4] == a4
        assert student._answers[1].content == 'a'
        assert student._answers[5].content == ["yes", "sometimes"]
        assert student._answers[2].content == 3
        assert student._answers[4].content == True

    def test_student_set_answer_not_valid(self) -> None:
        """Test that set_answer does not record invalid answers """
        student = Student(1, 'John')
        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer('z')
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer('yes')
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(7)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer("True")
        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)
        student.set_answer(q4, a4)
        assert len(student._answers) == 0
        assert student._answers == {}

    # Student.get_answer()
    def test_student_get_answer_valid(self) -> None:
        student = Student(1, 'John')
        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer('a')
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer(["yes", "sometimes"])
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(3)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer(True)
        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)
        student.set_answer(q4, a4)
        assert len(student._answers) == 4
        assert student.get_answer(q1) == a1
        assert student.get_answer(q2) == a2
        assert student.get_answer(q3) == a3
        assert student.get_answer(q4) == a4

    def test_student_get_answers_not_valid(self) -> None:
        student = Student(1, 'John')
        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer('z')
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer('yes')
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(7)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer("True")
        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)
        student.set_answer(q4, a4)
        assert len(student._answers) == 0
        assert student.get_answer(q1) is None
        assert student.get_answer(q2) is None
        assert student.get_answer(q3) is None
        assert student.get_answer(q4) is None

    def test_Student_has_nonexistant(self) -> None:
        """Test if student has a nonexistent entry"""
        student = Student(1, 'John')

        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")

        a1 = Answer(2)
        a2 = Answer("opt 1")
        a3 = Answer(["a", "b"])

        student.set_answer(q1, a1)
        student.set_answer(q2, a2)
        student.set_answer(q3, a3)

        assert not student.has_answer(q4)


# Step 3
class TestCourse:
    def test_course_attributes(self) -> None:
        """Test the public attributes of Course"""
        course = Course('csc148')
        assert course.name == 'csc148'
        assert course.students == []

    def test_enroll_students_no_dupes(self) -> None:
        """Test enroll_students method w/o duplicate students"""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        studs = [quinn, tomasz]
        csc148 = Course('csc148')
        csc148.enroll_students(studs)
        assert csc148.students == studs


    def test_enroll_students_with_dupes(self) -> None:
        """Test enroll_students method with duplicate students"""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        csc148 = Course('csc148')
        csc148.enroll_students([ellen])
        assert csc148.students == [ellen]
        studs = [quinn, tomasz, ellen]
        csc148.enroll_students(studs)
        assert csc148.students == [ellen]

    def test_course_get_students(self) -> None:
        quinn = Student(22, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(14, "Ellen")
        students = [quinn, tomasz, ellen]
        csc148 = Course('csc148')
        csc148.enroll_students(students)
        assert csc148.get_students() == (tomasz, ellen, quinn)


# Step 4:
class TestQuestion:
    def test_mcq_str(self) -> None:
        """Test __str__ of class"""
        my_question = MultipleChoiceQuestion(1, "Acceptable Colours",
                                             ["Red", "Green", "Blue"])
        assert my_question.__str__() == "Q[1]: Acceptable Colours " \
                                        "Opt 1: Red, Opt 2: Green, Opt 3: Blue"

    def test_num_str(self) -> None:
        """Test __str__ of class"""
        my_question = NumericQuestion(2, "Buckets needed",
                                      2, 10)
        assert my_question.__str__() == "Q[2]: Buckets needed Opt 1: 2, Opt 2: 10"

    def test_yn_str(self) -> None:
        """Test __str__ of class"""
        my_question = YesNoQuestion(3, "Do you allow robots to paint?")

        assert my_question.__str__() == "Q[3]: Do you allow robots to paint?  " \
                                        "Opt 1: True, Opt 2: False"

    def test_cbox_str(self) -> None:
        """Test __str__ of class"""
        my_question = CheckboxQuestion(1, "Trusted Workers",
                                       ["Bob the builder",
                                        "Timmy the destroyer",
                                        "Pan the painter"])
        assert my_question.__str__() == "Q[1]: Trusted Workers " \
                                        "Opt 1: Bob the builder, " \
                                        "Opt 2: Timmy the destroyer, " \
                                        "Opt 3: Pan the painter"

    def test_mcquestion_attributes(self) -> None:
        """Test the attributes of class MultipleChoiceQuestion"""
        q = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        assert q.id == 1
        assert q.text == "a b c or d?"
        assert q._options == ['a', 'b', 'c', 'd']

    def test_numericquestion_attributes(self) -> None:
        """Test the attributes of class NumbericQuestion"""
        nq = NumericQuestion(2, '5 + 5', 9, 11)
        assert nq.id == 2
        assert nq.text == "5 + 5"
        assert nq._options[0] == "9"
        assert nq._options[1] == '11'

    def test_yesnoquestion_attributes(self) -> None:
        """Test the public attributes of class YesNoQuestions"""
        ynq = YesNoQuestion(4, "are you human?")
        assert ynq.id == 4
        assert ynq. text == 'are you human?'

    def test_checkboxquestion_attributes(self) -> None:
        """Test the attributes of class Checkbox"""
        cbq = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        assert cbq.id == 5
        assert cbq.text == "do you like dogs?"
        assert cbq._options == ['yes', 'no', 'sometimes']

    def test_mcq_valid_invalid(self) -> None:
        """Test __str__ of class"""
        my_question = MultipleChoiceQuestion(1, "Acceptable Colours",
                                             ["Red", "Green", "Blue"])
        answer_1 = Answer("Dog")
        answer_2 = Answer("Red")
        answer_3 = Answer("Green")
        answer_4 = Answer("")
        assert not answer_1.is_valid(my_question)
        assert answer_2.is_valid(my_question)
        assert answer_3.is_valid(my_question)
        assert not answer_4.is_valid(my_question)

    def test_num_valid_invalid(self) -> None:
        """Test __str__ of class"""
        my_question = NumericQuestion(2, "Buckets needed",
                                      2, 10)
        answer_1 = Answer(0)
        answer_2 = Answer(2)
        answer_3 = Answer(5)
        answer_4 = Answer(10)
        answer_5 = Answer(11)
        assert not answer_1.is_valid(my_question)
        assert answer_2.is_valid(my_question)
        assert answer_3.is_valid(my_question)
        assert answer_4.is_valid(my_question)
        assert not answer_5.is_valid(my_question)

    def test_yn_valid_invalid(self) -> None:
        """Test __str__ of class"""
        my_question = YesNoQuestion(3, "Do you allow robots to paint?")

        answer_1 = Answer("True")
        answer_2 = Answer(True)
        answer_3 = Answer(False)
        answer_4 = Answer("False")
        answer_5 = Answer(0)
        answer_6 = Answer("")
        assert not answer_1.is_valid(my_question)
        assert answer_2.is_valid(my_question)
        assert answer_3.is_valid(my_question)
        assert not answer_4.is_valid(my_question)
        assert not answer_5.is_valid(my_question)
        assert not answer_6.is_valid(my_question)

    def test_cbox_valid_invalid(self) -> None:
        """Test __str__ of class"""
        my_question = CheckboxQuestion(1, "Acceptable Letters", ["A",
                                                                 "B",
                                                                 "C",
                                                                 "D"])

        answer_1 = Answer(["A", "B"])
        answer_2 = Answer(["0", "B"])
        answer_3 = Answer(False)
        answer_4 = Answer(["A", "A"])
        assert answer_1.is_valid(my_question)
        # assert not answer_2.is_valid(my_question)
        # assert not answer_3.is_valid(my_question)
        # assert not answer_4.is_valid(my_question)


# Step 5
class TestAnswer:
    def test_answer_attributes(self) -> None:
        """Test the public attributes of class Answer"""
        a = Answer("dogs")
        b = Answer(True)
        c = Answer(10)
        d = Answer(['a', 'b', 'c', 'd'])
        assert a.content == "dogs"
        assert b.content == True
        assert c.content == 10
        assert d.content == ['a', 'b', 'c', 'd']

    def test_mcq_similarity(self) -> None:
        """Test answer similarity for MultipleChoiceQuestions"""
        my_question = MultipleChoiceQuestion(1, "Acceptable Colours",
                                             ["R", "G", "B"])
        answer_1 = Answer("R")
        answer_2 = Answer("G")
        answer_3 = Answer("R")
        assert my_question.get_similarity(answer_1, answer_2) == 0.0
        assert my_question.get_similarity(answer_1, answer_3) == 1.0

    def test_num_similarity(self) -> None:
        """Test answer similarity for NumericQuestions"""
        my_question = NumericQuestion(2, "Buckets needed",
                                      1, 3)
        answer_1 = Answer(1)
        answer_2 = Answer(2)
        answer_3 = Answer(3)
        answer_4 = Answer(1)
        assert my_question.get_similarity(answer_1, answer_3) == 0.0
        assert my_question.get_similarity(answer_1, answer_4) == 1.0
        assert my_question.get_similarity(answer_1, answer_2) == 0.5
        assert my_question.get_similarity(answer_2, answer_3) == 0.5

    def test_yn_similarity(self) -> None:
        """Test answer similarity for YesNoQuestions"""
        my_question = YesNoQuestion(3, "Do you allow robots to paint?")

        answer_1 = Answer(True)
        answer_2 = Answer(False)
        answer_3 = Answer(True)
        assert my_question.get_similarity(answer_1, answer_2) == 0.0
        assert my_question.get_similarity(answer_1, answer_3) == 1.0

    def test_cbox_similarity(self) -> None:
        """Test answer similarities for CheckboxQuestions"""
        my_question = CheckboxQuestion(1, "Acceptable Letters", ["A",
                                                                 "B",
                                                                 "C",
                                                                 "D"])

        answer_1 = Answer(["A", "B", "C", "D"])
        answer_2 = Answer(["A"])
        answer_3 = Answer(["A", "B"])
        answer_4 = Answer(["A", "B", "C"])
        answer_5 = Answer(["A"])
        answer_6 = Answer(["B", "A"])
        assert my_question.get_similarity(answer_1, answer_2) == 0.25
        assert my_question.get_similarity(answer_1, answer_3) == 0.5
        assert my_question.get_similarity(answer_1, answer_4) == 0.75
        assert my_question.get_similarity(answer_2, answer_5) == 1.0
        assert my_question.get_similarity(answer_3, answer_6) == 1.0
        assert my_question.get_similarity(answer_2, answer_3) == 0.5


# Step 6
class TestCriterion:
    def test_homo_crit(self) -> None:
        """Test """
        my_question = NumericQuestion(1, "Pick a Number", 1, 5)

        answer_1 = Answer(1)
        answer_2 = Answer(2)
        answer_3 = Answer(3)
        answer_4 = Answer(4)
        answer_5 = Answer(5)

        common_answers = [answer_1, answer_1, answer_1, answer_1, answer_1]
        range_answers = [answer_1, answer_2, answer_3, answer_4, answer_5]
        opposite_answers = [answer_1, answer_5]

        homo_criterion = HomogeneousCriterion()

        assert homo_criterion.score_answers(my_question,
                                            common_answers) == 1
        result = homo_criterion.score_answers(my_question,
                                              range_answers)
        assert 0 < result < 1
        assert homo_criterion.score_answers(my_question,
                                            opposite_answers) == 0

    def test_hetero_crit(self) -> None:
        """Test """
        my_question = NumericQuestion(1, "Pick a Number", 1, 5)

        answer_1 = Answer(1)
        answer_2 = Answer(2)
        answer_3 = Answer(3)
        answer_4 = Answer(4)
        answer_5 = Answer(5)

        common_answers = [answer_1, answer_1, answer_1, answer_1, answer_1]
        range_answers = [answer_1, answer_2, answer_3, answer_4, answer_5]
        opposite_answers = [answer_1, answer_5]

        hetero_criterion = HeterogeneousCriterion()

        assert hetero_criterion.score_answers(my_question,
                                              common_answers) == 0
        result = hetero_criterion.score_answers(my_question,
                                                range_answers)
        assert 0 < result < 1
        assert hetero_criterion.score_answers(my_question,
                                              opposite_answers) == 1

    def test_lonely_crit(self) -> None:
        """Test """
        my_question = NumericQuestion(1, "Pick a Number", 1, 5)

        answer_1 = Answer(1)
        answer_2 = Answer(2)
        answer_3 = Answer(3)
        answer_4 = Answer(4)
        answer_5 = Answer(5)

        no_unique_answers = [answer_1, answer_1, answer_1, answer_1, answer_1]
        some_unique_answers = [answer_1, answer_2, answer_2, answer_2, answer_5]
        all_unique_answers = [answer_1, answer_2, answer_3, answer_4, answer_5]

        lonely_criterion = LonelyMemberCriterion()

        assert lonely_criterion.score_answers(my_question,
                                              no_unique_answers) == 1
        assert lonely_criterion.score_answers(my_question,
                                              some_unique_answers) == 0
        assert lonely_criterion.score_answers(my_question,
                                              all_unique_answers) == 0


# Step 7
class TestGroup:
    def test_group_contains_true(self) -> None:
        """Test the __contains__ method for class Group when member is
        contained within Group's _members list"""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        l = [quinn, tomasz, ellen]
        g = Group(l)
        assert g.__contains__(ellen) is True


    def test_group_contains_false(self) -> None:
        """Test the __contains__ method for class Group when member is
        NOT contained within Group's _members list"""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        l = [quinn, tomasz]
        g = Group(l)
        assert g.__contains__(ellen) is False


    def test_get_members_is_shallow(self) -> None:
        """Test get_members method in class Group returns a shallow
        copy of the list in self._members"""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        l = [quinn, tomasz, ellen]
        g = Group(l)
        assert id(g.get_members()) != id(g._members)


# Step 8
class TestGrouping:
    def test_grouping_attribute(self) -> None:
        """Test the attribute initialized in class Grouping"""
        g = Grouping()
        assert g._groups == []


    def test_add_group_base_case(self) -> None:
        """Test adding Groups of Students to class Grouping."""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        l1 = [quinn, tomasz, ellen]
        g1 = Group(l1)
        s = Student(6, 'Sally')
        d = Student(7, 'Donald')
        l2 = [s, d]
        g2 = Group(l2)
        v = Grouping()
        v.add_group(g1)
        v.add_group(g2)
        assert len(v._groups) == len([l1, l2])
        assert v._groups == [g1, g2]


    def test_add_group_zero_members(self) -> None:
        """Test adding Student Groups where one group is valid, but the second
        group is empty. """
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        l1 = [quinn, tomasz, ellen]
        g1 = Group(l1)
        g2 = Group([])
        v = Grouping()
        v.add_group(g1)
        v.add_group(g2)
        assert v._groups == [g1]


    # this test and ^^test might be redundant so maybe delete one?
    def test_add_group_zero_members2(self) -> None:
        """Test adding an empty Group to Grouping."""
        g = Group([])
        v = Grouping()
        v.add_group(g)
        assert v._groups == []


    def test_add_group_duplicates(self) -> None:
        """Test Group with duplicate students will not be added to Grouper's
        self._groups"""
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        sally = Student(6, 'Sally')
        donald = Student(7, 'Donald')
        l1 = [quinn, tomasz, ellen]
        l2 = [sally, donald, ellen]
        g1 = Group(l1)
        g2 = Group(l2)
        v = Grouping()
        v.add_group(g1)
        v.add_group(g2)
        assert v._groups == [g1]


    def test_get_groups_is_shallow(self) -> None:
        """Test that Grouping's get_groups method returns a shallow copy of
        self._groups. """
        quinn = Student(1, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(3, "Ellen")
        sally = Student(6, 'Sally')
        donald = Student(7, 'Donald')
        l1 = [quinn, tomasz, ellen]
        l2 = [sally, donald]
        g1 = Group(l1)
        g2 = Group(l2)
        v = Grouping()
        v.add_group(g1)
        v.add_group(g2)
        assert id(v._groups) != id(v.get_groups())


# Step 9
class TestSurvey:
    def test_survey_init(self) -> None:
        """Test initialization and basic properties of Survey"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")
        q_list = [q1, q2, q3, q4]

        my_survey = Survey(q_list)

        assert isinstance(my_survey._questions, Dict)
        assert isinstance(my_survey._criteria, Dict)
        assert isinstance(my_survey._weights, Dict)
        assert isinstance(my_survey._default_criterion, HomogeneousCriterion)
        assert my_survey._default_weight == 1

        assert q1.id in my_survey._questions
        assert q2.id in my_survey._questions
        assert q3.id in my_survey._questions
        assert q4.id in my_survey._questions


    def test_survey_len(self) -> None:
        """Test Survey method __len__"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")
        q_list = [q1, q2, q3, q4]

        my_survey = Survey(q_list)

        assert len(my_survey) == 4


    def test_survey_str(self) -> None:
        """Test Survey method __Str__"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")
        q_list = [q1, q2, q3, q4]

        my_survey = Survey(q_list)
        assert isinstance(str(my_survey), str)
        assert str(my_survey)[0] == "Q"


    def test_survey_contains(self) -> None:
        """Test Survey method contains"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")
        q_list = [q1, q2, q3]

        my_survey = Survey(q_list)
        assert my_survey.__contains__(q1)
        assert not my_survey.__contains__(q4)


    def test_survey_get_questions(self) -> None:
        """Test Survey method get_questions"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")
        q_list = [q1, q2, q3, q4]

        my_survey = Survey(q_list)
        survey_questions = my_survey.get_questions()
        assert q_list == survey_questions


    def test_survey_set_get_criterion(self) -> None:
        """Test Survey set and get criterion"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")
        q5 = YesNoQuestion(5, "T or F")

        c_1 = HomogeneousCriterion()
        c_2 = HeterogeneousCriterion
        c_3 = LonelyMemberCriterion

        q_list = [q1, q2, q3, q5]
        my_survey = Survey(q_list)

        # Test setting valid criterion
        assert my_survey.set_criterion(c_1, q1)
        assert my_survey.set_criterion(c_2, q2)
        assert my_survey.set_criterion(c_3, q3)

        # Test setting criterion to non existent question
        assert not my_survey.set_criterion(c_1, q4)
        assert not my_survey.set_criterion(c_2, q4)
        assert not my_survey.set_criterion(c_3, q4)

        # Test get criterion valid
        assert my_survey._get_criterion(q1) == c_1
        assert my_survey._get_criterion(q2) == c_2
        assert my_survey._get_criterion(q3) == c_3

        # Test get criterion on unset question
        assert my_survey._get_criterion(q5) == my_survey._default_criterion


    def test_survey_set_get_weight(self) -> None:
        """Test Survey set and get weight"""
        q1 = NumericQuestion(1, "Pick num", 1, 5)
        q2 = MultipleChoiceQuestion(2, "Pick text", ["opt 1", "opt 2"])
        q3 = CheckboxQuestion(3, "Pick multiple", ["a", "b", "c"])
        q4 = YesNoQuestion(4, "T or F")

        w_1 = 2
        w_2 = 3

        q_list = [q1, q2, q3]
        my_survey = Survey(q_list)

        # Test setting valid weight
        assert my_survey.set_weight(w_1, q1)
        assert my_survey.set_weight(w_2, q2)

        # Test setting weight to non existent question
        assert not my_survey.set_weight(w_1, q4)
        assert not my_survey.set_weight(w_2, q4)

        # Test get weight valid
        assert my_survey._get_weight(q1) == w_1
        assert my_survey._get_weight(q2) == w_2

        # Test get weight on unset question
        assert my_survey._get_weight(q3) == my_survey._default_weight


# Step 10
class TestHelperFunctions:
    def test_slice_list(self) -> None:
        """Test the slice_list function"""
        assert slice_list([3, 4, 6, 2, 3], 2) == [[3, 4], [6, 2], [3]]
        assert slice_list(['a', 1, 6.0, False], 3) == [['a', 1, 6.0], [False]]
        assert slice_list([], 1) == []

    def test_windows(self) -> None:
        """Test the windows function"""
        assert windows([3, 4, 6, 2, 3], 2) == [[3, 4], [4, 6], [6, 2], [2, 3]]
        assert windows(['a', 1, 6.0, False], 3) == [['a', 1, 6.0], [1, 6.0, False]]
        assert windows([], 1) == []


# Step 11
class TestGrouper:
    def test_class_grouper_init(self) -> None:
        """Test """
        g = Grouper(3)
        assert g.group_size == 3
        g.group_size = 4
        assert g.group_size == 4

    def test_alpha_grouper(self) -> None:
        """Test """
        g = AlphaGrouper(3)
        assert g.group_size == 3
        g.group_size = 4
        assert g.group_size == 4

    def test_alpha_make_grouping(self) -> None:
        """Test """
        quinn = Student(22, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(14, "Ellen")
        julia = Student(3, 'Julia')
        doria = Student(7, "Doria")
        vanessa = Student(14, 'Vanessa')
        students = [quinn, tomasz, ellen, julia, doria, vanessa]
        csc148 = Course('csc148')
        csc148.enroll_students(students)

        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        q4 = YesNoQuestion(4, "T or F")
        q_list = [q1, q2, q3, q4]

        s = Survey(q_list)

        alpha = AlphaGrouper(2)
        alpha.make_grouping(csc148, s)
        assert ...


def test_greedy_make_grouping(self) -> None:
        """Test """
        quinn = Student(22, 'Quinn')
        tomasz = Student(2, 'Tomasz')
        ellen = Student(14, "Ellen")
        julia = Student(3, 'Julia')
        doria = Student(7, "Doria")
        vanessa = Student(14, 'Vanessa')
        students = [quinn, tomasz, ellen, julia, doria, vanessa]
        csc148 = Course('csc148')
        csc148.enroll_students(students)

        q1 = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
        a1 = Answer('z')
        q2 = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
        a2 = Answer('yes')
        q3 = NumericQuestion(2, "Pick num", 1, 5)
        a3 = Answer(7)
        q4 = YesNoQuestion(4, "T or F")
        a4 = Answer("True")




# def test_score_students() -> None:
# #     q1 = YesNoQuestion(1, " ")
# #     q2 = YesNoQuestion(2, " ")
# #
# #     a_true = Answer(True)
# #     a_false = Answer(False)
# #
# #     person_1 = Student(1, "Albo")
# #     person_2 = Student(2, "Bora")
# #     person_3 = Student(3, "Cola")
# #
# #     person_1.set_answer(q1, a_true)
# #     person_1.set_answer(q2, a_true)
# #     person_2.set_answer(q1, a_true)
# #     person_2.set_answer(q2, a_false)
# #     person_3.set_answer(q1, a_true)
# #     person_3.set_answer(q2, a_false)
# #
# #     q_list = [q1, q2]
# #     my_survey = Survey(q_list)
# #
# #     my_survey.set_weight(2, q1)
# #     my_survey.set_weight(3, q2)
# #
# #     criterion = HomogeneousCriterion()
# #     q2_answers = [a_true, a_false, a_false]
# #     similarity = criterion.score_answers(q2, q2_answers)
# TODO: FINISH THIS TEST CASE FOR SCORE STUDENTS


# def test_score_students_simple() -> None:
#     q1 = NumericQuestion(1, "Pick num", 1, 5)
#     q2 = YesNoQuestion(2, "T or F")
#
#     a_1 = Answer(1)
#     a_2 = Answer(5)
#     a_3 = Answer(True)
#     a_4 = Answer(False)
#
#     s_1 = Student(1, "Alphie")
#     s_2 = Student(2, "Alfons")
#     s_3 = Student(3, "Zori")
#     s_4 = Student(4, "Zoran")
#
#     s_1.set_answer(q1, a_1)
#     s_1.set_answer(q2, a_3)
#
#     s_2.set_answer(q1, a_1)
#     s_2.set_answer(q2, a_3)
#
#     s_3.set_answer(q1, a_2)
#     s_3.set_answer(q2, a_4)
#
#     s_4.set_answer(q1, a_2)
#     s_4.set_answer(q2, a_4)
#
#     s_list = [s_1, s_2, s_3, s_4]
#     q_list = [q1, q2]
#     my_survey = Survey(q_list)
#
#     my_survey.score_students(s_list)


if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])
