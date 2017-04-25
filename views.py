#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
#import MySQLdb,csv,os
from django.db import transaction,IntegrityError
from models import python_tomcat,tomcatlog
from models import Colors,Clothes,Ball,Child
from django.template import RequestContext
from django.db.models import Q
import urllib2
import json
import testapp.auth


import logging
logger = logging.getLogger('test1')

"""
django控制台会输出一部分日志
还有一部分日志是开发自定义的路径

"""


"""
django的事务管理通过@transaction.atomic实现
百度上所有的回复都是瞎扯淡
正常情况下python不会出现中文乱码现象，如果出现了说明有可能是mysql的设置问题
"""
@transaction.atomic
def insert(request):
    project_name = request.GET.get('project_name')
    module = request.GET.get('module')
    app = request.GET.get('app')
    jdk = request.GET.get('jdk')
    
    if python_tomcat.objects.filter(module=module,app=app).count() >= 1:
        print "插入的模块应用已经存在"
        logger.error("插入的模块应用已经存在")
        return HttpResponse("插入的模块应用已经存在") 
    try:
        with transaction.atomic():
            python_tomcat.objects.create(project_name=project_name,module=module,app=app,jdk=jdk)
            #i = 1/0
            tomcatlog.objects.create(module=module,app=app,action='新增',submitter='yishipeng',submitter_timer='123')
        
    except Exception,e:
        
        print e
    return HttpResponse("事务测试")
"""
以下是跨站请求伪造
loads 将已编码的 JSON 字符串解码为 Python 对象

"""
def login(request):
    return render_to_response('login.html',context_instance=RequestContext(request))
"""
logger记录日志，开发者自定义的日志
request.session.set_expiry(value)

你可以传递四种不同的值给它：

* 如果value是个整数，session会在些秒数后失效。
* 如果value是个datatime或timedelta，session就会在这个时间后失效。
* 如果value是0,用户关闭浏览器session就会失效。
* 如果value是None,session会依赖全局session失效策略。
"""
def validate(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    url_new="http://172.25.201.58/validate?username=%s&password=%s" %(username,password)
    try:
        url = urllib2.Request(url_new)
        response = urllib2.urlopen(url,timeout=10).read()
        groupid = json.loads(response)['groupid']
        if json.loads(response)['status'] == 'success':
            logger.info('%s_%s 成功登陆' %(username,password))
            request.session['username'] = username
            request.session['groupid'] = groupid
            return render_to_response('welcome.html',{'username':username},context_instance=RequestContext(request))
        else:
            logger.info('%s_%s 登陆失败' %(username,password))
            return HttpResponseRedirect('/testapp/login')
        #print response['status']
        #print response['groupid']
    except:
        return HttpResponseRedirect('/testapp/login')
    return render_to_response('welcome.html',context_instance=RequestContext(request))


"""
装饰器
"""
@testapp.auth.login_check()
def fun1(request):
    username = request.session.get('username')
    groupid = request.session.get('groupid')
    return HttpResponse("%s_%s" %(username,groupid))


    
        
"""
values是获取数据库 表的某一个字段
__contains 等价于like
filter表示模糊匹配，get表示精确匹配
"""
def fun2(request):
    result = tomcatlog.objects.filter(module__contains='hecko',app='checkout').values('action')
    for item in result:
        print item['action']
    return HttpResponse("Django mysql values去某一列的值")

"""
数据库的一对一测试
很恶心没有找到查询所有的方法
"""    
def fun3(request):
    cc = Colors.objects.get(ball__description='blue ball')
    
    return HttpResponse("Django Mysql表一对一测试")

"""
一对一映射默认映射母表的主键，如果没有指定主键则默认是id
onetoonefield
一种颜色对应一个皮球
"""   
def one_to_one(request):
    print Colors.objects.get(ball__description='红球').ball.color
    return HttpResponse("django mysql 一对一测试")

"""
一对多
foreign key
一件衣服对应多个颜色,外键
"""
def one_to_many(request):
    obj = Clothes.objects.filter(color=Colors.objects.get(colors='red'))
    print obj
    return HttpResponse("Django mysql一对多测试")

"""
多对多测试
多对多情况下数据库会多生成表的favor
manytomanyfield
"""
def many_to_many(request):
    obj = Child.objects.get(name='yi')
    print obj.favor.all()
    return HttpResponse("Django mysql多对多测试")
"""
Django mysql数据库的强制清空命令 python manage.py migrate testapp --fake
"""
"""
Q表示django数据库中的或者条件
"""
def Q_test(request):
    content = tomcatlog.objects.filter(Q(module='django')|Q(app='checkout'))
    for item in content:
        print item.id,item.module,item.app,item.action,item.submitter
    return HttpResponse("Django mysql Q数据库查询或者")
