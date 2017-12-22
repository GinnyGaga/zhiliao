#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask,render_template,request,session,redirect,url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    print ('index')
    return 'index'


@app.route('/login/',methods = ['GET','POST'])
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111':
            session['username'] = 'zhiliao'
            return '登入成功'
        else:
            return '用户名或密码错误'


@app.route('/edit/')
def edit():
    if session.get('username'):
        return '修改成功'
    else:
        return redirect(url_for('login'))


@app.before_request
def my_before_request():

    print ("hello world")


if __name__ == '__main__':
    app.run(debug=True)