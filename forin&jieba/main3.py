# 讀取檔案三步驟
# 1. 所有資源放在專案底下
# 2. 檔案路徑: 相對路徑
# 第一步驟
f = open("a.txt", "r", encoding="utf-8")
# 第二步驟
article = f.read()
# 第三步驟
f.close()

print(article)

result = {}
for c in article:
    # 對的話:我們第二次遇到
    if c in result:
        result[c] = result[c] + 1
    # 錯的話:第一次遇到
    else:
        result[c] = 1
print(result)

# jieba結巴函式庫
import jieba.analyse
keywords = jieba.analyse.extract_tags(article, 5)
print("最關鍵的詞:", keywords)

