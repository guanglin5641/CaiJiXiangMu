import requests
import hashlib
import json
import time
class ApiRequest:
    def __init__(self, api_url, user_id, api_token):
        self.api_url = api_url
        self.user_id = user_id
        self.api_token = api_token
    def generate_signature(self, data, format='json', method='express.order.create', timestamp=None, version='V1.0'):
        if timestamp is None:
            timestamp = int(time.time())
        params = self.user_id + json.dumps(data) + format + method + str(timestamp) + version
        params_with_token = self.api_token + params + self.api_token
        signature = hashlib.md5(params_with_token.encode()).hexdigest()
        return signature
    def send_request(self, data, format='json', method='express.order.create', timestamp=None, version='V1.0'):
        if timestamp is None:
            timestamp = int(time.time())
        signature = self.generate_signature(data, format, method, timestamp, version)
        payload = {
            'user_id': self.user_id,
            'data': json.dumps(data),
            'format': format,
            'method': 'express.channel.getlist',
            'timestamp': str(timestamp),
            'version': version,
            'sign': signature
        }
        try:
            response = requests.post(self.api_url, json=payload)
            if response.status_code == 200:
                response_data = response.json()
            else:
                print('请求失败:', response.status_code)
        except Exception as e:
            print('发送请求失败:', e)
if __name__ == '__main__':
    api_url = 'Https://open.yw56.com.cn/api/order'
    user_id = '20170073'
    api_token = '55E0CE9E3B4A61C10B046613C3A7EC2D'

data ={

}


api_request = ApiRequest(api_url, user_id, api_token)
api_request.send_request(data)


