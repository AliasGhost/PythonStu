import pandas as pd
import re

# 读取 Excel 文件
input_file = 'xxx.xlsx'  # 输入 Excel 文件路径
output_file = './output-07.xlsx'  # 输出 Excel 文件路径
sheet_name = 'Sheet1'  # 要处理的工作表名称
column_name = '详细描述'  # 要处理的列名称

# 读取 Excel 文件
df = pd.read_excel(input_file, sheet_name=sheet_name)

# 处理文本，替换所有换行符为空格
def replace_newlines(text):
    # 替换所有类型的换行符为空格
    text = re.sub(r'[\r\n]+', ' ', text)
    return text

# 应用文本处理
df[column_name] = df[column_name].astype(str).apply(replace_newlines)

# 保存处理后的数据到新的 Excel 文件
df.to_excel(output_file, index=False)

print(f"数据处理完成，结果已保存到 {output_file}")