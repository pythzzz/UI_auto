# 导入pymysql
import pymysql
import time


# 定义一个函数
# 这个函数用来创建连接(连接数据库用）
def mysql_db():
    # 连接数据库肯定需要一些参数
    conn = pymysql.connect(
        host="172.31.81.52",
        port=3306,
        database="db1",
        charset="utf8",
        user="yyy",
        password="072620yY."
    )

    cursor=conn.cursor()
    sql='select * from user'
    cursor.execute(sql)
    result=cursor.fetchall()
    return result


if __name__ == '__main__':
    print(mysql_db())
    # print(time.strptime('20221202 160013','%Y%m%d %H%M%S'))

