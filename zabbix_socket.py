#!/usr/bin/python
#coding=utf-8
import socket,commands,re,os,datetime

d1 = datetime.datetime.now()
NOW_DATE = d1.strftime('%Y-%m-%d %H:%M:%S')



def restart_port(TIME,IP,NAME,HOST):

    try:
        if re.search(r'离线:'.decode('utf-8').encode('utf-8'),NAME).group():
            JBOSS = re.search(r'离线:(.*) .*%'.decode('utf-8').encode('utf-8'),NAME).group(1)
            JBOSSITEM = re.search(r'^(.*):离线:(.*) .*%'.decode('utf-8').encode('utf-8'),NAME).group(1)
            JBOSSIP = JBOSS.replace(',','')
            JBOSSIP = []
            for ip in range(len(JBOSS.split(','))):
                 JBOSSIP.append(JBOSS.split(',')[ip])
                 os.system('/usr/bin/ssh -qTfn %s \"bash ~/jboss_%s_restart.sh  >/dev/null\"' % (JBOSSIP[0],JBOSSITEM))
                 JBOSSIP = []
            FILE = open('/data/postmall/deploy/logs/maven/zabbix.log','a')
            FILE.write(TIME+'\t'+NAME+'\n')
            FILE.close()
    except:
        pass

   
    try:
        if re.search(r'^tomcat\d{1,2}',NAME).group():
	 		TOMCAT = re.search(r'^tomcat\d{1,2}',NAME).group()
			os.system('/usr/bin/ssh -qTfn %s \"bash ~/shell/tomkill.sh %s >/dev/null\"' % (IP,TOMCAT))
			FILE = open('/data/postmall/deploy/logs/maven/zabbix.log','a')
			FILE.write(TIME+'\t'+IP+'\t'+NAME+'\n')
			FILE.close()
    except:
        pass

    try:
        if re.search(r'More\ than\ 80',NAME).group() and HOST == "172.24.139.23":
            ds_ip = re.search(r'(.*),(.*),.*More\ than\ 80',NAME).group(1) 
            jboss_server = re.search(r'(.*),(.*),.*More\ than\ 80',NAME).group(2) 
            ds_name = NAME.replace(","," ")
            os.system('/usr/bin/ssh -qTfn  %s \"nohup bash ~/jboss_%s_restart.sh >/dev/null 2>&1 &\"' % (ds_ip,jboss_server))
            FILE = open('/data/postmall/deploy/logs/maven/zabbix.log','a')
            FILE.write(TIME+'\t'+'\t'+ds_name+'\n')
            FILE.close()
    except:
        pass


	try:
		if re.search(r'Low free disk space .*/data',NAME).group():
			os.system('bash /data/postmall/lihao/check_space.sh %s >/dev/null' % IP)
			FILE = open('/data/postmall/deploy/logs/maven/zabbix.log','a')
			FILE.write(TIME+'\t'+IP+'\t'+NAME+'\n')
			FILE.close()
	except:
		pass

	try:
		if re.search(r'^Port\ (\d{4,5})',NAME).group():
			PORT = re.search(r'^Port (\d{4,5})',NAME).group(1)
			if PORT == '8009':
				TOMCAT = '1'
			elif PORT == '9009':
				TOMCAT = '2'
			elif PORT == '7009':
				TOMCAT = '3'
			elif PORT == '6009':
				TOMCAT = '4'
			elif PORT == '5009':
				TOMCAT = '5'
			elif PORT == '4009':
				TOMCAT = '6'
			elif PORT == '3009':
				TOMCAT = '7'
			elif PORT == '2009':
				TOMCAT = '8'
			elif PORT == '18009':
				TOMCAT = '11'
			elif PORT == '19009':
				TOMCAT = '12'
			elif PORT == '17009':
				TOMCAT = '13'
			elif PORT == '16009':
				TOMCAT = '14'
			elif PORT == '15009':
				TOMCAT = '15'
			elif PORT == '14009':
				TOMCAT = '16'
			elif PORT == '13009':
				TOMCAT = '17'
			elif PORT == '12009':
				TOMCAT = '18'
           		elif PORT == '28009':
           		    TOMCAT = '21'
           		elif PORT == '29009':
           		    TOMCAT = '22'
           		elif PORT == '27009':
           		    TOMCAT = '23'
           		elif PORT == '26009':
           		    TOMCAT = '24'
			if TOMCAT:
				os.system('/usr/bin/ssh -qTfn %s \"bash ~/t%s_restart.sh >/dev/null \"' % (IP,TOMCAT))
				FILE = open('/data/postmall/deploy/logs/maven/zabbix.log','a')
				FILE.write(TIME+'\t'+IP+'\t'+NAME+'\n')
				FILE.close()

	except:
		pass
    
	try:
		if re.search(r'^TT(\d{4,5})',NAME).group():
			PORT = re.search(r'TT(\d{4,5})',NAME).group(1)
			if PORT == '12000':
				TTserver = 'ttserver12000'
			if PORT == '13000':
				TTserver = 'ttserver13000'
			if PORT == '14000':
				TTserver = 'ttserver14000'
			if PORT == '15000':
				TTserver = 'ttserver15000'
			if PORT == '16000':
				TTserver = 'ttserver16000'
			if PORT == '17000':
				TTserver = 'ttserver17000'
			if PORT == '18000':
				TTserver = 'ttserver18000'
			if PORT == '24000':
				TTserver = 'ttserver24000'
			if PORT == '26000':
				TTserver = 'ttserver26000'
			if TTserver:
				os.system('/usr/bin/ssh -qTfn %s \"bash ~/%s_restart.sh >/dev/null \"' % (IP,TTserver))
				FILE = open('/data/postmall/deploy/logs/maven/zabbix.log','a')
				FILE.write(TIME+'\t'+IP+'\t'+NAME+'\n')
				FILE.close()

	except:
		pass
    









if __name__ == '__main__' :
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('172.24.138.79', 8001))
	sock.listen(1)
	while True:
	    connection,address = sock.accept()
	    #print'Connected by',address
	    try:
	        connection.settimeout(5)
	        buf = connection.recv(1024)
	        cmd_status,cmd_result = commands.getstatusoutput(buf)
		print cmd_result
		result=eval(cmd_result)
		restart_port(result['TIME'],result['IP'],result['NAME'],result['HOST'])
	        if len(cmd_result.strip()) == 0:
	            	connection.sendall('Done!')
	        else:
	        	connection.sendall(cmd_result)
	    except socket.timeout:
	       pass  
	    connection.close()
