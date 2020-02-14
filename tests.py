from course import Student, Course
# from survey import Question, \
#     MultipleChoiceQuestion, \
#     NumericQuestion, \
#     YesNoQuestion,


def test_Student_attributes() -> None:
    """Test the public attributes of Student"""
    student = Student(1, 'John')
    assert student.name == 'John'
    assert student.id == 1


def test_Student_str_method() -> None:
    """Test the str method of Student"""
    student = Student(2, 'Jill')
    assert student.__str__() == 'Jill'


def test_Course_attributes() -> None:
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


if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])
