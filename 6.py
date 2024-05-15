# 连接数据库,创建连接并返回连接对象
import psycopg2
def connect():
    conn = psycopg2.connect(database="postgres", user="gaussdb", password="Passwd123@123", host="127.0.0.1", port="5432")

    return conn

##*********begin*********
# 转账
#
# @param src 转出账户
# @param dest 转入账户
# @param amount 转账金额
# return 0/1 meaning 转账成功/转账失败(不细分失败原因)
def transfer_money(conn, src, dest, amount):
    cursor = conn.cursor()
    try:
        conn.autocommit = False

        # 扣减转出账户的金额
        sql = "UPDATE bank_card SET b_balance = b_balance - %s WHERE b_number = %s;"
        cursor.execute(sql, (amount, src))

        # 增加转入账户的金额
        sql = "UPDATE bank_card SET b_balance = b_balance + %s WHERE b_number = %s AND b_type = '储蓄卡';"
        cursor.execute(sql, (amount, dest))

        # 处理信用卡账户的金额
        sql = "UPDATE bank_card SET b_balance = b_balance - %s WHERE b_number = %s AND b_type = '信用卡';"
        cursor.execute(sql, (amount, dest))

        # 检查转出账户余额
        sql = "SELECT * FROM bank_card WHERE b_number = %s AND b_type = '储蓄卡';"
        cursor.execute(sql, (src,))
        result = cursor.fetchone()
        if not result:
            conn.rollback()
            return 1
        else:
            if result[3] < 0:  # Assuming b_balance is the 4th column
                conn.rollback()
                return 1
            else:
                sql = "SELECT * FROM bank_card WHERE b_number = %s;"
                cursor.execute(sql, (dest,))
                result = cursor.fetchone()
                if not result:
                    conn.rollback()
                    return 1
                else:
                    conn.commit()
                    return 0
    except Exception as e:
        print(e)
        conn.rollback()
        return 1
    finally:
        cursor.close()


# 从键盘读取转账需求：转出账户，转入账户，转账金额。三项之彰用空格隔开，一笔转账需求占一行。
# 对每一笔转账业务，调用transfer_money()函数转账，根据返回结果输出对应提示信息

conn = connect()
iteration = 1
for iteration in range(1,10) :
    try:
        input_data = input()
        commands = input_data.split(" ")

        payer_card = commands[0]

        payee_card = commands[1]

        amount = float(commands[2])
        
        if transfer_money(conn, payer_card, payee_card, amount) == 0:
            print(f"第{iteration}笔：转账成功")
        else:
            print(f"第{iteration}笔：转账失败，请核对卡号，卡类型及卡余额")
        iteration += 1
        
    except Exception as e:
        pass
    

##************end***********


# 从键盘读取转账需求：转出账户，转出账户，转账金额。三项之彰用空格隔开，一笔转账需求占一行。
# 对每一笔转账业务，调用transfer_money()函数转账，根据返回结果输出对应提示信息
##************end***********
