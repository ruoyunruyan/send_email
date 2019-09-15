# Time: 2019/9/9  14:22
# Author jzh
# File main.py

from flask import render_template

from send_mail.app_factory import create_app, make_celery
from send_mail.forms import MailForm
from common.settings.default import DefaultConfig

app = create_app(DefaultConfig, enable_config_env=True)
celery_app = make_celery(app)

from celery_tasks.email_task.tasks import send_email


@app.route('/', methods=['get', 'post'])
def index():
    form = MailForm()
    if form.validate_on_submit():
        recipients = form.recipients.data.split(';')
        copy = form.copy.data
        if copy:
            copy = copy.split(';')
        subject = form.subject.data
        msg = form.msg.data
        send_email.apply_async(args=(subject, recipients, msg, copy), queue='send_email', routing_key='send_email')
    return render_template('index.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
