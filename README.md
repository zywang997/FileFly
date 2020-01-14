# FileFly
北京大学《互联网软件开发技术与实践》课程期末大作业


## 简介
使用 Python 的 Flask 框架开发的一个校园分享云盘系统，存储使用了 Hadoop 分布式文件系统，数据库使用到了 ORM 框架 SQLAlchemy。 


参考项目：https://github.com/seeicb/Flask-Disk


主要特性：

    文件操作：上传、下载、重命名、密钥分享、无密钥共享、取消分享、删除、恢复、彻底删除
    
    用户操作：注册、登陆、编辑资料、修改密码
    
    管理员操作：查看所有用户个人信息，锁定/解锁用户账号，修改用户账号密码
    
    邀请码注册：每个用户初始分配一个随机邀请码，用于邀请其他用户注册，有3次有效使用机会
    
    用户积分制：上传文件增加用户积分，无密钥共享的文件被下载也会增加用户积分（积分用途待后续开发）
    
    文件基本分类：根据扩展名进行判别，展示时可按文件名、修改日期、大小、下载次数排序
    
    热门分享：可以看到所有用户无密钥共享的内容，实现真正意义上的共享（未共享资源属于个人资源，他人不可见）


## 安装使用
### Hadoop安装配置
首先需要安装 Hadoop 环境，参考http://www.powerxing.com/install-hadoop/  

启用 Hadoop 回收站，修改 conf/core-site.xml 和 hdfs-site.xml

真分布式 hdfs 的搭建要注意：

    1. 主机名的修改，要与 hdfs 中节点 hosts 文件的名字相同
    
    2. namenode 的 webhdfs 端口从 50070 转成 9870 
    
    3. core-site 中使用 ip 地址而不是 0.0.0.0，并在 hdfs-site.xml 中添加与 namenode 的 rpc 通信的配置项目
    
    4. 注意端口的安全组和防火墙设置



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
# 最大上传限制，默认128M
MAX_CONTENT_LENGTH = 1024 * 1024 * 128
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

默认用户名admin，密码 I won't tell you（管理员账户）
