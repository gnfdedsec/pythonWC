import requests
from pprint import pprint
url ='https://opend.data.go.th/govspending/cgdcontract'
token ='vwfxCiKKD2bfNcSBOvpysL0TxrZqq89W'
parameters={'api-key':token,
            'year':2562,
            'keyword':'เรือดำน้ำ'
            }

rq =  requests.get(url,params=parameters)
result = rq.json()
allproject = result['result']
print('จำนวนโปรเจค/โครงการ :',len(allproject),'โครงการ')
#print(type())
#print(type(allproject))
#pprint(result['result'])

allbudget = []
projectname = []
for pj in allproject:

    allbudget.append(int(pj['sum_price_agree'].replace(',','')))
    projectname.append(pj['project_name'])
totalbudget = sum(allbudget)
print('งบประมาณทั้งหมด :'+str(totalbudget)+": บาท")
pprint(result['result'])
