"""
数组二分查找算法
bisect 模块接受排序后的列表
"""
"""
该bisect()功能对于数字表查找很有用。
本示例用于bisect()根据一组有序的数字断点来查找考试成绩（例如）的字母等级：90和更高是'A'，80到89是'B'，依此类推：
"""
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


if __name__ == "__main__":
    grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(grades)
