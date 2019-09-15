# Time: 2019/9/9  19:01
# Author jzh
# File tasks.py

from main import celery_app


@celery_app.task(bind=True, name='send-email', retry_backoff=3)
def send_email(self, subject, recipients, msg, copy=None):
    """
     将包导在上方为啥会影响celery发现task???
    :param self:  指定bind后需要加上
    :param subject: 主题
    :param recipients: 收件人
    :param msg: 正文
    :param copy: 抄送
    :return:
    """
    from flask_mail import Message
    from flask import current_app

    sender = current_app.config['MAIL_SENDER']
    message = Message(subject=subject, recipients=recipients, sender=sender, html=msg, cc=copy)
    try:
        # 发送邮件
        current_app.mail.send(message)
    except Exception as e:
        # 出错后继续尝试发送三次
        raise self.retry(exc=e, max_retries=3)
