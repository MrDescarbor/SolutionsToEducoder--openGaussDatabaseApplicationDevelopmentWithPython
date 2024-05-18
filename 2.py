import psycopg2

def main():
    try:
        # 连接数据库
        conn = psycopg2.connect(
            dbname="postgres",
            user="gaussdb",
            password="Passwd123@123",
            host="localhost",
            port="5432"
        )
        
        # 创建游标
        cur = conn.cursor()

        # 用户输入
        login_name = input("请输入用户名：")
        login_pass = input("请输入密码：")

        # 执行查询
        cur.execute("SELECT * FROM client WHERE c_mail = %s;", (login_name,))
        row = cur.fetchone()
        # 验证用户名和密码
        if row:
            if row[5].strip() == login_pass:
                print("登录成功。")
            else:
                print("用户名或密码错误！")
        else:
            print("用户名或密码错误！")

    except psycopg2.Error as e:
        print("数据库错误:", e)
    finally:
        # 关闭连接
        if conn is not None:
            conn.close()

main()
