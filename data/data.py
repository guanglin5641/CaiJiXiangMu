import pandas as pd
 # 读取表A中的数据
df_a = pd.read_excel(r'C:\Users\86176\Desktop\Amazon\data\汉情趣内衣.xlsx', sheet_name='sheet1')
 # 复制SKU列到新的DataFrame
df_b = pd.DataFrame(df_a['SKU'])
 # 读取宏文件表B的Template工作表
df_template = pd.read_excel(r'C:\Users\86176\Desktop\Amazon\data\uk.xlsm', sheet_name='Template')
 # 将复制的SKU列添加到Template工作表的item_sku列
df_template['item_sku'] = df_b['SKU']
 # 保存修改后的Template工作表到原宏文件表B
with pd.ExcelWriter(r'C:\Users\86176\Desktop\Amazon\data\uk.xlsm', engine='openpyxl', mode='a') as writer:
    df_template.to_excel(writer, sheet_name='Template', index=False)
 # 保存原状态的宏文件表B
df_b.to_excel(r'C:\Users\86176\Desktop\Amazon\data\uk.xlsm', sheet_name='Template', index=False, startrow=df_template.shape[0]+2)