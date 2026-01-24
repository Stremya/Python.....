class Student:
    def __init__(self, name: str, age: int, course: int, gpa: float, student_id: str):
        self.name = name
        self.age = age
        self.course = course
        self.gpa = gpa
        self.student_id = student_id

    def increase_course(self):
        if self.course < 5:
            self.course += 1

    def update_gpa(self, new_gpa: float):
        if 0 <= new_gpa <= 5:
            self.gpa = new_gpa
        else:
            raise ValueError("GPA должен быть в диапозоне от 0 до 5")



# Студенты
student1 = Student(
    name="Иван Петров",
    age=19,
    course=1,
    gpa=4.2,
    student_id="ST001"
)

student2 = Student(
    name="Мария Сидорова",
    age=20,
    course=2,
    gpa=4.7,
    student_id="ST002"
)

print("=== СТУДЕНТЫ ===")
print(f"{student1.name}, курс: {student1.course}, GPA: {student1.gpa}")
print(f"{student2.name}, курс: {student2.course}, GPA: {student2.gpa}")