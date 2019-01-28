#import pymysql as mysql 
import MySQLdb as mysql #更换数据库驱动为C驱动程序，py驱动太慢了
import re
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class PrpCrypt(object):
 
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
 
    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)
 
    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')
 
	
db = mysql.connect("localhost", "root", "root", "test", use_unicode=True, charset="utf8")
data = db.cursor()
data.execute('select count(*) as num from mdzz1')
db.commit()
# SQL 查询序号最大值
limit_tuple=data.fetchone()
max=int(limit_tuple[0])
print("找到",limit_tuple[0],"条可续命记录")
#设定初始值
sql_num=1
password = PrpCrypt('necenter89631358')
while sql_num <= max : 
	# SQL 查询语句
	data.execute('SELECT 用户名 from sheet1 where 序号 = %s',(sql_num,))
	db.commit()
	data_init_0 = data.fetchone()
    # 取得数据库返回值

	if data_init_0 == None :
		print(sql_num,'值已被删除')
		sql_num += 1
		continue
	#查看数据是否已被删除
	#print(len(data_init[0]))
	
	if len(data_init_0[0]) >20 :
		print(sql_num,'已被处理')
		sql_num += 1
		continue
	#查看数据是否已被处理
	
	try:
		data.execute('SELECT * from mdzz1 where 序号 = %s',(sql_num,))
		#print('提交到数据库执行')
		db.commit()
		data_init = data.fetchone()
		#print(data_init)
	except:
		sql_num += 1
		continue
		print('取得数据库返回值错误')
	try:
		data_init = list(data_init)
	except:
		continue
	i=0
	while i<16 :
		if i==0 :
			data_init[i]=str('')
			i+=1
		elif (i==1 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'终端类型：'+str(data_init[i])
			i+=1
		elif (i==2 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\nDNS：'+str(data_init[i])
			i+=1
		elif (i==3 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n源端口：'+str(data_init[i])
			i+=1
		elif (i==4 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n服务端口：'+str(data_init[i])
			i+=1
		elif (i==5 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n应用类别：'+str(data_init[i])
			i+=1
		elif (i==6 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n应用规则：'+str(data_init[i])
			i+=1
		elif (i==7 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n每分钟连接数：'+str(data_init[i])
			i+=1
		elif (i==8 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n协议：'+str(data_init[i])
			i+=1
		elif (i==9 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\nmac：'+ str(password.encrypt(data_init[i]))
			i+=1
		elif (i==10 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\nURL地址：'+str(data_init[i])
			i+=1
		elif (i==11 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n访问域名：'+str(data_init[i])
			i+=1
		elif (i==12 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n聊天动作：'+str(data_init[i])
			i+=1
		elif (i==13 and len(data_init[i])!= 0) :
#			print(len(data_init[i]))
			data_init[0]=data_init[0]+'\\n接收账号：'+ str(password.encrypt(data_init[i]))
			i+=1
		elif (i==14 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n发送账号：'+ str(password.encrypt(data_init[i]))
			i+=1
		elif (i==15 and len(data_init[i])!= 0) :
			data_init[0]=data_init[0]+'\\n标题：'+str(data_init[i])
			i+=1
		else :
			i+=1
		#循环好歹设计好了
	finaldata = data_init[0] #这是拿出来的数据
	#处理学号

	data_intermediate = data_init_0[0].split('[')
		
	if len(data_intermediate[0]) == 12:
		nb = re.findall(r'.{4}', str(data_intermediate[0]))
		number= nb[1] + nb[2]
		ID = nb[0] + str(password.encrypt(number))
		data.execute('UPDATE sheet1 SET 详情 = "%s" , 用户名 = "%s" WHERE 序号 = "%s"',(finaldata,ID,sql_num))
		#print([finaldata,tunnel])
		#print(finaldata)
	else:
		data.execute('DELETE FROM sheet1 WHERE 序号 = "%s"',(sql_num,))
	print('处理',sql_num,'完成')
	db.commit()	
	#数据库操作递交
	sql_num += 1
print('已处理',sql_num)
print("理论上完事了，还没完就送命了~")
db.close()
