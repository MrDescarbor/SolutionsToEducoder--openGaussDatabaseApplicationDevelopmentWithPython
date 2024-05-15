# 连接数据库,创建连接并返回连接对象
def connect():
    conn = psycopg2.connect(database="postgres", user="gaussdb", password="Passwd123@123", host="127.0.0.1", port="5432")

    return conn

##*********begin*********
# 向Client表中插入数据
#
# @param cid 客户编号
# @param cardNum 银行卡号
def removeBankCard(connection, cid, cardNum):
    cursor = connection.cursor()
    try:
        sql = "DELETE FROM bank_card WHERE b_c_id = %s AND b_number = %s;"
        cursor.execute(sql, (cid, cardNum))
        connection.commit()
        n = cursor.rowcount
    except Exception as e:
        print(e)
        n = 0
    finally:
        cursor.close()
    return n
# 加载数据库模块
import psycopg2

# 从键盘读取两行记录，字段与字段之间用空格隔开，一条记录占一行
# 调用removeBankCard()注释银行卡

for i in range(1,3):
    connection = connect()
    input_data = input().strip()
    if input_data:
        data = input_data.split(" ")
        if len(data) == 2:
            cid = int(data[0])
            cardNum = data[1]
            n = removeBankCard(connection, cid, cardNum)
            if n > 0:
                print(f"已销卡数： {n}")
            else:
                print("销户失败，请检查客户编号或银行卡号！")

