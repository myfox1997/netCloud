import QcloudApi

module = 'wenzhi'

action = 'TextClassify'

config = {
    'secretId': 'AKIDISP8exVwc5KMAl6JH1YszsY0FG2XDkTw',
    'secretKey': 'JOCl35rNddNuBD4f1EE1by72kFXcU6SY',
    'Region': 'gz',
    'method': 'POST'
}

params = {'content': '男孩子呀你要明白,女孩子的撒娇、女孩子的任性、女孩子的小脾气都是在告诉你,快抱抱我'}

try:
    service = QcloudApi(module, config)

    print(service.call(action, params))
except Exception as e:
    print(e)
