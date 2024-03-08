class StudentGrade:
    def __init__(self, student_name='', grade=0.0) -> None:
        self.student_name = student_name
        self.grade = grade


class Gradebook:
    def __init__(self, student_grades=[]) -> None:
        self.studentGrades = student_grades

    def highest_grade(self):
        highest = 0.0
        for i in self.studentGrades:
            highest = i.grade if i.grade > highest else highest
        return highest

    def average_grade(self):
        avg_sum = 0.0
        for i in self.studentGrades:
            avg_sum += i.grade
        return round(avg_sum/len(self.studentGrades), 2)

    def anyone_with_Q(self):
        for i in self.studentGrades:
            if i.student_name.lower().startswith('q'):
                return True
        return False

    def students_who_passed(self):
        passed = []
        for i in self.studentGrades:
            if i.grade > 50:
                passed.append(i.student_name)
        return passed

    def longest_name(self):
        first = ""
        max_len = ""
        for i in self.studentGrades:
            if len(i.student_name) == len(max_len):
                first = max_len
                max_len = i.student_name
            elif len(i.student_name) > len(max_len):
                max_len = i.student_name
        return first if len(max_len) == len(first) else max_len


student_grades = [StudentGrade("saad", 51), StudentGrade("faisal", 59), StudentGrade("taha", 21), StudentGrade(
    "noman", 91), StudentGrade("Qureshi", 11), StudentGrade("kashif", 71), StudentGrade("abdullah", 31), StudentGrade("rafay", 61)]

grade_book = Gradebook(student_grades)
print(grade_book.anyone_with_Q())
print(grade_book.longest_name())
print(grade_book.average_grade())
print(grade_book.highest_grade())
print(grade_book.students_who_passed())
