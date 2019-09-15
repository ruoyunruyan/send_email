# Time: 2019/9/9  16:58
# Author jzh
# File forms.py

from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MailForm(FlaskForm):
    recipients = StringField('收件人', validators=[DataRequired(message='收件人不能为空')], description='多个邮箱之间用英文分号隔开, 不可以为空')
    copy = StringField('抄送', description='多个邮箱之间用英文分号隔开, 可以为空')
    subject = StringField('主题', validators=[DataRequired(message='主题不能为空')])
    msg = CKEditorField('内容', validators=[DataRequired(message='内容不能为空')])
    submit = SubmitField('发送')
