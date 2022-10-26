from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.news.models import User

app = create_app()

with app.app_context():
    username = input('Write the name')

    if User.query.filter(User.username == username).count():
        print('User with this name are done yet')
        sys.exit(0)
    
    password1 = getpass('Write the password')
    password2 = getpass('Repeate the password')
    if not password1 == password2:
        print('password is not correct')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))