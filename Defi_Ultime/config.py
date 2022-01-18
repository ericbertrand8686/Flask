import os
SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    FB_APP_ID = 3018046051780686
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    FB_APP_ID = 3018046051780686
    #FB_APP_ID = 1967148823570310