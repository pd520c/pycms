import web
import os
from jinja2 import *
from jinja2 import Environment,FileSystemLoader
from web.contrib.template import render_jinja
from model import *


urls = (  
    '/', 'Index',
    '/Sign', 'Sign'
)  

def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
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
        #return render.first('world','name')
        #f = Sign() 
        return  render_template('Sign.html', encoding='utf-8',title = 'sign')
    def POST(self):
        i = web.input()
        insert = admin_table.insert()
        conn = mysql_engine.connect()
        stm = select([admin_table.c.adminname]).where(admin_table.c.adminname == i.name)
        i = conn.execute(stm).fetchall()
        if len(i)>0 :
            return "Sorry Don't resign"
        else:
            conn.execute(insert, adminname = i.name, password = i.password)
            return "resign successed"

if __name__ == "__main__":  
    app = web.application(urls, globals())  
    app.run()     

