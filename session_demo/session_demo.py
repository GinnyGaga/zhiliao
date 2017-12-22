#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask,session
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)#只有一条设置可以这样写

#添加数据到session中
#操作session和操作字典是一样的
#设置SECRET_KEY


@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    return 'Hello World!'


@app.route('/get/')
def get():
    # session['username']
    # session.get('username')

    print (session.get('username'))
    return 'secessdd'


@app.route('/delete/')
def delete():
    print (session.get('username'))
    session.pop('username')
    print (session.get('username'))
    return 'success'


@app.route('/clear/')
def clear():
    print (session.get('username'))
    session.clear()
    print (session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)