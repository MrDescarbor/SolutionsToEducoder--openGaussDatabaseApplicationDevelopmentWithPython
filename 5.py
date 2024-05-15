# 连接数据库,创建连接并返回连接对象
def connect():
    conn = psycopg2.connect(database="postgres", user="gaussdb", password="Passwd123@123", host="127.0.0.1", port="5432")

    return conn

 ##*********begin*********
# 更改用户密码
#
# @param cmail 用户名号
# @param cpass 用户密码
# @param newpass 新设密码
# return 1/2/3/4 meaning 用户不存在/用户密码不对/密码修改成功/密码修改异常
def passwd(connection, cmail, cpass, newpass):
    cursor = connection.cursor()
    try:
        # 检查用户是否存在
        sql = "SELECT * FROM client WHERE c_mail = %s;"
        cursor.execute(sql, (cmail,))
        result = cursor.fetchone()
        if result is None:
            return 2
        
        # 检查密码是否正确
        sql = "SELECT * FROM client WHERE c_mail = %s AND c_password = %s;"
        cursor.execute(sql, (cmail, cpass))
        result = cursor.fetchone()
        if result is None:
            return 3

        # 更新密码
        sql = "UPDATE client SET c_password = %s WHERE c_mail = %s;"
        cursor.execute(sql, (newpass, cmail))
        connection.commit()
        return 1
    except Exception as e:
        print(e)
        return 4
    finally:
        cursor.close()


# 加载数据库模块
import psycopg2

# 从键盘读取两行记录，字段与字段之间用空格隔开，一条记录占一行。
# 检查两次密码输入是否一致，然后调用passwd()函数修改密码
connection = connect()
for i in range(1,5):
    input_data = input().strip()
    if input_data:
        data = input_data.split(" ")
        if len(data) == 4:
            email = data[0]
            passw = data[1]
            newpass1 = data[2]
            newpass2 = data[3]
            if newpass1 == newpass2:
                result = passwd(connection, email, passw, newpass1)
                if result == 1:
                    print(f'第{i}组:密码修改成功')
                if result == 3:
                    print(f'第{i}组:用户密码不正确')
                if result == 2:
                    print(f'第{i}组:用户不存在')
            else:
                print(f"第{i}组:两次输入的密码不一致")

##************end***********