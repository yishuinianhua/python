#coding=utf-8
#from urllib2 import urlopen

# import redis
#
# r = redis.Redis(host="172.25.201.58",port=6379,passwd="redis")
# r.get("java")
#print urlopen("http://www.baidu.com",timeout=10).read()
'''
设置超时的时间是10秒 timeout=10
'''
'''
不要简单的import urlopen,否则许多无法使用
'''
import urllib2,urllib

'''
运行结果是完全一样的，只不过中间多了一个request对象，推荐大家这么写，
因为在构建请求时还需要加入好多内容，通过构建一个request，服务器响应请求得到应答，这样显得逻辑上清晰明确。
'''

'''
URLError:网络无连接，即本机无法上网/连接不到特定的服务器/服务器不存在
[Errno 11004] getaddrinfo failed
们知道，HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常，所以上述的代码可以这么改写
'''
#request = urllib2.Request('http://blog.csdn.net/cqcre')
request = urllib2.Request('http://blognimeide.csdn.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    if hasattr(e,"code"):
        print e.code
        print e.reason
except urllib2.URLError,e:
    if hasattr(e,"reason"):
        print e.reason
'''
POST方式
如果有data直接转变为post方式
'''
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
value = {"username":"kaifa","password":"kaifa"}
headers = {"User-Agent":user_agent}
data = urllib.urlencode(value)
print data
url = "http://172.25.201.58/validate"
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request,timeout=3)
print response.read()
response.close()

'''
GET方式
geturl直接拼接参数
urlopen方法了，第三个参数就是timeout的设置，可以设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响
'''
value={}

value["username"] = "devmanager"
value["password"] = "devmanager"

data = urllib.urlencode(value)
url = "http://172.25.201.58/validate"
geturl = url + "?" + data
print geturl
request = urllib2.Request(geturl)
response = urllib2.urlopen(request,timeout=3)
print response.read()

'''
Proxy（代理）的设置

urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，
如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了，这酸爽！

'''

"""标准格式的requests post/get方式请求"""
def get_mail_token(company):
    # 每隔2小时调用tencent接口获取token，保存到redis数据库中
    # 获取腾讯企业邮箱token,获取token需要管理员账号,秘钥,授权方式
    data = dict()
    if company == 'zhongan':
        data = {
            "client_id": app.config['CLIENT_ID_ZHONGAN'],
            "client_secret": app.config['CLIENT_SECRET_ZHONGAN'],
            "grant_type": "client_credentials"
        }
        elif company == 'zatech':
            data = {
                "client_id": app.config['CLIENT_ID_ZATECH'],
                "client_secret": app.config['CLIENT_SECRET_ZATECH'],
                "grant_type": "client_credentials"
            }
            url = app.config['MAIL_API_HOST']+'/gettoken'
            try:
                response = requests.post(url, data, timeout=20)
                out_logger.info(response.content)
                mail_token = response.json().get("access_token")
                out_logger.info("got token: " + str(mail_token))
                return mail_token
            except Exception, e:
                out_logger.exception("get tokens fail %s", e)
                return False
            





