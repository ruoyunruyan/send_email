### 启动命令
```python
系统: win7
celery -A main:celery_app worker -l info -P eventlet
```
需要依赖`eventlet`模块, 不然会报错

使用`rabbitmq`做为`broker`
使用`redis`做为`backend`
`MAIL_USERNAME`、`MAIL_PASSWORD`和`MAIL_SENDER`定义在环境变量中
