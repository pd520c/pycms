# -*- coding: UTF-8 -*-
from sqlalchemy import *
from sqlalchemy.sql import *
#from sqlalchemy.orm import *
from sqlalchemy.databases import mysql
#连接数据库
mysql_engine = create_engine('mysql://root:@localhost:3306/cms?charset=utf8',
                             encoding = "utf-8",echo =True)
metadata = MetaData()

#管理员表,管理员id，用户名，密码，权限
admin_table = Table('admin', metadata,
Column('adminid', Integer, primary_key=True),
Column('adminname', String(20)),
Column('password', String(20)),
Column('grade', String(20)),
mysql_engine='InnoDB')
#用户表,用户id，用户名，昵称，密码，备注
user_table = Table('user', metadata,
Column('userid', Integer, primary_key=True),
Column('username', String(20)),
Column('nickname', String(20)),
Column('password', String(20)),
Column('info', String(20)),
mysql_engine='InnoDB')
#栏目表，栏目id，栏目名称，排序，栏目url
channel_table = Table('channel', metadata,
Column('channelid', Integer, primary_key=True),
Column('channelname', String(20)),
Column('sort', Integer),
Column('url', String(20)),
mysql_engine='InnoDB')
#内容表，内容id，标题，内容，作者，发布时间
content_table = Table('content', metadata,
Column('contextid', Integer, primary_key=True),
Column('title', String(20)),
Column('body', String(1000)),
Column('author', String(20)),
Column('datetime', String(20)),
mysql_engine='InnoDB')
#评论表，评论id，标题，评论内容，评论时间
comment_table = Table('comment', metadata,
Column('commentid', Integer, primary_key=True),
Column('title', String(20)),
Column('commentbody', String(100)),
Column('commentdate', String(20)),
mysql_engine='InnoDB')

#创建所有表
def install(): 
    metadata.create_all(mysql_engine)
#s='adminname'
#select = admin_table.select()
#conn = mysql_engine.connect()
#result = conn.execute(select)
#for x in result:
    #if x[1]==s:
       #print"dongt"
    #else:
       # print"dddd"



