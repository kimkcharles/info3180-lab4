from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!') ])
    