from bs4 import BeautifulSoup
import pymysql
import time, datetime


#增加信息
def add(number,name,id_card,birthday,address,phone,department,money,work_time,professon,zhiwu,remark):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    t = (number, name, id_card,birthday,address, phone,department,money,work_time,professon,zhiwu,remark)
    sql = "INSERT INTO teacher(number,name,id_card,birthday,address,phone,department,money,work_time,professon,zhiwu,remark) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % t
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
def update(number,name,id_card,birthday,address,phone,department,money,work_time,professon,zhiwu,remark):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    t = ( name, id_card,birthday,address, phone,department,money,work_time,professon,zhiwu,remark,number)
    sql = "update teacher set name = '%s', id_card='%s',birthday='%s', address='%s',phone='%s',department='%s',money='%s',work_time='%s',professon='%s',zhiwu='%s',remark='%s' where number = '%s'" % t
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
def delete(number):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    t = (number)
    sql = "delete from teacher where number='%s'" % t
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()
def loadAll():
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from teacher"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        results=conn.fetchall()
        return results
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()

#根据教师编号查询
def loadNumber(number):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from teacher where number='"+number+"'"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        result=conn.fetchall()
        return result
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()

#根据教师姓名查询
def loadName(name):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from teacher where name='"+name+"'"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        results=conn.fetchall()
        return results
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()

#根据出生年月范围查询
def loadBirthday(date1,date2):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from teacher where birthday>='"+date1+"' and birthday<='"+date2+"'"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        results=conn.fetchall()
        return results
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()
#根据工资范围查询
def loadMoney(money1,money2):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from teacher where money>='"+money1+"' and money<='"+money2+"'"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        results=conn.fetchall()
        return results
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()

#根据参见工作时间范围查询
def loadWork_time(date1,date2):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', passwd='root', db='information_teacher', port=3306,
                         charset='utf8')
    conn = db.cursor()  # 获取指针以操作数据库
    conn.execute('set names utf8')
    sql = "select * from teacher where work_time>='"+date1+"' and work_time<='"+date2+"'"#查询所有信息
    print(sql)
    try:
        conn.execute(sql)
        # 执行sql语句
        results=conn.fetchall()
        return results
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
        return
    # 关闭数据库连接
    db.close()
results=loadAll()
for item in results:
    for i in range(len(item)):
        print(item[i]),
    print('/n')