from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):

    name = StringField(
        label="Name",
        name="name",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ]
    )
    username = StringField(
        label="username",
        name="username",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ]
    )
    email = StringField(
        label="email",
        name="email",
        validators=[
            DataRequired(),
            Length(min=3, max=200),
        ]
    )
    is_new = BooleanField(
        label="Is new user",
        name="is-new",
        default=False,
    )