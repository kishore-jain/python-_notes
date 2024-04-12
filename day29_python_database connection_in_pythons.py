import pymysql

dbc = pymysql.connect(host='localhost',user='root',passwd='',db='sla')

c=dbc.cursor()

c.execute('select * from mnr')

output = c.fetchall()

for i in output:
    print('--------------------------------------------------------')
    print('|',i,'|')
    print('--------------------------------------------------------')

dbc.close()
