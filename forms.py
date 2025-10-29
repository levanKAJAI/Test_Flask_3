from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class FeedbackForm(FlaskForm):
    name = StringField("სახელი", validators=[DataRequired(message="შეიყვანეთ სახელი")])
    email = StringField("ელფოსტა", validators=[
        DataRequired(message="აუცილებელია ელფოსტა"),
        Email(message="არასწორი ელფოსტის ფორმატი")
    ])
    message = TextAreaField("შეფასება", validators=[
        DataRequired(message="აუცილებელია შეფასება"),
        Length(min=20, message="შეფასება უნდა იყოს მინიმუმ 20 სიმბოლო")
    ])
    feedback_type = SelectField("შეფასების ტიპი", choices=[
        ("Positive", "პოზიტური"),
        ("Neutral", "ნეიტრალური"),
        ("Negative", "უარყოფითი")
    ])
    submit = SubmitField("გაგზავნა")
