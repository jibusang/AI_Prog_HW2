
import os
import random
import time


#Student数据类、__init__、__str__、
class Student:
    # 初始化属性
    def __init__(self, name, gender, cls, sid, college):
        self.name = name
        self.gender = gender
        self.cls = cls
        self.student_id = sid
        self.college = college


    def __str__(self):
        return f"姓名:{self.name} 性别:{self.gender} 班级:{self.cls} 学号:{self.student_id} 学院:{self.college}"


    @staticmethod
    def check_student_id(sid):
        return sid.isdigit()


# 系统管理类
class ExamSystem:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_students(self):
        pass


if __name__ == "__main__":
    app = ExamSystem("人工智能编程语言学生名单.txt")