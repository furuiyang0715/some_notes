import datetime

import numpy as np


def gen_quarter_last_day(start_date: datetime.datetime, end_date: datetime.datetime):
    """
    获取两个时间点之间包含的所有季度末日期
    :param start_date:
    :param end_date:
    :return:
    """
    start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
    end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)

    date_list = list()

    # 获取start_date的四个季度时间点
    start_year = start_date.year
    s1 = datetime.datetime(start_year, 3, 31, 0, 0, 0)
    s2 = datetime.datetime(start_year, 6, 30, 0, 0, 0)
    s3 = datetime.datetime(start_year, 9, 30, 0, 0, 0)
    s4 = datetime.datetime(start_year, 12, 31, 0, 0, 0)
    # 判断start_date位置
    if start_date <= s1:
        date_list.extend([s1, s2, s3, s4])
    elif start_date <= s2:
        date_list.extend([s2, s3, s4])
    elif start_date <= s3:
        date_list.extend([s3, s4])
    elif start_date <= s4:
        date_list.append(s4)
    else:
        raise Exception(f"该日期错误: {start_date}")  # 应该不会走到这一步

    # 获取end_date的四个季度时间点
    end_year = end_date.year
    e1 = datetime.datetime(end_year, 3, 31, 0, 0, 0)
    e2 = datetime.datetime(end_year, 6, 30, 0, 0, 0)
    e3 = datetime.datetime(end_year, 9, 30, 0, 0, 0)
    e4 = datetime.datetime(end_year, 12, 31, 0, 0, 0)
    # 判断end_date位置
    if end_date >= e4:
        date_list.extend([e1, e2, e3, e4])
    elif start_date >= e3:
        date_list.extend([e1, e2, e3])
    elif start_date >= e2:
        date_list.extend([e1, e2])
    elif start_date >= e1:
        date_list.append(e1)
    else:
        pass  # 时间未到第一季度末 不做处理

    # 获取中间年份的所有季度时间点
    middle_year = start_year + 1
    while middle_year < end_year:
        m1 = datetime.datetime(middle_year, 3, 31, 0, 0, 0)
        m2 = datetime.datetime(middle_year, 6, 30, 0, 0, 0)
        m3 = datetime.datetime(middle_year, 9, 30, 0, 0, 0)
        m4 = datetime.datetime(middle_year, 12, 31, 0, 0, 0)
        date_list.extend([m1, m2, m3, m4])
        middle_year += 1

    # # test
    # for date in date_list:
    #     print(date)

    # 整理输出格式
    dates = [yyyymmdd_date(date) for date in date_list]
    return np.array(dates)


def yyyymmdd_date(dt: datetime) -> int:
    return dt.year * 10000 + dt.month * 100 + dt.day


if __name__ == "__main__":
    _start_date = datetime.datetime(2015, 7, 27)
    _end_date = datetime.datetime(2019, 1, 11)
    res = gen_quarter_last_day(_start_date, _end_date)
    print(res)

