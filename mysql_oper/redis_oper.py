import redis

con_redis = redis.Redis(host='172.31.81.52', password='072620', port=6379, decode_responses=True)

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
