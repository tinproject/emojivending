from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import AnyOf


category = {
    "o1": "😀",
    "o2": "☹",
    "o3": "😈",
    "o4": "😺",
    "o5": "🐵",
    "o6": "🏴",
}


class GetEmojiForm(FlaskForm):
    category = StringField(label="category", validators=[AnyOf(list(category.keys()))])


class SendFeedbackForm(FlaskForm):
    feedback = StringField(label="feedback", validators=[AnyOf(["yes", "no"])])
