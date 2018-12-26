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

    start_year = start_date.year
    s1 = datetime.datetime(start_year, 3, 31, 0, 0, 0)
    s2 = datetime.datetime(start_year, 6, 30, 0, 0, 0)
    s3 = datetime.datetime(start_year, 9, 30, 0, 0, 0)
    s4 = datetime.datetime(start_year, 12, 31, 0, 0, 0)

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

    end_year = end_date.year
    e1 = datetime.datetime(end_year, 3, 31, 0, 0, 0)
    e2 = datetime.datetime(end_year, 6, 30, 0, 0, 0)
    e3 = datetime.datetime(end_year, 9, 30, 0, 0, 0)
    e4 = datetime.datetime(end_year, 12, 31, 0, 0, 0)

    if end_date >= e4:
        date_list.extend([e1, e2, e3, e4])
    elif end_date >= e3:
        date_list.extend([e1, e2, e3])
    elif end_date >= e2:
        date_list.extend([e1, e2])
    elif end_date >= e1:
        date_list.append(e1)
    else:
        pass

    middle_year = start_year + 1
    while middle_year < end_year:
        m1 = datetime.datetime(middle_year, 3, 31, 0, 0, 0)
        m2 = datetime.datetime(middle_year, 6, 30, 0, 0, 0)
        m3 = datetime.datetime(middle_year, 9, 30, 0, 0, 0)
        m4 = datetime.datetime(middle_year, 12, 31, 0, 0, 0)
        date_list.extend([m1, m2, m3, m4])
        middle_year += 1

    dates = [yyyymmdd_date(date) for date in date_list]
    return np.array(dates)


def yyyymmdd_date(dt: datetime) -> int:
    return dt.year * 10000 + dt.month * 100 + dt.day


def gen_q_last_day_list(start_date: datetime.datetime, end_date: datetime.datetime, q):
    """
    获取两个时间点之间包含的所有某一季度末日期
    :param start_date:
    :param end_date:
    :param q:
    :return:
    """
    quarter_map = {
        1: (3, 31),
        2: (6, 30),
        3: (9, 30),
        4: (12, 31)
    }
    _month, _day = quarter_map.get(q)

    start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
    end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)

    date_list = list()

    start_year = start_date.year
    s = datetime.datetime(start_year, _month, _day, 0, 0, 0)
    if start_date <= s:
        date_list.append(s)

    end_year = end_date.year
    e = datetime.datetime(end_year, _month, _day, 0, 0, 0)
    if end_date >= e:
        date_list.append(e)

    middle_year = start_year + 1
    while middle_year < end_year:
        m = datetime.datetime(middle_year, _month, _day, 0, 0, 0)
        date_list.append(m)
        middle_year += 1
    return date_list


def gen_1q_last_day_list(start_date: datetime.datetime, end_date: datetime.datetime):
    """
    获取两个时间点之间包含的所有第一季度末日期
    :param start_date:
    :param end_date:
    :return:
    """
    start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
    end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)

    date_list = list()

    start_year = start_date.year
    s1 = datetime.datetime(start_year, 3, 31, 0, 0, 0)
    if start_date <= s1:
        date_list.append(s1)

    end_year = end_date.year
    e1 = datetime.datetime(end_year, 3, 31, 0, 0, 0)
    if end_date >= e1:
        date_list.append(e1)

    middle_year = start_year + 1
    while middle_year < end_year:
        m1 = datetime.datetime(middle_year, 3, 31, 0, 0, 0)
        date_list.append(m1)
        middle_year += 1
    return date_list


def gen_2q_last_day_list(start_date: datetime.datetime, end_date: datetime.datetime):
    """
    获取两个时间点之间包含的所有第二季度末日期
    :param start_date:
    :param end_date:
    :return:
    """
    start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
    end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)

    date_list = list()

    start_year = start_date.year
    s2 = datetime.datetime(start_year, 6, 30, 0, 0, 0)
    if start_date <= s2:
        date_list.append(s2)

    end_year = end_date.year
    e2 = datetime.datetime(end_year, 6, 30, 0, 0, 0)
    if end_date >= e2:
        date_list.append(e2)

    middle_year = start_year + 1
    while middle_year < end_year:
        m2 = datetime.datetime(middle_year, 6, 30, 0, 0, 0)
        date_list.append(m2)
        middle_year += 1
    return date_list


def gen_3q_last_day_list(start_date: datetime.datetime, end_date: datetime.datetime):
    """
    获取两个时间点之间包含的所有第三季度末日期
    :param start_date:
    :param end_date:
    :return:
    """
    start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
    end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)

    date_list = list()

    start_year = start_date.year
    s3 = datetime.datetime(start_year, 9, 30, 0, 0, 0)
    if start_date <= s3:
        date_list.append(s3)

    end_year = end_date.year
    e3 = datetime.datetime(end_year, 9, 30, 0, 0, 0)
    if end_date >= e3:
        date_list.append(e3)

    middle_year = start_year + 1
    while middle_year < end_year:
        m3 = datetime.datetime(middle_year, 9, 30, 0, 0, 0)
        date_list.append(m3)
        middle_year += 1
    return date_list


def gen_4q_last_day_list(start_date: datetime.datetime, end_date: datetime.datetime):
    """
    获取两个时间点之间包含的所有第四季度末日期
    :param start_date:
    :param end_date:
    :return:
    """
    start_date = datetime.datetime.combine(start_date.date(), datetime.time.min)
    end_date = datetime.datetime.combine(end_date.date(), datetime.time.max)

    date_list = list()

    start_year = start_date.year
    s4 = datetime.datetime(start_year, 12, 31, 0, 0, 0)
    if start_date <= s4:
        date_list.append(s4)

    end_year = end_date.year
    e4 = datetime.datetime(end_year, 12, 31, 0, 0, 0)
    if end_date >= e4:
        date_list.append(e4)

    middle_year = start_year + 1
    while middle_year < end_year:
        m4 = datetime.datetime(middle_year, 12, 31, 0, 0, 0)
        date_list.append(m4)
        middle_year += 1
    return date_list


if __name__ == "__main__":
    _start_date = datetime.datetime(2015, 7, 27)
    _end_date = datetime.datetime(2019, 1, 11)
    res = gen_quarter_last_day(_start_date, _end_date)
    print(res)

    res1 = gen_1q_last_day_list(_start_date, _end_date)
    r1 = gen_q_last_day_list(_start_date, _end_date, 1)
    print(res1)
    print(res1 == r1)

    res2 = gen_2q_last_day_list(_start_date, _end_date)
    r2 = gen_q_last_day_list(_start_date, _end_date, 2)
    print(res2)
    print(res2 == r2)

    res3 = gen_3q_last_day_list(_start_date, _end_date)
    r3 = gen_q_last_day_list(_start_date, _end_date, 3)
    print(res3)
    print(res3 == r3)

    res4 = gen_4q_last_day_list(_start_date, _end_date)
    r4 = gen_q_last_day_list(_start_date, _end_date, 4)
    print(res4)
    print(res4 == r4)

