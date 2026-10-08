from dataclasses import dataclass


class Student:
    def __init__(self, name, chinese,math,english ):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def str(self):
        return f"姓名:{self.name},语文:{self.chinese},数学:{self.math},英语:{self.english}"

    def update_grade(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class Edumaganment:
    def __init__(self):
        self.students = []

# 添加学生
    def add_student(self):
        name = input("请输入姓名:")
        for s in self.students:
            if s.name == name:
                return
        chinese = int(input("请输入语文成绩:"))
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            student = Student(name, chinese, math, english)
            self.students.append(student)

# 修改学生成绩
    def update_student_grade(self):
        name = input("请输入姓名:")
        for student in self.students:
            if student.name == name:
                chinese = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                    student.update_grade(chinese, math, english)
                break
            print("未找到该学生！")

# 删除学生
    def remove_student(self):
        name = input("请输入姓名:")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break
            print("未找到该学生！")

#找到指定学生
    def show_student(self):
        name = input("请输入姓名:")
        for student in self.students:
            if student.name == name:
                print(student.str())
                break
            print("未找到该学生！")

# 列出所有学生
    def list_students(self):
        for student in self.students:
            print(student.str())

#运行系统
    def run(self):
        while True:
            print()
            print("1. 添加学生")
            print("2. 修改学生成绩")
            print("3. 删除学生")
            print("4. 找到指定学生")
            print("5. 列出所有学生")
            print("6. 退出系统")
            print()
            choice = input("请输入你的选择:")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student_grade()
            elif choice == "3":
                self.remove_student()
            elif choice == "4":
                self.show_student()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                print("退出系统")
                break
            else:
                print("无效的选择，请重新输入")

Edumaganment().run()