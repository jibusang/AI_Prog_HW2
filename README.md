罗顺——25351038——人工智能编程语言第二次作业
1. 任务拆解与 AI 协作策略
我将整个编程任务分成四个步骤，逐步交给 AI 完成，确保代码结构清晰、功能逐步完善。
1：让 AI 先搭建最基础的框架，包括导入库、空的 Student 类、空的 ExamSystem 类，以及程序入口。 2：让 AI 完善 Student 类，实现属性初始化、打印方法、学号校验，并完善 ExamSystem 初始化。3：让 AI 实现核心功能：读取学生文件、异常处理、按学号查询、随机点名。4：让 AI 完成剩余全部功能：生成考场安排、生成准考证、菜单系统，让程序可以完整运行。
2. 核心 Prompt 迭代记录
初代 Prompt
帮我写一个学生考试系统的代码，要有类和方法。
AI 生成的问题 / 缺陷
代码结构不完整，没有面向对象规范，没有异常处理，没有按作业要求实现功能。
优化后的 Prompt
请按照 Python 面向对象规范写代码；必须使用 Student 类和 ExamSystem 类；必须包含文件读取、异常处理、学号校验、输入判断；不能使用课外库；代码要分步骤提交，一步步完善功能。
优化后 AI 生成的代码完全符合工程规范、作业要求，结构清晰，功能完整。
3. Debug 与异常处理记录
报错类型 / 漏洞现象
运行时出现 FileNotFoundError，提示找不到学生名单文件。
解决过程
我把报错信息发给 AI，AI 告诉我是文件路径错误或文件不存在。我按照 AI 的建议，找到了项目的文件夹，并将txt文件拖入其中，（其实是文件路径不会找）
4. 人工代码审查 (Code Review)
我选取 AI 生成的文件读取与数据加载核心逻辑代码，添加了中文注释，理解了代码运行机制。
# 从txt文件中读取学生数据，并封装成学生对象存入列表
def load_data(self):
    # 异常捕获：防止文件不存在、读取失败等错误
    try:
        # 以只读方式打开学生名单文件，使用utf-8编码避免中文乱码
        with open(self.file_name, "r", encoding="utf-8") as f:
            # 一次性读取文件所有行，保存到lines列表中
            lines = f.readlines()
            
            # 遍历每一行数据，跳过第一行表头（从第二行开始）
            for line in lines[1:]:
                # 去除每行首尾的空格、换行符等空白字符
                line = line.strip()
                
                # 如果当前行为空行，跳过不处理
                if not line:
                    continue
                
                # 按制表符\t切割字符串，将一行数据分成5个字段
                data = line.split("\t")
                
                # 判断切割后的数据是否为5个字段（姓名、性别、班级、学号、学院）
                if len(data) == 5:
                    #  创建Student对象
                    stu = Student(*data)
                    # 将创建好的学生对象添加到系统学生列表中
                    self.student_list.append(stu)
        
        # 数据读取完成后，打印成功提示与学生数量
        print(f"成功读取{len(self.student_list)}条学生数据")
    
    # 捕获文件不存在的异常
    except FileNotFoundError:
        print("错误：找不到学生名单txt文件")
    
    # 捕获其他所有未知异常，保证程序不崩溃
    except Exception as e:
        print(f"读取异常：{e}")
        
