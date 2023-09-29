import requests
import json
import caiji.mysql as mysql
 # 登录
def login():
    url = "https://pro.gateway.lonfenner.com/auth/cus/login"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,de;q=0.7,fr;q=0.6,it;q=0.5,es;q=0.4,pl;q=0.3,sv;q=0.2",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "pro.gateway.lonfenner.com",
        "Origin": "https://www.maijiazaixian.cn",
        "Referer": "https://www.maijiazaixian.cn/",
        "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    payload = {
        "loginType": 0,
        "userName": "wenyaohua",
        "password": "yaohua666",
        "verificationCode": ""
    }
    response = requests.post(url, headers=headers, json=payload)
    json_response = response.json()
    access_token = json_response["data"]["accessToken"]
    bearer_token = "Bearer " + access_token
    print('登录成功')
    return bearer_token
 # 获取ID和主体
def get_api_data(authorization):
    url = "https://pro.gateway.lonfenner.com/esproduct/mine/product/list"
    params = {
        "isAsc": "",
        "orderByColumn": "",
        "pageNum": 1,
        "pageSize": 520
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": authorization,
        "Connection": "keep-alive",
    }
    response = requests.get(url, params=params, headers=headers)
    json_response = response.json()
     # 保存JSON数据到文件
    with open("../../response.json", "w", encoding="utf-8") as file:
        json.dump(json_response, file, ensure_ascii=False, indent=4)
    print("JSON数据已保存到文件response.json")
     # 将data.items.id吸入数据库
    for item in json_response["data"]["items"]:
        if "id" in item:
            id = item["id"]
            sku = item["sku"]
            salePrice = item["salePrice"]
            title = item["title"] if "title" in item else "Null"
            sourceUrl = item["sourceUrl"] if item["sourceUrl"] is not None else "Null"
            values = id, sku, salePrice, title, sourceUrl, 20
            print(values)
            mysql.insert_sql('data', 'parent_parentage', '`MJ_id`,`Seller_SKU`, `Standard Price`, `Item Name`, URL,Quantity', values)
        else:
            print("无效的数据项：", item)
    return json_response
 # 根据id获取列表
def get_api_list(id, authorization):
    url = "https://pro.gateway.lonfenner.com/esproduct/mine/product/selectDetailById/{id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": authorization,
        "Connection": "keep-alive",
    }
    response = requests.get(url.format(id=id), headers=headers)
    json_response = response.json()
    print(json_response)
    return json_response
#根据ID更新
def update_list():
    authorization = login()
    header = authorization
    a = mysql.select_sql('data', '`MJ_id`',
                         'parent_parentage pp LEFT JOIN child_parentage cp ON cp.parent_MJ_id = pp.MJ_id where cp.parent_MJ_id is null')
    for i in a:
        id = i[0]
        json_response = get_api_list(id, authorization)
        json_parent = json_response["data"]
        parent_sku = json_parent["sku"]
        bulletPoint1 = json_parent['description']["bulletPoint1"].replace("'", " ")
        bulletPoint2 = json_parent['description']["bulletPoint2"].replace("'", " ")
        bulletPoint3 = json_parent['description']["bulletPoint3"].replace("'", " ")
        bulletPoint4 = json_parent['description']["bulletPoint4"].replace("'", " ")
        bulletPoint5 = json_parent['description']["bulletPoint5"].replace("'", " ")
        Product_Description = json_parent['description']["textDescription"].replace("\n", "<br/>").replace("'", " ")
        update_data = {
            "bullet_point1": bulletPoint1,
            "bullet_point2": bulletPoint2,
            "bullet_point3": bulletPoint3,
            "bullet_point4": bulletPoint4,
            "bullet_point5": bulletPoint5,
        }
        update_data["Product_Description"] = json_parent['description']["textDescription"].replace("\n", "<br/>").replace("'", " ")
        where = "WHERE `Seller_SKU` = '%s'" % parent_sku
        mysql.update_sql('data', 'parent_parentage', update_data, where)
        for item in json_response["data"]["children"]:
            if "id" in item:
                parentId = item["parentId"]
                sku = item["sku"]
                upc = int(item.get("upc", "Null"))
                UPC_type = 'EAN'
                title = item.get("title", "Null")
                salePrice = item["salePrice"]
                Quantity = 20
                main_image_url = item['images'][0].get("sourceUrl", "Null")if len(item['images']) > 0 else "Null"
                other_image_urls1 = item['images'][1].get("sourceUrl", "Null")if len(item['images']) > 1 else "Null"
                other_image_urls2 = item['images'][2].get("sourceUrl", "Null")if len(item['images']) > 2 else "Null"
                other_image_urls3 = item['images'][3].get("sourceUrl", "Null")if len(item['images']) > 3 else "Null"
                other_image_urls4 = item['images'][4].get("sourceUrl", "Null")if len(item['images']) > 4 else "Null"
                other_image_urls5 = item['images'][5].get("sourceUrl", "Null")if len(item['images']) > 5 else "Null"
                other_image_urls6 = item['images'][6].get("sourceUrl", "Null")if len(item['images']) > 6 else "Null"
                other_image_urls7 = item['images'][7].get("sourceUrl", "Null")if len(item['images']) > 7 else "Null"
                other_image_urls8 = item['images'][8].get("sourceUrl", "Null") if len(item['images']) > 8 else "Null"
                variation_theme = item['variationData']['themeCode']
                color_name = item['variationData']['items'][0].get("value", "Null")
                size_name = item['variationData']['items'][1].get("value", "Null")


                values = (
                    sku, upc, UPC_type, title, salePrice, Quantity, main_image_url,
                    other_image_urls1, other_image_urls2, other_image_urls3,
                    other_image_urls4, other_image_urls5, other_image_urls6,
                    other_image_urls7, other_image_urls8, parent_sku, variation_theme, color_name, size_name, parentId
                )
                mysql.insert_sql(
                    'data', 'child_parentage',
                    '`Seller_SKU`,`Product ID`,`Product ID Type`,`Item Name`,`Standard Price`,`Quantity`,`main_image_url`,`other_image_url1`,`other_image_url2`,`other_image_url3`,`other_image_url4`,`other_image_url5`,`other_image_url6`,`other_image_url7`,`other_image_url8`,`parent_sku`,`variation_theme`,`color_name`,`size_name`,`parent_MJ_id`',values)
            else:
                print("无效的数据项：", item)
if __name__ == '__main__':
    get_api_data(login())
    update_list()