# 有关python时间处理的相关操作的总结
import datetime
import time
import calendar

# 几种时间对象

# datetime格式的当前时间
now = datetime.datetime.now()
print(now)
# 2018-12-19 09:30:50.377268

# timestamp
_timestamp = time.time()
print(_timestamp)
# 1545183149.9541223

# time tuple
print(time.localtime())
#  time.struct_time(tm_year=2018, tm_mon=12, tm_mday=19, tm_hour=9, tm_min=34, tm_sec=0, tm_wday=2,
#  tm_yday=353, tm_isdst=0)

# string
print(now.strftime("%Y-%m-%d %H:%M:%S"))
# 2018-12-19 09:35:28

# date
print(now.date())
# 2018-12-19

# datetime的基本操作

# 获取当前datetime
print(datetime.datetime.now())
# 2018-12-19 09:38:07.379948

# 获取当天的date
print(datetime.date.today())
# 2018-12-19

# 获取明天/之后n天
print(datetime.date.today()+datetime.timedelta(days=1))
# 2018-12-20

# 获取之前n天
print(datetime.date.today()-datetime.timedelta(days=3))
# 2018-12-16

# 获取当天的开始时间和结束时间
start = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
print(start)  # 2018-12-19 00:00:00
end = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
print(end)  # 2018-12-19 23:59:59.999999

# 获取两个datetime的时间差
life_long = (datetime.datetime.now() - datetime.datetime(1994, 4, 14, 0, 0, 0)).total_seconds()
print(life_long)  # 778931169.625487

# 获取本周的最后一天
today = datetime.date.today()
today_weekday = today.weekday()
print(today_weekday)  # 2
sunday = today + datetime.timedelta(6-today.weekday())
print(sunday)  # 2018-12-23

# 获取本月的最后一天
today = datetime.date.today()
print(today.year, today.month)  # 2018 12
_, last_day_num = calendar.monthrange(today.year, today.month)
print(_, last_day_num)  # 5 31
last_day = datetime.date(today.year, today.month, last_day_num)
print(last_day)  # 2018-12-31

# 获取上月的最后一天 （有可能跨年）
today = datetime.date.today()
# 首先获取到本月的第一天
first = datetime.date(year=today.year, month=today.month, day=1)
# 减去 1d 获取到上月的最后一天
last_month_last_day = first - datetime.timedelta(days=1)
print(last_month_last_day)

# 关系转换
# datetime --> string
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 2018-12-19 10:02:24

# string --> datetime
print(datetime.datetime.strptime("2018-12-19 10:02:24", "%Y-%m-%d %H:%M:%S"))
# # 2018-12-19 10:02:24

# datetime --> timetuple
print(now.timetuple())

# timetuple --> datetime
# timetuple --> timestamp --> datetime

# datetime --> date
print(now.date())

# date --> datetime
# 当前datetime
print(datetime.time())
print(datetime.datetime.combine(datetime.date.today(), datetime.time(10, 10, 0)))
# 获取当天最小时间的datetime
print(datetime.datetime.combine(datetime.date.today(), datetime.time.min))

# datetime --> timestamp
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())
print(timestamp)  # 1545185654.0

# timestamp --> datetime
print(datetime.datetime.fromtimestamp(timestamp))

