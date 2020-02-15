# TODO: put all your tests in this file (you can delete this line)
from course import *
from survey import *
from criterion import *
from grouper import *

# Step 2
def test_student__str__() -> None:
    """Test student initializer and __str__ implementation"""
    Tom = Student(0,"Thomas")
    assert Tom.name == "Thomas"
    assert Tom.id == 0
    assert Tom.__str__() == "Thomas"


def test_student_attributes() -> None:
    """Test the public attributes of Student"""
    student = Student(1, 'John')
    assert student.name == 'John'
    assert student.id == 1


def test_student_str_method() -> None:
    """Test the str method of Student"""
    student = Student(2, 'Jill')
    assert student.__str__() == 'Jill'

#Step 3

def test_course_attributes() -> None:
    """Test the public attributes of Course"""
    course = Course('csc148')
    assert course.name == 'csc148'
    assert course.students == []


def test_enroll_students_no_dupes() -> None:
    """Test enroll_students method w/o duplicate students"""
    quinn = Student(1, 'Quinn')
    tomasz = Student(2, 'Tomasz')
    studs = [quinn, tomasz]
    csc148 = Course('csc148')
    csc148.enroll_students(studs)
    assert csc148.students == studs


def test_enroll_students_with_dupes() -> None:
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

# Step 4:

def test_mcq_str() -> None:
    """Test __str__ of class"""
    my_question = MultipleChoiceQuestion(1, "Acceptable Colours",
                                         ["Red", "Green", "Blue"])
    assert my_question.__str__() == "Q[1]: Acceptable Colours " \
                                    "Opt 1: Red, Opt 2: Green, Opt 3: Blue"

def test_num_str() -> None:
    """Test __str__ of class"""
    my_question = NumericQuestion(2, "Buckets needed",
                                         2, 10)
    assert my_question.__str__() == "Q[2]: Buckets needed Opt 1: 2, Opt 2: 10"

def test_yn_str() -> None:
    """Test __str__ of class"""
    my_question = YesNoQuestion(3, "Do you allow robots to paint?")

    assert my_question.__str__() == "Q[3]: Do you allow robots to paint?  " \
                                    "Opt 1: True, Opt 2: False"

def test_cbox_str() -> None:
    """Test __str__ of class"""
    my_question = CheckboxQuestion(1, "Trusted Workers",
                                         ["Bob the builder",
                                          "Timmy the destroyer",
                                          "Pan the painter"])
    assert my_question.__str__() == "Q[1]: Trusted Workers " \
                                    "Opt 1: Bob the builder, " \
                                    "Opt 2: Timmy the destroyer, " \
                                    "Opt 3: Pan the painter"

## SURVEY
def test_mcquestion_attributes() -> None:
    """Test the attributes of class MultipleChoiceQuestion"""
    q = MultipleChoiceQuestion(1, "a b c or d?", ['a', 'b', 'c', 'd'])
    assert q.id == 1
    assert q.text == "a b c or d?"
    assert q._options == ['a', 'b', 'c', 'd']


def test_numericquestion_attributes() -> None:
    """Test the attributes of class NumbericQuestion"""
    nq = NumericQuestion(2, '5 + 5', 9, 11)
    assert nq.id == 2
    assert nq.text == "5 + 5"
    assert nq._options[0] == "9"
    assert nq._options[1] == '11'


def test_yesnoquestion_attributes() -> None:
    """Test the public attributes of class YesNoQuestions"""
    ynq = YesNoQuestion(4, "are you human?")
    assert ynq.id == 4
    assert ynq. text == 'are you human?'


def test_checkboxquestion_attributes() -> None:
    """Test the attributes of class Checkbox"""
    cbq = CheckboxQuestion(5, "do you like dogs?", ['yes', 'no', 'sometimes'])
    assert cbq.id == 5
    assert cbq.text == "do you like dogs?"
    assert cbq._options == ['yes', 'no', 'sometimes']


def test_answer_attributes() -> None:
    """Test the public attributes of class Answer"""
    a = Answer("dogs")
    b = Answer(True)
    c = Answer(10)
    d = Answer(['a', 'b', 'c', 'd'])
    assert a.content == "dogs"
    assert b.content == True
    assert c.content == 10
    assert d.content == ['a', 'b', 'c', 'd']


def test_mcq_valid_invalid() -> None:
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

def test_num_valid_invalid() -> None:
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

def test_yn_valid_invalid() -> None:
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

def test_cbox_valid_invalid() -> None:
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

def test_mcq_similarity() -> None:
    """Test __str__ of class"""
    my_question = MultipleChoiceQuestion(1, "Acceptable Colours",
                                         ["R", "G", "B"])
    answer_1 = Answer("R")
    answer_2 = Answer("G")
    answer_3 = Answer("R")
    assert my_question.get_similarity(answer_1, answer_2) == 0.0
    assert my_question.get_similarity(answer_1, answer_3) == 1.0

def test_num_similarity() -> None:
    """Test __str__ of class"""
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

def test_yn_similarity() -> None:
    """Test __str__ of class"""
    my_question = YesNoQuestion(3, "Do you allow robots to paint?")

    answer_1 = Answer(True)
    answer_2 = Answer(False)
    answer_3 = Answer(True)
    assert my_question.get_similarity(answer_1, answer_2) == 0.0
    assert my_question.get_similarity(answer_1, answer_3) == 1.0

def test_cbox_similarity() -> None:
    """Test __str__ of class"""
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

def test_homo_crit() -> None:
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

def test_hetero_crit() -> None:
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

def test_lonely_crit() -> None:
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

def test_group_contains_true() -> None:
    """Test the __contains__ method for class Group when member is
    contained within Group's _members list"""
    quinn = Student(1, 'Quinn')
    tomasz = Student(2, 'Tomasz')
    ellen = Student(3, "Ellen")
    l = [quinn, tomasz, ellen]
    g = Group(l)
    assert g.__contains__(ellen) is True


def test_group_contains_false() -> None:
    """Test the __contains__ method for class Group when member is
    NOT contained within Group's _members list"""
    quinn = Student(1, 'Quinn')
    tomasz = Student(2, 'Tomasz')
    ellen = Student(3, "Ellen")
    l = [quinn, tomasz]
    g = Group(l)
    assert g.__contains__(ellen) is False


def test_get_members_is_shallow() -> None:
    """Test get_members method in class Group returns a shallow
    copy of the list in self._members"""
    quinn = Student(1, 'Quinn')
    tomasz = Student(2, 'Tomasz')
    ellen = Student(3, "Ellen")
    l = [quinn, tomasz, ellen]
    g = Group(l)
    assert id(g.get_members()) != id(g._members)


def test_grouping_attribute() -> None:
    """Test the attribute initialized in class Grouping"""
    g = Grouping()
    assert g._groups == []


def test_add_group_base_case() -> None:
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


def test_add_group_zero_members() -> None:
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
def test_add_group_zero_members2() -> None:
    """Test adding an empty Group to Grouping."""
    g = Group([])
    v = Grouping()
    v.add_group(g)
    assert v._groups == []


def test_add_group_duplicates() -> None:
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


def test_get_groups_is_shallow() -> None:
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


if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])

