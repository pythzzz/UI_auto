import redis

con_redis = redis.Redis(host='172.31.95.244', password='072620', port=6379, decode_responses=True)

# string格式
# 单值塞数据查数据
con_redis.set('abc', '123abc', ex=600)  # 设置失效时间，也可以直接用setex(key,value,time)，效果一致
print(con_redis.get('abc'))
# setnx 表示如果key不存在就塞数据，key已经存在了就不塞
con_redis.setnx('abc', '123')
print(con_redis.get('abc'))
# 批量塞数据,查数据
con_redis.mset({'1': '1', '2': '2'})
print(con_redis.mget('1', '2'))
print(con_redis.mget(['1', '2']))  # 等同于上一行
# 删除
con_redis.delete('abc')
print(con_redis.exists('abc'))
print(con_redis.get('abc'))
print('==' * 20)

# hash格式
# 单值
con_redis.hset('hash1', 'a', '1')
print(con_redis.hget('hash1', 'a'))
# 多值
con_redis.hmset('hash1', {'b': 2, 'c': 3, 'd': 4})
print(con_redis.hmget('hash1', ['a', 'b', 'c']))
print(con_redis.hmget('hash1', 'a', 'b', 'c'))  # 等同于上一行
# 获取name对应hash的所有键值
print(con_redis.hgetall('hash1'))
# 获取name对应的hash中键值对的个数
print(con_redis.hlen('hash1'))
# 获取name对应的hash中所有的key的值
print(con_redis.hkeys('hash1'))
# 获取name对应的hash中所有的value的值
print(con_redis.hvals('hash1'))
# 检查name对应的hash是否存在当前传入的key
print(con_redis.hexists('hash1', 'f'))
# 将name对应的hash中指定key的键值对删除
print(con_redis.hdel('hash1', 'a', 'b'))
print(con_redis.hgetall('hash1'))

print('==' * 20)

# list类型
# list中添加元素，每个元素都添加到list的最左边
con_redis.lpush('list1',1,2,3)
# 相对应的，元素添加到list的最右边
con_redis.rpush('list1',-1,-2,-3)
# 获取list中元素
# 根据索引切片获取
print(con_redis.lrange('list1',0,100))
# 根据索引单值获取
print(con_redis.lindex('list1',0))
# 从左边删除第一个元素
con_redis.lpop('list1')
# 从右边删除第一个元素
con_redis.rpop('list1')
print(con_redis.lrange('list1',0,-1))
# list中删除指定的值，并指定删除个数,如下，0表示删除所有
con_redis.lrem('list1',0,2)
con_redis.lrem('list1',0,1)
con_redis.lrem('list1',0,-1)
con_redis.lrem('list1',0,-2)
con_redis.lrem('list1',0,-3)
print(con_redis.lrange('list1',0,-1))
# 重置某个索引上的值,如下，修改左边第一位为100
con_redis.lset('list1',0,100)
print(con_redis.lrange('list1',0,-1))

con_redis.linsert('list1','before',1,1000)
print(con_redis.lrange('list1',0,-1))


print('=='*20)

# set集合操作
con_redis.sadd('set1',1,2,3)
# 获取集合中元素个数
print(con_redis.scard('set1'))
# 判断某个值是否是集合中元素
print(con_redis.sismember('set1',1))
print(con_redis.sismember('set1',-1))
# 查看集合中所有元素
print(con_redis.smembers('set1'))
# 删除集合中某些值
con_redis.srem('set1',1)
print(con_redis.smembers('set1'))