from app.extenions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    userAvatar = db.Column(db.String(100))
    selfIntroduction = db.Column(db.String(250))
    userLogs = db.relationship('UserLog', backref='user')
    blogs = db.relationship('Blog', backref='user')

    def __repr__(self):
        return "<User %r>" % self.username


class UserLog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    userId = db.Column(db.ForeignKey('user.id'))
    addTime = db.Column(db.DateTime, default=datetime.now())\

    def __repr__(self):
        return "<UserLog> %r" % self.id


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)
    sendTime = db.Column(db.DateTime, default=datetime.now())
    modifyTime = db.Column(db.DateTime)
    userId = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Blog %r>" % self.title


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    sendTime = db.Column(db.DateTime, default=datetime.now())
    sendUser = db.Column(db.ForeignKey('user.id'))
    commentBlog = db.Column(db.ForeignKey('blog.id'))

    def __repr__(self):
        return "<Comment %r>" % self.id


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    adminName = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    logs = db.relationship('AdminLog', backref='admin')

    def __repr__(self):
        return "<Admin %r>" % self.adminName


class AdminLog(db.Model):
    __table__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    addTime = db.Column(db.DateTime, default=datetime.now())
    adminId = db.Column(db.ForeignKey('admin.id'))

    def __repr__(self):
        return "<AdminLog %r>" % self.id


