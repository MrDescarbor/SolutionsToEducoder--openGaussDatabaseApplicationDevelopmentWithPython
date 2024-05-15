# 连接数据库,创建连接并返回连接对象
def connect():
    conn = psycopg2.connect(database="postgres", user="gaussdb", password="Passwd123@123", host="127.0.0.1", port="5432")

    return conn

 ##*********begin*********

# 向Client表中插入数据
#
# @param cid 客户编号
# @param cname 客户名称
# @param mail 客户邮箱
# @param idcard 客户身份证
# @param phone 客户手机号
# @param password 客户登录密码
def add_client(connection, cid,cname,mail,idcard,phone,password):
    cursor = connection.cursor()
    sql = "INSERT INTO client (c_id, c_name, c_mail, c_id_card, c_phone, c_password) VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.execute(sql, (cid, cname, mail, idcard, phone, password))
    connection.commit()


# 加载数据库模块
import psycopg2

# 从键盘读取两行记录，字段与字段之间用空格隔开，一条记录占一行
# 调用add_client()将输入数据插入client表
for i in range(1,3):
    connection = connect()
    input_data = input()
    commands = input_data.split(" ")
    id = commands[0];
    name = commands[1];
    mail = commands[2];
    idCard = commands[3];
    phone = commands[4];
    password = commands[5];
    add_client(connection, id, name, mail, idCard, phone, password);

##************end***********