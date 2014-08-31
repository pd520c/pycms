import web
#import sys
import os
from jinja2 import *
from jinja2 import Environment,FileSystemLoader
from web.contrib.template import render_jinja
from model import *


urls = (  
    '/', 'Index',
    '/Sign', 'Sign',
    '/Admin', 'Admin'
    
)
app = web.application(urls, globals())
db = web.database(dbn='mysql',db='cms',user='root',pw='')
session = web.session.Session(app, web.session.DBStore(db,'sessions'), initializer={'login': 0,})
# set jinja2 
def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    #jinja_env.update_template_context(context)
    return jinja_env.get_template(template_name).render(context)

class Index:
    def GET(self):
        return "Hello, sun!"

class Sign:  
    def GET(self):  
        return  render_template('Sign.html', encoding='utf-8',title = 'sign')
    def POST(self):
        name = web.input().name
        passwd =web.input().password
        nick =web.input().nickname
        conn = mysql_engine.connect()
        stm = select([user_table]).where((user_table.c.username == name)|(user_table.c.nickname == nick))
        i = conn.execute(stm).fetchall()
        conn.close()
        if len(i)==0 :
            mysql_engine.connect().execute(user_table.insert(), username = name, nickname = nick, password = passwd)
            mysql_engine.connect().close()
            return "resign successed"
        else:
            return "Don't resign"
def logged():
        if session.login==1:
            return True
        else:
            return False

class Admin:
    def GET(self):
        if logged():
            return render_template('Admin.html', encoding='utf-8',title = 'sign')
        else:
            return render_template('Login.html', encoding='utf-8',title = 'sign')
    
    def POST(self):
        name = web.input().name
        passwd =web.input().password
        conn = mysql_engine.connect()
        stm = select([admin_table]).where((admin_table.c.adminname == name)&(admin_table.c.password == passwd))
        i = conn.execute(stm).fetchall()
        conn.close()
        if len(i)>0:
            session.login = 1
            print"you are admin"
        else:
            session.login = 0
            return "error"
                
        
if __name__ == "__main__":
    app.run()     

