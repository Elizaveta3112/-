from flask import Flask, render_template

server = Flask(__name__)

messages = [
{'username':'lizabal','text':'Пиривт'},
{'username':'liza','text':'Здравствуйте!'},
{'username':'elizavea','text':'Добрый вечер'},
]


@server.route('/')
def hello():
return '''Hello, World!


<a target="_blank" href=/index>Index</a>'''
@server.route('/get_messages')
def get_messages():
return{
'messages': messages
}

@server.route('/index')
def index():
name = 'Лиза'
return render_template("index.html")

@server.route('/day-<num>')
def day(num):
return render_template(f"day-{num}.html")
