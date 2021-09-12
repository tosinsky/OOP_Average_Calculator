class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def get_name(self):
        return self.name

    def get_courses(self):
        names = []
        for course in self.courses:
            names.append(course.get_name())
        return names

    def get_total_ects(self):
        total_ects = 0
        for course in self.courses:
            total_ects += course.get_ects()
        return total_ects

    def get_average(self):
        average = 0
        temp = 0
        for course in self.courses:
            temp += course.get_grade() * course.get_ects()
        average = temp / self.get_total_ects()
        return average
        
     def add_course(self, course):
        self.courses.append(course)


class Course:
    # add semester and searching by it
    def __init__(self, name, ects):
        self.name = name
        self.ects = ects

    def get_name(self):
        return self.name

    def get_ects(self):
        return self.ects
        
    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

damian = Student("Damian")
print(damian.get_name())

proba = Course("Probabilistyka", 4)
proba.set_grade(4)

pelp = Course("Podstawy Elektroniki i Pomiarów", 3)
pelp.set_grade(5)

tmkt = Course("Techniki Modulacji i Kodowania", 5)
tmkt.set_grade(4)

damian.add_course(proba)
damian.add_course(pelp)
damian.add_course(tmkt)

print(damian.get_courses())
print(damian.get_total_ects())
print(damian.get_average())
