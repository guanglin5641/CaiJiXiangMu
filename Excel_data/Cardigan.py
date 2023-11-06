# import openpyxl
#
# wb = openpyxl.load_workbook('D:\pythonDma\MaiJiaZaiXian\CaiJiXiangMu\Excel_data\source_table.xlsx')
# sheet = wb['1111']
#
# target_value = 'item_sku'  # 要查找的单元格内容
#
# for row in sheet.iter_rows():
#     for cell in row:
#         if cell.value == target_value:
#             column = cell.column_letter
#             row = cell.row
#             print(f"单元格 '{target_value}' 位于列 {column}，行 {row}")
#             break
# df = pd.read_excel('D:\pythonDma\MaiJiaZaiXian\CaiJiXiangMu\Excel_data\source_table.xlsx', sheet_name='1111', header=None)

import pandas as pd
df = pd.read_excel('D:\pythonDma\MaiJiaZaiXian\CaiJiXiangMu\Excel_data\source_table.xlsx', sheet_name='1111',header=None)
list = df.iloc[4].dropna().index
# print(df.loc[3,1])
# print(list)
x = len(list)
rows = []
columns = []
for i in range(x):
    name = df.loc[2,list[i]]
    result = df.isin([name])
    row, column = result.stack().idxmax()
    # rows.append(row)
    columns.append(column)
    print(column,name)
# print(f"单元格 '{name}' 位于列 {column}，行 {row}")

target_value = 'item_sku'
 # 使用 pandas 的方法查询目标值所在的单元格位置
