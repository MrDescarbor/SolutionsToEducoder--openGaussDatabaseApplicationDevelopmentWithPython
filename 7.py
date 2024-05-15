# 连接数据库,创建连接并返回连接对象
def connect():
    conn = psycopg2.connect(database="postgres", user="gaussdb", password="Passwd123@123", host="127.0.0.1", port="5432")

    return conn
##*********begin*********

# 向sc表中插入数据
#
# @param sno 学号
# @param colName 列名
# @param colValue 列值
def add_sc(conn, sno, colName, colValue):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO sc (sno, col_name, col_value) VALUES (%s, %s, %s);"
        if colValue:
            cursor.execute(sql, (sno, colName, colValue))
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()

# 加载数据库模块
import psycopg2

conn = connect()
cursor = conn.cursor()
try:
    cursor.execute("SELECT * FROM entrance_exam;")
    rows = cursor.fetchall()
    for row in rows:
        sno = row[0]
        subjects = ["chinese", "math", "english", "physics", "chemistry", "biology", "history", "geography", "politics"]
        for i, subject in enumerate(subjects, start=1):
            score = row[i]
            if score != 0:
                add_sc(conn, sno, subject, score)
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
# 读取高考成绩entrance_exam表，并将chinese/math/english/physics/chemistry/biology/history/geography/politics
# 各科成绩，调用add_sc()，转成(学号，科目，成绩)的形式，存入sc表。
##************end***********