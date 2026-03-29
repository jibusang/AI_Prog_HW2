# 导入允许的标准库
import os
import random
import time


class Student:
    # 初始化五大属性
    def __init__(self, name, gender, cls, sid, college):
        self.name = name
        self.gender = gender
        self.cls = cls
        self.student_id = sid
        self.college = college


    def __str__(self):
        return f"姓名：{self.name}，性别：{self.gender}，班级：{self.cls}，学号：{self.student_id}，学院：{self.college}"


    @staticmethod
    def check_sid(sid):
        return sid.isdigit()

# 考场系统主类
class ExamSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        self.student_list = []
        self.load_data()

    # 文件读取
    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                lines = f.readlines()
                # 跳过表头
                for line in lines[1:]:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split("\t")
                    if len(data) == 5:
                        stu = Student(*data)
                        self.student_list.append(stu)
            print(f"成功读取{len(self.student_list)}条学生数据")
        except FileNotFoundError:
            print("错误：找不到学生名单txt文件")
        except Exception as e:
            print(f"读取异常：{e}")

    # 功能1：按学号查询
    def search_by_sid(self):
        sid = input("请输入查询学号：")
        if not Student.check_sid(sid):
            print("学号必须为纯数字")
            return
        find_flag = False
        for s in self.student_list:
            if s.student_id == sid:
                print("\n====查询结果====")
                print(s)
                find_flag = True
        if not find_flag:
            print("暂无该学号对应的学生")

    # 功能2：随机点名 含输入异常限制
    def random_call_student(self):
        total = len(self.student_list)
        while True:
            try:
                num = int(input(f"请输入点名人数(1~{total})："))
                if 1 <= num <= total:
                    break
                else:
                    print("超出合法人数范围")
            except ValueError:
                print("请输入整数数字！")
        res = random.sample(self.student_list, num)
        print("\n====随机点名名单====")
        for idx, item in enumerate(res,1):
            print(f"{idx}. {item.name} 学号：{item.student_id}")

    # 功能3：生成考场安排表
    def create_exam_table(self):
        if not self.student_list:
            print("无学生数据，无法生成")
            return
        shuffle_stu = random.sample(self.student_list, len(self.student_list))
        now_time = time.strftime("生成时间：%Y-%m-%d %H:%M:%S", time.localtime())
        with open("考场安排表.txt","w",encoding="utf-8") as f:
            f.write(now_time + "\n\n")
            f.write("座位号\t姓名\t学号\n")
            for seat,stu in enumerate(shuffle_stu,1):
                f.write(f"{seat}\t{stu.name}\t{stu.student_id}\n")
        print("考场安排表生成完毕")
        return shuffle_stu

    # 功能4：生成准考证文件夹和单个文件
    def create_all_ticket(self):
        stu_arr = self.create_exam_table()
        if not stu_arr:
            return
        folder_name = "准考证"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        for seat,stu in enumerate(stu_arr,1):
            path = os.path.join(folder_name,f"{seat:02d}.txt")
            with open(path,"w",encoding="utf-8") as f:
                f.write(f"考场座位号：{seat}\n")
                f.write(f"姓名：{stu.name}\n")
                f.write(f"学号：{stu.student_id}\n")
        print("全部个人准考证生成完成")

    # 主菜单界面
    def main_menu(self):
        while True:
            print("\n========学生信息与考场管理系统========")
            print("1. 按学号查询学生信息")
            print("2. 课堂随机点名")
            print("3. 生成考场安排总表")
            print("4. 批量生成个人准考证")
            print("0. 退出系统")
            choice = input("请输入功能编号(0~4)：")
            if choice == "1":
                self.search_by_sid()
            elif choice == "2":
                self.random_call_student()
            elif choice == "3":
                self.create_exam_table()
            elif choice == "4":
                self.create_all_ticket()
            elif choice == "0":
                print("程序正常退出，作业完成！")
                break
            else:
                print("输入无效，请输入0~4之间数字")

# 程序入口启动
if __name__ == '__main__':
    app = ExamSystem("人工智能编程语言学生名单.txt")
    app.main_menu()