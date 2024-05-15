 ##*********begin*********
import psycopg2
# Connect to your openGuass DB
conn = psycopg2.connect(database="postgres", user="gaussdb", password="Passwd123@123", host="127.0.0.1", port="5432")
# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a query
cur.execute("SELECT c_name, c_mail, c_phone FROM client where c_mail is not Null")
# Retrieve query results
records = cur.fetchall()

print("姓名\t邮箱\t\t\t\t电话")
for x in records:
    a = x[0]
    b = x[1]
    c = x[2]
    print(a+"\t"+b+"\t\t"+c)



# 依次释放资源
##************end***********
