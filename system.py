# 导入标准库
import os
import random
import time

class Student:
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

class ExamSystem:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
        self.load_students()


    def load_students(self):
        try:
            with open(self.filename,"r",encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines[1:]:
                    line = line.strip()
                    if not line:continue
                    arr = line.split("\t")
                    if len(arr)==5:
                        s = Student(*arr)
                        self.students.append(s)
            print(f"加载成功，共{len(self.students)}人")
        except FileNotFoundError:
            print("错误：找不到学生名单文件")
        except Exception as e:
            print("读取异常：",e)

    # 功能1：学号查询
    def search_by_id(self):
        sid = input("请输入学号：")
        if not Student.check_student_id(sid):
            print("学号必须是纯数字")
            return
        flag = False
        for item in self.students:
            if item.student_id == sid:
                print(item)
                flag = True
        if not flag:
            print("暂无该学号学生")

    # 功能2：随机点名+输入异常处理
    def random_call(self):
        total = len(self.students)
        while True:
            try:
                n = int(input("请输入点名人数："))
                if 1<=n<=total:break
                print("超出人数范围")
            except ValueError:
                print("请输入整数")
        res = random.sample(self.students,n)
        for r in res:
            print(r.name,r.student_id)

if __name__ == "__main__":
    app = ExamSystem("人工智能编程语言学生名单.txt")
    app.search_by_id()