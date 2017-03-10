#!/usr/bin/env python
# encoding: utf-8
# Author: FlyWen
import re
import MySQLdb
import os

def run(filename):
    f = open("./%s/%s"%(column_id,filename),'r')
    title = re.search(".*<title>(.*)</title>.*",f.read())
    content_title = title.group(1)
    #content_title = content_title.decode('utf-8')
    print content_title
    f.close()
    f = open("./%s/%s"%(column_id,filename),'r')
    content = re.search('.*den;">([\s\S]*)</div.*',f.read())
    content_detail = content.group(1)
    print content_detail
    f.close()

    cur = conn.cursor()
    sqli_1 = "insert into T_CONTENT values(%s,%s,'',null,'','','2017-01-01',null,null,null,null,null,%s)"
    cur.execute(sqli_1,(content_id,content_title,'1'))
    sqli_2 = "insert into T_CONTENT_DETAIL values(%s,%s)"
    cur.execute(sqli_2,(content_id,content_detail))
    sqli_3 = "insert into T_COLUMN_CONTENT values(%s,%s,%s)"
    cur.execute(sqli_3,(content_id,column_id,content_id))
    cur.close()
    conn.commit()

    html_file = open("./%s/%s.html"%(column_id,content_id),'w')
    html_file.write(content.group(1))
    html_file.close()

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host = '192.168.1.199',
        port = 3306,
        charset = 'utf8',
        user = 'root',
        passwd = 'Server_2017',
        db = 'cms_web_test',
    )
    #cur = conn.cursor()
    #sqli = "insert into aaa values(%s,%s,%s,%s)"
    #cur.execute(sqli,('1','2','3','4'))
    #cur.close()
    #conn.commit()
    content_id = 1001
    column_id = 37
    for i in os.walk('./%s/'%column_id):
        for j in i[2]:
            print j
            run(j)
            content_id = content_id+1
    #run("aaa")
    conn.close()
