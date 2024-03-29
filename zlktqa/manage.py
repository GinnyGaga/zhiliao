#!/usr/bin/env python
# -- coding:utf-8--

from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from exts import db
from zlktqa import app
from models import User,Question,Answer


manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()