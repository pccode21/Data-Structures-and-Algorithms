import sys
import os
os.chdir(r'.\Data-Structures-and-Algorithms\function')  # 创建工作路径
print(sys.getdefaultencoding())  # 用sys模块检查默认的编码
path = 'segismundo.txt'
with open(path) as f:  # 用with语句可以更容易地清理打开的文件,这样可以在退出代码块时，自动关闭文件
    lines = [x.rstrip() for x in f]  # rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
print(lines)
# 向文件写入，可以使用文件的write或writelines方法
with open('tmp.txt', 'w') as f:
    f.writelines(x for x in open(path) if len(x) > 1)  # 无空行写入
with open('tmp.txt') as f:
    lines = f.readlines()
print(lines)
