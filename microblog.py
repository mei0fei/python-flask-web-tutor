from app import app, db
from app.models import User, Post
from flask_babel import lazy_gettext as _l

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
