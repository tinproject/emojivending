from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import AnyOf

from .emoji import categories


class GetEmojiForm(FlaskForm):
    category = StringField(label="category", validators=[AnyOf(list(categories.keys()))])


class SendFeedbackForm(FlaskForm):
    feedback = StringField(label="feedback", validators=[AnyOf(["yes", "no"])])
