#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

#创建数据库：
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

db.create_all()


@app.route('/')
def hello_world():
    #增加：
    article1 = Article(title='aaa',content='bbb')
    db.session.add(article1)
    db.session.commit()
    return 'hello world'
    #
    # #查：
    # #select * from article where article.title='aaa';
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # print ("article title: %s " % article1.title)
    # print ("article content: %s " % article1.content)

    # #改：
    # #1、查找要更改的数据；
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # #2、修改这条数据；
    # #article1.title = 'new title'
    # #3、做事务的提交
    # #db.session.commit()
    #删：
    # #1、查找要删除的数据；
    # article1 = Article.query.filter(Article.content == 'bbb').first()
    # #2、删除这条数据；
    # db.session.delete(article1)
    # #事务的提交：
    # db.session.commit()
    # return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)