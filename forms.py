from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('Username',[validators.DataRequired(),validators.Length(min=4,max=25)])
    password = PasswordField('Password',[validators.DataRequired(),validators.Length(min=6,max=35)])

class RegistrationForm(Form):
    username = StringField('Username',[validators.DataRequired(),validators.Length(min=4,max=25)])
    email = StringField('Email Address',[validators.DataRequired(),validators.Length(min=6,max=35)])
    password = PasswordField('New Password',[validators.DataRequired(),validators.EqualTo('confirm',message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
