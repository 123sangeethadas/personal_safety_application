import pymysql
def iud(q,v):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="personal_safety")
    cmd=con.cursor()
    cmd.execute(q,v)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id


def selectone(q,v):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="personal_safety")
    cmd=con.cursor()
    cmd.execute(q,v)
    res=cmd.fetchone()
    return res

def select1(q,val):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="personal_safety")
    cmd=con.cursor()
    cmd.execute(q,val)
    res=cmd.fetchone()
    return res

def selectall(q,v):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="personal_safety")
    cmd=con.cursor()
    cmd.execute(q,v)
    res=cmd.fetchall()
    return res

def select(q):
    con=pymysql.connect(host="localhost",user="root",password="",port=3306,db="personal_safety")
    cmd=con.cursor()
    cmd.execute(q)
    res=cmd.fetchall()
    return res

def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='personal_safety')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='personal_safety')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
