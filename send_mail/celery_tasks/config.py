# Time: 2019/9/9  18:55
# Author jzh
# File config.py

from kombu import Exchange, Queue

# 使用rabbitmq作为 broker
BROKER_URL = 'amqp://guest:guest@127.0.0.1:5672/'

# 使用redis作为 backend
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# 指定时区
CELERY_TIMEZONE = 'Asia/Shanghai'

# 由于rabbitmq三分钟没有接收到任务, 会断开连接
# 每隔30s, RabbitMQ(server端)向生产者API(client端)发送心跳包，共发了5次
# 过了3分钟, RabbitMQ(server端)关闭连接，生产者API(client端)也关闭连接
# http://www.bubuko.com/infodetail-2942886.html
BROKER_HEARTBEAT = None

CELERY_QUEUES = (
    Queue(name='default', exchange=Exchange('default'), routing_key='default'),
    Queue(name='send_email', exchange=Exchange('send_email'), routing_key='send_email')
)

CELERY_ROUTES = {
    'celery_tasks.email_task.tasks.send_email': {'queue': 'send_email', 'routing_key': 'send_email'}
}

"""

CELERY_IMPORTS = (
    'celery_tasks.email_task'
)

# 定义任务队列
CELERY_QUEUES = (
    Queue("default", Exchange("default"), routing_key="default"),
    Queue("for_task_realtime", Exchange("for_task_realtime"), routing_key="task_realtime"),
    Queue("for_task_timer", Exchange("for_task_timer"), routing_key="task_timer"),
    Queue("for_task_monitor", Exchange("for_task_monitor"), routing_key="task_monitor")
)

# 定义routes用来决定不同的任务去哪一个queue
CELERY_ROUTES = {
    # tasks.taskrealtime的消息会进入for_task_realtime队列
    'tasks.taskrealtime': {"queue": "for_task_realtime", "routing_key": "task_realtime"},
    # tasks.tasktimer的消息会进入for_task_timer队列
    'tasks.tasktimer': {"queue": "for_task_timer", "routing_key": "task_timer"},
    # tasks.taskmonitor的消息会进入for_task_monitor队列
    'tasks.taskmonitor': {"queue": "for_task_monitor", "routing_key": "task_monitor"},
}

# 定时任务
CELERYBEAT_SCHEDULE = {
    # 任务名称
    'every-30-seconds': {
        # task就是需要执行计划任务的函数
         'task': 'handlers.schedules.every_30_seconds',
         # 配置计划任务的执行时间，这里是每30秒执行一次
         'schedule': timedelta(seconds=30),
         # 传入给计划任务函数的参数
         'args': {'value': '2333333'}
    },

    'push_occupancy_rates': {
        'task': 'handlers.schedules.test_func_b',
        # 每天中午12点执行
        'schedule': crontab(hour='12', minute='0'),
        'args': None
    }
}
"""
