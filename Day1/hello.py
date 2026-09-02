class Student():
    def __init__(self):
        self.gpa = 5.0
        self.name = "Sara"
        self.cources = ["Co-Op training", "Android app dev"]

class Cource():
    def __init__(self, name, teacher, section, level, univercity):
        self.name = name
        self.teacher = teacher
        self.section = section
        self.level = level
        self.univercity = univercity

    def get_name(self):
        return self.name


def main():
    # x = Student()
    # x.cources.pop()
    # print(x.cources)

    Math_101 = Cource(5, "khalyl", "A1", 0, "IEU")
    print(type(Math_101.get_name()))

if __name__ == "__main__":
    main()