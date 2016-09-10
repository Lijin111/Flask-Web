import os
from app import create_app, db
from app.models import User, Role,Permission,Post,Follow,Comment
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Follow=Follow,
                Permission=Permission, Post=Post, Comment=Comment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

'''
python manage.py shell
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgraed
python manage.py runserver --host 0.0.0.0
'''

if __name__ == '__main__':
    manager.run()
