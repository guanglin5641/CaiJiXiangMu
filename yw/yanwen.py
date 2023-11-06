import requests
import hashlib
import json
import time
class ApiRequest:
    def __init__(self, api_host, user_id, api_token):
        self.api_host = api_host
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
            'method': method,
            'timestamp': str(timestamp),
            'version': version,
            'sign': signature
        }
        try:
            api_url = self.api_host + '?user_id=' + self.user_id + '&method=' + method + '&format=' + format + '&timestamp=' + str(
                timestamp) + '&sign=' + signature + '&version=' + version
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                response_data = response.json()
            else:
                print('请求失败:', response.status_code)
            print('请求的URL:', api_url)  # 打印请求的URL
            print('请求方式: POST')  # 打印请求方式
            print('请求body:', payload)  # 打印请求body
            print('请求头:', response.headers)  # 打印请求头
        except Exception as e:
            print('发送请求失败:', e)
if __name__ == '__main__':
    api_host = 'Https://open.yw56.com.cn/api/order'
    user_id = '20170073'
    api_token = '55E0CE9E3B4A61C10B046613C3A7EC2D'
 # data = {...}  # 你的数据


data = {
    "channelId": "155",  # 产品编号
    "orderSource": "自建",  # 订单来源
    "userId": "20170073",  # 用户ID
    "orderNumber": "KI1000000001A",  # 订单号
    "dateOfReceipt": "",  # 收款到账日期
    "remark": "",  # 拣货单信息/备注
    "receiverInfo": {  # 收件人信息
        "name": "Suzanne M Salata",  # 收件人姓名
        "phone": "1823111588",  # 收件人电话
        "email": "",  # 收件人邮箱
        "company": "",  # 收件人公司
        "country": "115",  # 目的国id或目的国二字码
        "state": "",  # 收件人州（省）
        "city": "",  # 收件人城市
        "zipCode": "101110",  # 邮编
        "houseNumber": "",  # 收件人门牌号
        "address": "jia xing wu liu yuan A22-28",  # 收件人地址
        "taxNumber": ""  # 收件人税号
    },
    "parcelInfo": {  # 包裹信息
        "hasBattery": 0,  # 是否带电，1: 是，0: 否
        "currency": "USD",  # 币种代码
        "totalPrice": "40.00",  # 申报总价值
        "totalQuantity": "1",  # 申报总数量
        "totalWeight": "300",  # 总重量（单位：克）
        "height": "",  # 包裹高（单位：厘米）
        "width": "",  # 包裹宽（单位：厘米）
        "length": "",  # 包裹长（单位：厘米）
        "ioss": "",  # IOSS税号
        "productList": [  # 商品信息（支持5组）
            {
                "goodsNameCh": "摩托车居家服",  # 中文品名
                "goodsNameEn": "Motorcycle Homewear",  # 英文品名
                "price": "12.50",  # 申报单价
                "quantity": "2",  # 数量
                "weight": "100",  # 单件重量（单位：克）
                "hscode": "",  # 海关编码
                "url": "",  # 商品链接
                "material": ""  # 商品材质
            },
            {
                "goodsNameCh": "薄纱花朵连衣裙",  # 中文品名
                "goodsNameEn": "tulle floral dress",  # 英文品名
                "price": "15.00",  # 申报单价
                "quantity": "1",  # 数量
                "weight": "100",  # 单件重量（单位：克）
                "hscode": "",  # 海关编码
                "url": "",  # 商品链接
                "material": ""  # 商品材质
            }
        ]
    },
    "senderInfo": {  # 发件人信息
        "name": "",  # 发件人姓名
        "phone": "",  # 发件人电话
        "company": "",  # 发件人公司
        "email": "",  # 发件人邮箱
        "country": "",  # 发件人国家（默认为CN）
        "state": "",  # 发件人州（省）
        "city": "",  # 发件人城市
        "zipCode": "",  # 发件人邮编
        "houseNumber": "",  # 发件人门牌号
        "address": "",  # 发件人地址
        "taxNumber": ""  # 发件人税号
    }
}
api_request = ApiRequest(api_host, user_id, api_token)
api_request.send_request(data)
#打印请求信息
print(api_request.__dict__)


