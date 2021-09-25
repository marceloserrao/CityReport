###Imports
import pandas as pd
import pynetbox
import requests

##read excel file     
df = pd.read_excel('cabling.xlsx',sheet_name='DL_Resume',usecols='L:T',skiprows=1 )##.to_dict('records')
#netbox session
session=requests.Session()
session.verify = False          ##Session variables
nb=pynetbox.api(
    'http://172.29.59.238:8000', 
    token=' 0123456789abcdef0123456789abcdef01234567'

)
nb.http_session = session

for i, row in df.iterrows():
    nb.dcim.devices.create(
        hostname = row[0]
        model = row[1]
        serial = row[2]
        ##insert others here
    )
