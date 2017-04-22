#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
#import MySQLdb,csv,os
from django.db import transaction,IntegrityError
from models import python_tomcat,tomcatlog
from django.template import RequestContext
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


    
        
# def index(req):
#     return render_to_response('index.html')
# def modify(req):
#     return render_to_response('modify.html')
# def search(req):
# #     search = req.GET.get('search',None)
#     result = Server.objects.all()
#     listarray = []
#     for item in result:
#         listarray.append([item.hostname,item.nodeType,item.cabinet,item.location,item.em1IP,item.em1SwitchPort,item.memory,item.vcpu,item.disk,item.fqdn,item.sn,item.manageIP,item.em2IP,item.em2SwitchPort,item.em3IP,item.em3SwitchPort,item.em4IP,item.em4SwitchPort])
#     serverString =""
#     for item in listarray:
#         serverString += "<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th><button  id='change' style='height:30px' class='btn btn-success submit achange'>编辑</button>&nbsp<button id='del' class='btn btn-success submit con adel'>删除</button></th></tr>" %(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14],item[15],item[16],item[17])
#     print serverString    
#     return render_to_response('search.html',{'result':result})
# def restart(req):
#     item = req.GET.get('item')
#     return HttpResponse(item)
# def delete(req):
#     delete = req.GET.get('delete',None)
#     if delete != None:
#         Server.objects.filter(hostname=delete).delete()
#     return render_to_response('delete.html')
#     
# def add(req):
#     hostname=req.GET.get('hostname',None)
#     nodeType=req.GET.get('nodeType',None)
#     cabinet=req.GET.get('cabinet',None)
#     location=req.GET.get('location',None)
#     em1IP=req.GET.get('em1IP',None)
#     em1SwitchPort=req.GET.get('em1SwitchPort',None)
#     memory=req.GET.get('memory',None)
#     vcpu=req.GET.get('vcpu',None)
#     disk=req.GET.get('disk',None)
#     fqdn=req.GET.get('fqdn',None)
#     sn=req.GET.get('sn',None)
#     manageIP=req.GET.get('manageIP',None)
#     em2IP=req.GET.get('em2IP',None)
#     em2SwitchPort=req.GET.get('em2SwitchPort',None)
#     em3IP=req.GET.get('em3IP',None)
#     em3SwitchPort=req.GET.get('em3SwitchPort',None)
#     em4IP=req.GET.get('em4IP',None)
#     em4SwitchPort=req.GET.get('em4SwitchPort',None)
#     if hostname != None and nodeType != None:
#         Server.objects.create(hostname=hostname,nodeType=nodeType,cabinet=cabinet,location=location,em1IP=em1IP,em1SwitchPort=em1SwitchPort,memory=memory,vcpu=vcpu,disk=disk,fqdn=fqdn,sn=sn,manageIP=manageIP,em2IP=em2IP,em2SwitchPort=em2SwitchPort,em3IP=em3IP,em3SwitchPort=em3SwitchPort,em4IP=em4IP,em4SwitchPort=em4SwitchPort)
#     return render_to_response('add.html')
# #测试方便，路径是windows路径，/home/lihao/mysite/admin/
# def information_table(information):
#         File='D:\%s.csv' % information
#         csvfile = file('%s' % File, 'w')
#         spawriter = csv.writer(csvfile)
#         mysql_action ="select * from %s;"  % information
#         con= MySQLdb.connect(host='172.24.147.240',user='root',passwd='root',db='testapp',charset='utf8')
#         cursor =con.cursor()
#         cursor.execute(mysql_action)
#         row=cursor.fetchall()
#         if information == 'testapp_server':
#             spawriter.writerow(['主机名'.decode('utf-8').encode('gb2312'),'节点类型'.decode('utf-8').encode('gb2312'),'机柜编号'.decode('utf-8').encode('gb2312'),'位置'.decode('utf-8').encode('gb2312'),'em1','交换机端口'.decode('utf-8').encode('gb2312'),'内存G'.decode('utf-8').encode('gb2312'),'VCPU','磁盘'.decode('utf-8').encode('gb2312'),'FQDN','SN','管理IP'.decode('utf-8').encode('gb2312'),'em2','交换机端口'.decode('utf-8').encode('gb2312'),'em3','交换机端口'.decode('utf-8').encode('gb2312'),'em4','交换机端口'.decode('utf-8').encode('gb2312')])       
#         elif information == 'testapp_virtual':
#             spawriter.writerow(['虚拟机主机名'.decode('utf-8').encode('gb2312'),'应用环境'.decode('utf-8').encode('gb2312'),'IP地址'.decode('utf-8').encode('gb2312'),'物理配置'.decode('utf-8').encode('gb2312'),'宿主机'.decode('utf-8').encode('gb2312'),'宿主机IP'.decode('utf-8').encode('gb2312'),'cephfs','备注'.decode('utf-8').encode('gb2312')])
#         elif information == 'testapp_beta_virtual':
#             spawriter.writerow(['宿主机'.decode('utf-8').encode('gb2312'),'宿主机IP'.decode('utf-8').encode('gb2312'),'虚拟机主机名'.decode('utf-8').encode('gb2312'),'应用环境'.decode('utf-8').encode('gb2312'),'IP地址'.decode('utf-8').encode('gb2312'),'物理配置'.decode('utf-8').encode('gb2312'),'cephfs','备注'.decode('utf-8').encode('gb2312')])
#         elif information == 'testapp_logstach':
#             spawriter.writerow(['宿主机'.decode('utf-8').encode('gb2312'),'宿主机IP'.decode('utf-8').encode('gb2312'),'虚拟机主机名'.decode('utf-8').encode('gb2312'),'应用环境'.decode('utf-8').encode('gb2312'),'IP地址'.decode('utf-8').encode('gb2312'),'物理配置'.decode('utf-8').encode('gb2312'),'isci','cephfs','备注'.decode('utf-8').encode('gb2312')])
#         elif information == 'testapp_apache':
#             spawriter.writerow(['宿主机'.decode('utf-8').encode('gb2312'),'宿主机IP'.decode('utf-8').encode('gb2312'),'虚拟机主机名'.decode('utf-8').encode('gb2312'),'应用环境'.decode('utf-8').encode('gb2312'),'IP地址'.decode('utf-8').encode('gb2312'),'物理配置'.decode('utf-8').encode('gb2312'),'cephfs','备注'.decode('utf-8').encode('gb2312')])
#         data=[]
#         for i in row:
#                 data.append(i)
#         spawriter.writerows(data)
#         csvfile.close()
#         con.close()
#         
# #需要js触发svn函数        
# def svn(req):
#         print "Hello"
#         os.system("svn ci /home/lihao/mysite/admin/server.csv")
#         return render_to_response('index.html')
