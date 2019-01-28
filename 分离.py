#import pymysql as mysql 
import MySQLdb as mysql #更换数据库驱动为C驱动程序，py驱动太慢了

db = mysql.connect("localhost", "root", "root", "test", use_unicode=True, charset="utf8")
data = db.cursor()
# MySQL数据库驱动
id=0

data.execute('select count(*) as num from sheet1')
db.commit()
# SQL 查询序号最大值
limit_tuple=data.fetchone()
max=int(limit_tuple[0])-1
print("找到",limit_tuple[0],"条可续命记录")
sql_num=0
# 设定初始值
while sql_num <= max :
    sql_num += 1
    # SQL 查询语句
    data.execute('SELECT 详情 from sheet1 where 序号 = %s',(sql_num,))
    # 提交到数据库执行
    data_init = data.fetchone()
    # 取得数据库返回值
    data_intermediate_0 = data_init[0].split('\n')
    # 分割得到的数据
    data_intermediate_1 = [([0] * 2) for i in range(20)]
    # 初始化列表。

    try:
        i = 0
        while i < (len(data_intermediate_0)) and len(data_intermediate_0) > 0 : 
            # 启动数据分离循环，并判断是否未读出数据
            data_intermediate_1[i] = data_intermediate_0[i].split(':')
            data_intermediate_1[i][0] = data_intermediate_1[i][0].replace(' ','')
            data_intermediate_1[i][1] = data_intermediate_1[i][1].replace(' ','')
            # 去除无用的空格
            i += 1
    except:
            print("WARING,分离循环0异常!")
            # 错误跳出

    try:
        zdxq=dns=ydk=fwdk=yylb=yygz=mfzljs=xy=mac=url=fwym=ltdz=jszh=fszh=bt=""
        t = 0
    except:
        print("WARING,初始化部分变量异常!")
    try:
        while t < 19 and data_intermediate_1[t][0] != 0 :
            t+=1
            if   data_intermediate_1[t-1][0] == '终端详情' :
                  zdxq=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == 'DNS' :
                  dns=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '源端口' :
                  ydk=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '服务端口' :
                  fwdk=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '应用类别' :
                  yylb=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '应用规则' :
                  yygz=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '每分钟连接数' :
                  mfzljs=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '协议' :
                  xy=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == 'mac' :
                  mac=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == 'URL地址' :
                  url=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '访问域名' :
                  fwym=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '聊天动作' :
                  ltdz=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '接收帐号' :
                  jszh=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '发送帐号' :
                  fszh=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '标题' :
                  bt=data_intermediate_1[t-1][1]
            elif data_intermediate_1[t-1][0] == '0' :
                  break
            else :
                  break
    except:
            print("WARING,分离循环1异常!")
            #傻逼分离做完了

    # 令人想死的插入语句
    data.execute('INSERT INTO mdzz1 (终端详情,DNS,源端口,服务端口,应用类别,应用规则,每分钟连接数,协议,mac,URL地址,访问域名,聊天动作,接收帐号,发送帐号,标题) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(zdxq,dns,ydk,fwdk,yylb,yygz,mfzljs,xy,mac,url,fwym,ltdz,jszh,fszh,bt))
    # 提交到数据库执行
    db.commit()

    if data.fetchone() == None :
        print('插入数据第 %s 条时成功续命。' %sql_num)
    else :
        print('插入数据第 %s 条时成功送命。' %sql_num)
	    #要闷声发大财，吼不吼啊？

db.close()
# 关闭数据库连接
abbc=input('等一下，主席。')
