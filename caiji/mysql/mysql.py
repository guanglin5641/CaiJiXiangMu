import pymysql
#封装创建语句
def create_table(database_name, table_name, columns):
    # Establish a connection to the database
    conn = pymysql.connect(host='localhost', user='root', password='123mysql', charset='utf8', database=database_name)
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Build the SQL query to create the table
    create_table_query = f"CREATE TABLE {table_name}  {columns}"
    print(create_table_query)
    # Execute the SQL query
    cursor.execute(create_table_query)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Table '{table_name}' created in database '{database_name}'.")
#封装查询语句
def select_sql(database_name, columns, where):
    # 建立与数据库的连接
    conn = pymysql.connect(host='localhost', user='root', password='123mysql', charset='utf8', database=database_name)
    try:
        # 创建游标对象以执行SQL查询
        with conn.cursor() as cursor:
            # 构建查询数据的SQL查询语句
            select_query = f"SELECT {columns} FROM {where};"
            # 执行SQL查询
            print(select_query)
            cursor.execute(select_query)
            # 从数据库中获取数据
            data = cursor.fetchall()
            # 输出获取到的数据
            # print(data)
            return data
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        # 关闭连接
        conn.close()
# 封装插入语句
# def insert_sql(database_name, table_name, columns, values):
#     # 建立与数据库的连接
#     conn = pymysql.connect(host='localhost', user='root', password='123mysql', charset='utf8', database=database_name)
#     # 创建游标对象以执行SQL查询
#     cursor = conn.cursor()
#     # 构建插入数据的SQL查询语句
#     insert_query = f"INSERT INTO {table_name} ({columns}) VALUES {values};"
#     print(insert_query)
#     # 执行SQL查询
#     cursor.execute(insert_query)
#     # 提交更改并关闭连接
#     conn.commit()
#     conn.close()
#     print(f"在数据库 '{database_name}' 中修改了表 '{table_name}'。")
def insert_sql(database_name, table_name, columns, values):
    # 建立与数据库的连接
    conn = pymysql.connect(host='localhost', user='root', password='123mysql', charset='utf8', database=database_name)
    # 创建游标对象以执行SQL查询
    cursor = conn.cursor()
    # 构建插入数据的SQL查询语句
    insert_query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES {values};"
    print(insert_query)
    # 执行SQL查询
    cursor.execute(insert_query)
    # 提交更改并关闭连接
    conn.commit()
    conn.close()
    print(f"在数据库 '{database_name}' 中修改了表 '{table_name}'。")


#封装更新语句
def update_sql(database_name, table_name, update_data, where):
    # 建立与数据库的连接
    conn = pymysql.connect(host='localhost', user='root', password='123mysql', charset='utf8', database=database_name)
    # 创建游标对象以执行SQL查询
    cursor = conn.cursor()
    # 构建SET子句
    set_clause = ', '.join([f"{column} = '{value}'" for column, value in update_data.items()])
    # 构建INSERT ... ON DUPLICATE KEY UPDATE语句
    update_query = f"INSERT INTO {table_name} SET {set_clause} ON DUPLICATE KEY UPDATE {set_clause};"
    print(update_query)
    # 执行SQL查询
    cursor.execute(update_query)
    # 提交事务并关闭连接
    conn.commit()
    conn.close()
    print(f"成功更新数据库 '{database_name}' 中的表 '{table_name}'。")
