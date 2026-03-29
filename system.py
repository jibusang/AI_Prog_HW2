# 导入允许的标准库
import os
import random
import time

# 学生实体类 空定义
class Student:
    def __init__(self):
        pass

# 考场系统主类 空定义
class ExamSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        self.student_list = []

# 程序入口启动
if __name__ == '__main__':
    app = ExamSystem("人工智能编程语言学生名单.txt")