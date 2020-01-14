# FileFly
Web assignment


## 简介
使用python的Flask框架开发的一个校园分享云盘系统，存储使用了Hadoop分布式文件系统，数据库使用到了ORM框架SQLAlchemy。  

功能：  
    用户管理：注册、登录、资料编辑和修改密码。使用邀请码机制来管控新用户注册，防止上传文件的内容违规。
    文件管理：文件上传下载、文件公开分享和密码分享、删除文件、恢复文件和重命名文件  
    管理员后台：查看用户个人信息、锁定普通用户、修改用户密码  
    公共分享文件论坛：可以看到最新最热的公共分享资源

## 安装使用
### Hadoop安装配置
首先需要安装Hadoop环境，参考http://www.powerxing.com/install-hadoop/  
启用Hadoop回收站，修改conf/core-site.xml和hdfs-site.xml

真分布式hdfs的搭建主要注意
    1. 主机名的修改，要与hdfs中节点hosts文件的名字相同
    2. namenode的webhdfs端口从50070转成9870
    3. core-site中使用ip地址而不是0.0.0.0，并在hdfs-site.xml中添加与namenode的rpc通信的配置项目



### 依赖安装

```
pip3 install virtualenv
virtualenv --no-site-packages venv
source venv/bin/activate
git clone https://github.com/MaxwellSigmoid/FileFly
pip install -r requirements.txt
```

### 修改配置
配置文件config.py，其中

```
# 最大上传限制，默认1024M
MAX_CONTENT_LENGTH = 1024 * 1024 * 1024
# Cookie 过期时间
REMEMBER_COOKIE_DURATION = timedelta(days=7)
# HDFS回收站文件路径
HDFS_TRASH = '/user/username/.Trash/Current/'
# HDFS namenode
hdfs的主节点ip，9870是webhdfs入口
HDFS_IP = "http://114.116.5.3:9870"
# 网站地址，是flask后端运行的域名
BASE_HOST='http://114.115.167.187:8082/'
```



### 数据库配置
```
python manage.py db init
python manage.py db migrate -m "init"
python manage.py db upgrade
python manage.py deploy
```

## 启动
`python manage.py runserver`

打开：http://114.115.167.187:8082/

默认用户名admin，密码 password（管理员账户）