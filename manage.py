from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import User, Writer, Post, Comment, Subscription

#Creating app instance
app = create_app('development')

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Writer = Writer, Post = Post, Comment = Comment, Subscription = Subscription )


if __name__ == '__main__':
    manager.run()