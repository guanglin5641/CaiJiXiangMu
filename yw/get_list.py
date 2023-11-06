import json
from yw_interface import api_requester
from CaiJiXiangMu.common.rout import METHOD_NAME

method = METHOD_NAME()
def creat_order():
    # 将 JSON 对象转换为字符串
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
    # 发送请求并接收数据
    response_data = api_requester.send_request(data=data, method=method.create_waybill)
    # 打印接收到的数据
    return (response_data)



if __name__ == '__main__':
    print(creat_order())