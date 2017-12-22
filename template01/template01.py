#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask ,render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = 'ginny'
        age = '18'
    p = Person()

    context = {
        'username':'知了课堂',
        'gender':'male',
        'age': 18,
        'Person':p,
        'websites': {
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }

        }
    return render_template('anthor/index.html',**context)


if __name__ == '__main__':
    app.run(debug=True)