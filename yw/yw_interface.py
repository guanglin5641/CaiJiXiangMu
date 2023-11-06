import requests
import hashlib
import json
import time
from urllib.parse import urlencode
import urllib3
import yaml

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIRequester:
    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        self.api_url = config['yw_config']['api_url']
        self.api_token = config['yw_config']['api_token']
        self.user_id = config['yw_config']['user_id']


    def generate_signature(self, data, format, method, timestamp, version):
        timestamp = str(timestamp)
        params = [
            self.user_id,
            data,
            format,
            method,
            timestamp,
            version
        ]
        concatenated_params = self.api_token+''.join(params)+self.api_token
        # print(concatenated_params)
        signature = hashlib.md5(concatenated_params.encode('utf-8')).hexdigest()
        # print(signature)
        return signature

    def create_request_url(self, data, format, method, version):
        timestamp = int(time.time() * 1000)
        signature = self.generate_signature(data, format, method, timestamp, version)
        params = {
            'user_id': self.user_id,
            'format': format,
            'method': method,
            'timestamp': timestamp,
            'version': version,
            'sign': signature,
            'data': data,
        }
        request_url = f"{self.api_url}?{urlencode(params)}"
        return request_url

    def send_request(self, data, method):
        # Assuming format and version are constant, you can modify them accordingly
        format = "json"
        version = "V1.0"
        data_str = json.dumps(data)
        request_url = self.create_request_url(data_str, format, method, version)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(request_url, json=json.loads(data_str), headers=headers, verify=False)

        if response.status_code == 401:
            print(f"请求失败，状态码 401。内容：{response.text}")
        elif response.status_code == 200:
            try:
                return response.json()
            except json.decoder.JSONDecodeError as e:
                print(f"无法解码 JSON 响应。内容：{response.text}")
                raise e
        else:
            print(f"请求失败，状态码 {response.status_code}。内容：{response.text}")
            response.raise_for_status()
api_requester = APIRequester('../config.yaml')

if __name__ == '__main__':
    data = {
    "channelId": "481",
    "orderSource": "portal",
    "userId": "账号",
    "orderNumber": "KI1000000001A",
    "dateOfReceipt": "2022-07-10",
    "remark": "拣货单信息",
    "receiverInfo": {
        "name": "glassware",
        "phone": "18231730588",
        "email": "529932298@qq.com",
        "company": "yanwen",
        "country": "115",
        "state": "he bei sheng",
        "city": "cang zhou shi",
        "zipCode": "10110",
        "houseNumber": "#4501124",
        "address": "he fang jie cang zhou kai fa qu",
        "taxNumber": "qwer123"
    },
    "parcelInfo": {
        "productList": [
            {
                "goodsNameCh": "杯子",
                "goodsNameEn": "CUP",
                "price": "12.5",
                "hscode": "8400000001",
                "url": "http://www.aliexpress.com/item//32681820727.html",
                "material": "material",
                "quantity": "10",
                "weight": "1000"
            },
            {
                "goodsNameCh": "杯子",
                "goodsNameEn": "CUP",
                "price": "12.5",
                "hscode": "8400000001",
                "url": "http://www.aliexpress.com/item//32681820727.html",
                "material": "material",
                "quantity": "10",
                "weight": "1000"
            }
        ],
        "hasBattery": 1,
        "currency": "USD",
        "totalPrice": "50.01",
        "totalQuantity": "10",
        "totalWeight": "243",
        "height": "10",
        "width": "10",
        "length": "10",
        "ioss": "123456"
    },
    "senderInfo": {
        "name": "glassware",
        "phone": "18231730588",
        "email": "529932298@qq.com",
        "company": "yanwen",
        "country": "115",
        "state": "he bei sheng",
        "city": "cang zhou shi",
        "zipCode": "101110",
        "houseNumber": "#4501124",
        "address": "he fang jie cang zhou kai fa qu",
        "taxNumber": "qwer123"
    }
}
    method = 'express.order.create'
    result = api_requester.send_request(data=data, method=method)
    print(result)

