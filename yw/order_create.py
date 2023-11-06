from CaiJiXiangMu.yw.yw_interface import api_requester
import requests
import json

# 原始 JSON 数据
data = '''{"channelId":"481","orderSource":"portal","userId":"账号",
    "orderNumber":"KI1000000001A",
    "dateOfReceipt":"2022-07-10",
    "remark":"拣货单信息",
    "receiverInfo":{
        "name":"glassware",
        "phone":"18231730588",
        "email":"529932298@qq.com",
        "company":"yanwen",
        "country":"115",
        "state":"he bei sheng",
        "city":"cang zhou shi",
        "zipCode":"10110",
        "houseNumber":"#4501124",
        "address":"he fang jie cang zhou kai fa qu",
        "taxNumber":"qwer123"
    },
    "parcelInfo":{
        "productList":[
            {
                "goodsNameCh":"杯子",
                "goodsNameEn":"CUP",
                "price":"12.5",
                "hscode":"8400000001",
                "url":"http://www.aliexpress.com/item//32681820727.html",
                "material":"material",
                "quantity":"10",
                "weight":"1000"
            },
            {
                "goodsNameCh":"杯子",
                "goodsNameEn":"CUP",
                "price":"12.5",
                "hscode":"8400000001",
                "url":"http://www.aliexpress.com/item//32681820727.html",
                "material":"material",
                "quantity":"10",
                "weight":"1000"
            }
        ],
        "hasBattery":1,
        "currency":"USD",
        "totalPrice":"50.01",
        "totalQuantity":"10",
        "totalWeight":"243",
        "height":"10",
        "width":"10",
        "length":"10",
	    "ioss":"123456"
    },
    "senderInfo":{
        "name":"glassware",
        "phone":"18231730588",
        "email":"529932298@qq.com",
        "company":"yanwen",
        "country":"115",
        "state":"he bei sheng",
        "city":"cang zhou shi",
        "zipCode":"101110",
        "houseNumber":"#4501124",
        "address":"he fang jie cang zhou kai fa qu",
        "taxNumber":"qwer123"
    }
}'''

# 将 JSON 数据加载为 Python 对象
json_object = json.loads(data)

# 将 Python 对象转换为 JSON 字符串，去除额外的空格和换行符
compressed_json = json.dumps(json_object, separators=(',', ': '))


method = 'express.order.create'

try:
    result = api_requester.send_request(compressed_json, method)
    print(result)
except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")
