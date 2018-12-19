import os
import pymongo
import datetime

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/")
mongo = pymongo.MongoClient(MONGO_URI)

_db = mongo["stock"]

coll = getattr(_db, "mv_like")

# 查看一个 item 中的所有字段
# instance = coll.find().next()
# key_list = list(instance.keys())

# for key in key_list:
#     print(key)

# _id
# InfoPublDate
# EndDate
# CompanyCode
# TotalNonCurrentLiability
# code
# SEWithoutMI
# CashEquialents
# NPFromParentCompanyOwners
# NetProfit
# TotalLiability

demo_code_list = ["SZ000001", "SZ000002"]
demo_trade_date = datetime.datetime(2005, 10, 1)

# 查询出一些测试数据
# cur = list(coll.find())
# for instance in cur[101:105]:
#     print(instance.get("code"))
#     print(instance.get("InfoPublDate"))
#     print(instance.get("TotalLiability"))
#     print(instance.get("NetProfit"))
#     print()

# SZ000001
# 1994-04-16 00:00:00
# 8114407110.59
# 273311145.21
#
# SZ000001
# 1991-02-10 00:00:00
# None
# None
#
# SZ000001
# 2005-04-26 00:00:00
# 196365200873.0
# 154126411.0
#
# SZ000001
# 1995-08-11 00:00:00
# 15571604045.48
# 216501117.68

# ----------------------

# SZ000002
# 1993-03-21 00:00:00
# 725313856.14
# 65421050.81
#
# SZ000002
# 1994-08-20 00:00:00
# 1264800648.66
# 77072057.73
#
# SZ000002
# 2006-10-31 00:00:00
# 30469722339.52
# 1363735879.79
#
# SZ000002
# 2007-03-20 00:00:00
# 31501921434.67
# 2308440478.62

group_query = {'_id': "$code",
               'date': {'$last': '$InfoPublDate'},
               "totalliability": {"$last": "$TotalLiability"},
               "netprofit": {"$last": "$NetProfit"},
               }

ret = coll.aggregate([{'$match': {'code': {'$in': demo_code_list},
                                  'InfoPublDate': {'$lte': demo_trade_date}}},
                      {'$group': group_query}])

for r in ret:
    print(r)

# {'_id': 'SZ000002', 'date': datetime.datetime(2004, 4, 19, 0, 0), 'totalliability': 6298225548.88, 'netprofit': 110005143.63}
# {'_id': 'SZ000001', 'date': datetime.datetime(2003, 4, 24, 0, 0), 'totalliability': 158546187482.0, 'netprofit': 153313141.0}
