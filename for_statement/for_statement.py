#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask,render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     # user = {
#     #     'username': 'ginny',
#     #     'age': '18'
#     # }
#     #
#     # websites = ['baidu.com','google.com']
#     #
#     # return render_template('index.html',user=user,websites=websites)

# index.html:
# < !--{ %
# for k, v in user.items() %}-->
# < !-- < p > {{k}}: {{v}} < / p > -->
# < !--{ % endfor %}-->
#
# < !--{ %
# for website in websites %}-->
# < !-- < p > {{website}} < / p > -->
# < !--{ % endfor %}-->



@app.route('/')
def index():
    books = [
        {
            'name':'西游记',
            'author':'吴承恩',
            'price': 109
        },
        {
            'name':'红楼梦',
            'author':'曹雪芹',
            'price':200
        },
        {
            'name':'三国演义',
            'author':'罗贯中',
            'price':120
        },
        {
            'name':'水浒传',
            'author':'施耐庵',
            'price':130
        }

    ]
    return render_template('index.html',books=books)


if __name__ == '__main__':
    app.run(debug=True)