#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask
from exts import db
import config
from models import Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app) #绑定app,初始化app


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)