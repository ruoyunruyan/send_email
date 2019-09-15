# Time: 2019/9/9  16:51
# Author jzh
# File app_factory.py

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_ckeditor import CKEditor
from celery import Celery


def create_app(config, enable_config_env=False):
    """app工厂"""
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config)
    if enable_config_env:
        from common.utils import constants
        app.config.from_envvar(constants.GLOBAL_SETTING_ENV_MAIL_USERNAME, silent=True)
        app.config.from_envvar(constants.GLOBAL_SETTING_ENV_MAIL_PASSWORD, silent=True)
        app.config.from_envvar(constants.GLOBAL_SETTING_ENV_MAIL_SENDER, silent=True)

    # 初始化邮箱扩展
    mail = Mail()
    mail.init_app(app)

    app.mail = mail

    # 初始化bootstrap扩展
    bootstrap = Bootstrap()
    bootstrap.init_app(app)

    # 初始化ckeditor
    ckeditor = CKEditor()
    ckeditor.init_app(app)

    return app


def make_celery(app):
    """创建celery, 将任务执行包装在应用程序上下文中"""
    c = Celery(app.import_name)

    c.config_from_object('celery_tasks.config')

    c.conf.update(app.config)

    c.autodiscover_tasks(['celery_tasks.email_task'])

    class ContextTask(c.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    c.Task = ContextTask
    return c
