from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import User, Writer, Post, Comment, Subscription
from flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = create_app('development')
# app = create_app('production')

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Writer = Writer, Post = Post, Comment = Comment, Subscription = Subscription )


if __name__ == '__main__':
    manager.run()