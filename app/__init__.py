from flask import Flask

# Config Values
UPLOAD_FOLDER = './app/static/uploads'


USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

ALLOWED_EXTS =set(['png','jpg'])

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)
app.config.from_object(__name__)
from app import views
