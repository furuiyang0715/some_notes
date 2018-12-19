# 获取mongo数据库中的集合的方法
import os
import pymongo

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/")
mongo = pymongo.MongoClient(MONGO_URI)

_db = mongo["stock"]
# coll 即生成了针对mongodb的集合操作的连接对象
coll = getattr(_db, "soft_base")

