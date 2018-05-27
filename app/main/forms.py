from flask_wtf import FlaskForm
from wtfforms import StringField,TextAreaField,RadioField,SubmitField,SelectField,ValidationError
from wtfforms.validators import Required

#Post Form
class PostForm(FlaskForm):
    title_id = SelectField('Posts')
    body = TextAreaField()
    submit = SubmitField('Submit Post')

#Comment Form
class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()

#Subscription Form
class SubscriptionForm(FlaskForm):
    email = TextAreaField('Email')
    submit = SubmitField()