#!/usr/bin/env python
# -- coding:utf-8--

from exts import db

class Article(db.Model):
    __table__name = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    context = db.Column(db.Text,nullable=False)
    tags = db.Column(db.String(100),nullable=True)