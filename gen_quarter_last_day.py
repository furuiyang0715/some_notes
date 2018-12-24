"""
获取两个时间点之间
包含的所有季度末日期
"""

import datetime

start_date = datetime.datetime(2015, 7, 27)
start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
end_date = datetime.datetime(2019, 1, 11)
end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)
# print(start_date)
# print(end_date)


# 获取start_date的四个季度时间点
start_year = start_date.year
# print(start_year)  # 2015
q1 = datetime.datetime(start_year, 3, 31, 0, 0, 0)
q2 = datetime.datetime(start_year, 6, 30, 0, 0, 0)
q3 = datetime.datetime(start_year, 9, 30, 0, 0, 0)
q4 = datetime.datetime(start_year, 12, 31, 0, 0, 0)

date_list = list()
# 判断start_date在哪个时间点之间
if start_date <= q1:
    date_list.extend([q1, q2, q3, q4])
elif start_date <= q2:
    date_list.extend([q2, q3, q4])
elif start_date <= q3:
    date_list.extend([q3, q4])
elif start_date <= q4:
    date_list.append(q4)
else:
    raise Exception(f"该日期错误: {start_date}")  # 应该不会走到这一步
print(date_list)


# 获取end_date的四个季度时间点
end_year = end_date.year
# print(end_year)  # 2019
e1 = datetime.datetime(end_year, 3, 31, 0, 0, 0)
e2 = datetime.datetime(end_year, 6, 30, 0, 0, 0)
e3 = datetime.datetime(end_year, 9, 30, 0, 0, 0)
e4 = datetime.datetime(end_year, 12, 31, 0, 0, 0)
if end_date >= e4:
    date_list.extend([e1, e2, e3, e4])
elif start_date >= e3:
    date_list.extend([e1, e2, e3])
elif start_date >= e2:
    date_list.extend([e1, e2])
elif start_date >= e1:
    date_list.append(e1)
else:
    pass
print()
print()
print(date_list)

# 获取中间年份的所有季度时间点
middle_year = start_year + 1
while middle_year < end_year:
    m1 = datetime.datetime(middle_year, 3, 31, 0, 0, 0)
    m2 = datetime.datetime(middle_year, 6, 30, 0, 0, 0)
    m3 = datetime.datetime(middle_year, 9, 30, 0, 0, 0)
    m4 = datetime.datetime(middle_year, 12, 31, 0, 0, 0)
    date_list.extend([m1, m2, m3, m4])
    middle_year += 1

# print()
# print()
# print(date_list)
for date in date_list:
    print(date)

