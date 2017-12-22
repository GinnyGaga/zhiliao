#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    comments = [
        {
        'user':'知了课堂',
        'comment':'xxx'
    },
    {
        'user':'ginny',
        'comment':'xxx'
    }
    ]
    return render_template('index.html',comments=comments)


if __name__ == '__main__':
    app.run(debug=True)