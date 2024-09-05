from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class VideosLinkFormat(FlaskForm):
    video_link = StringField('Video Link', validators=[DataRequired()])
    submit = SubmitField('Submit')
