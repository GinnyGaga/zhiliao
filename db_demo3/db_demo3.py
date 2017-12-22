#!/usr/bin/env python
# -- coding:utf-8--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)



class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref=db.backref('articles'))

db.create_all()


@app.route('/')
def index():
    # #想要添加一篇文章，首先先添加一个用户
    # user1=User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()
    # return 'index'
    # 添加文章
    # article1=Article(title='111',content='222',author_id=1)
    # db.session.add(article1)
    # db.session.commit()
    # return 'index'
    # 想要找文章标题为111的作者，先找到篇文章,方法1如下，未添加关联表之前：
    # article = Article.query.filter(Article.title == '111').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print ("username: %s" % user.username)
    #方法2，删掉article表，添加关联后，重新添加一篇文章，然后再找这篇文章的作者：
    # article = Article(title='aaa', content='bbb', author_id=1)
    # db.session.add(article)
    # db.session.commit()
    # article.author
    # print ("username: %s" % article.author.username)
    #找到zhiliao用户写过的所有文章：
    # article = Article(title='ccc', content='zzz', author_id=1)
    # db.session.add(article)
    # db.session.commit()
    user = User.query.filter(User.username == 'zhiliao').first()
    result = user.articles
    for article in result:
        print ('_'*10)
        print(article.title)

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)