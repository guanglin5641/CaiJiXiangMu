import caiji.mysql.mysql
def get_data(page_size, page):
    columns = "id,Seller_SKU,Item_Name,Standard_Price,URL,MJ_id"
    where = f"parent_parentage LIMIT {page_size * (page - 1)}, {page_size}"
    result = caiji.mysql.mysql.select_sql("data", columns, where)
    data = []
    for row in result:
        item = {
            "id": row[0],
            "Seller_SKU": row[1],
            "Item_Name": row[2],
            "Standard_Price": row[3],
            "URL": row[4],
            "MJ_id": row[5]
        }
        data.append(item)
    return data
def page():
    result = caiji.mysql.mysql.select_sql("data", "count(id)", "parent_parentage")
    return result[0][0]
def truncate_string(string, length):
    if len(str(string)) > length:
        return str(string)[:length-3] + "..."
    else:
        return str(string)