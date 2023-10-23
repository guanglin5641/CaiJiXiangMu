from flask import Flask, request, jsonify
import caiji.mysql.mysql
app = Flask(__name__)
@app.route('/get_data')
def get_data():
    page_size = request.args.get('page_size', default=10, type=int)
    page = request.args.get('page', default=1, type=int)
    columns = "id,Seller_SKU,Item_Name,Standard_Price,URL"
    where = f"parent_parentage LIMIT {page_size * (page - 1)}, {page_size}"
    result = caiji.mysql.mysql.select_sql("data",columns, where)
    data = []
    for row in result:
        item = {
        "id": row[0],
        "Seller_SKU": row[1],
        "Item_Name": row[2],
        "Standard_Price": row[3],
        "URL": row[4]
        }
        data.append(item)
    if result:
        response = {
            "code": 200,
            "message": "Success",
            "data": data
        }
    else:
        response = {
            "code": 404,
            "message": "No data found",
            "data": []
        }
    return jsonify(response)

# @app.route('/get_product_details')
# def get_product_details():
#     id== request.args.get('id', default=10, type=int)





if __name__ == '__main__':
    app.run()