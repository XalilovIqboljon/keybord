import requests
from pprint import pprint

token = "1679454024:AAEs98zOJvEYgdYwbZgFaJQQMSsBHFWHdnc"
def sendKeyboard(idx):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    
    payload ={
        'chat_id':idx,
        'text':'Button',
        'reply_markup':{
            'keyboard':[[{'text':1},{'text':2}]]
        }
    }
    r=requests.post(url,json=payload)
    
    return r.json()


ids=1395234286

pprint(sendKeyboard(ids))