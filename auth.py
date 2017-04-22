#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
def login_check():
        
        def decorator(func):
                def login_auth_check(req):
                        
                        if req.method=='GET':
                                try:
                                        if req.session['username']:
                                                return func(req)
                                        else:
                                            print "未登陆"
                                except:
                                        req.session.clear_expired()
                                        return HttpResponseRedirect('/testapp/login')
                        else:
                                return HttpResponseRedirect('/testapp/login')


                return login_auth_check
        return decorator