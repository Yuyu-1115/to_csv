import csv
from pathlib import Path

input("請將文字複製到raw_data.txt，完成後請按Enter")


with open(str(Path.cwd() / "raw_data.txt"), "r", encoding = "utf-8") as f:
    text_list = f.readlines()

for i in range(0, len(text_list) - 1):
    text_list[i] = text_list[i][:-1]

text_list = text_list[9:]

n = int(input("請輸入資料數量："))
field = ["NO", "許可證/登錄字號", "有效日期", "中文品名", "英文品名", "醫療器材商", "製造業者", "限制項目"]
row_list = list()

k = 0
for i in range(1, n + 1):
    row_list.append([""])
    row_list[i - 1][0] = str(i)
    k += 1
    row_list[i - 1].extend([
            text_list[k] + text_list[k + 1], #字號
            text_list[k + 2], #有效日期
            text_list[k + 3], #中文品名
            text_list[k + 4], #英文品名
            text_list[k + 5], #公司名稱
            text_list[k + 6], #製造業者
        ])
    # row_list[i - 1][2] = str(int(row_list[i - 1][2][0:3]) + 1911) + row_list[i - 1][2][3:]
    # 轉換為西元年
    k += 7
    row_list[i - 1].append("")
    while text_list[k].startswith("R"):  
        row_list[i - 1][7] += text_list[k] + "\n"
        k += 1
        if k == len(text_list):
            break
    row_list[i - 1][7] = row_list[i - 1][7][:-1]

with open("output.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(field)
    for item in row_list:
        csv_writer.writerow(item)
print("完成轉換")

