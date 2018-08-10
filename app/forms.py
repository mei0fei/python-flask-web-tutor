from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User
from flask_babel import lazy_gettext as _l
from flask_babel import _


class LoginForm(FlaskForm):
    username = StringField(_l('用户名称'), validators=[DataRequired()])
    password = PasswordField(_l('密码'), validators=[DataRequired()])
    remember_me = BooleanField(_l('记住我'))
    submit = SubmitField(_l('登录'))

class RegisterationForm(FlaskForm):
    username = StringField(_l('用户名称'), validators=[DataRequired()])
    email = StringField(_l('邮箱'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('密码'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('重复密码'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('注册'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('该用户名称已经注册过！'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('该邮箱已经注册过.'))

class EditProfileForm(FlaskForm):
    username = StringField(_l('用户名称'), validators=[DataRequired()])
    about_me = TextAreaField(_l('关于我'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('提交'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l('名称已经存在。'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('发帖'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('提交'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('邮箱'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('重置密码'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('密码'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('再次确认密码'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('重置密码'))