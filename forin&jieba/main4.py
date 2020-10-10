import jieba
# import jieba.analyse (第一種寫法)
# from jieba import analyse (第二種寫法)
from jieba.analyse import extract_tags # (第三種寫法)

# 讀取檔案三步驟
# 1. 所有資源放在專案底下
# 2. 檔案路徑: 相對路徑
# 第一步驟
f = open("a.txt", "r", encoding="utf-8")
# 第二步驟
article = f.read()
# 第三步驟
f.close()

# jieba.load_userdict("./mydict.txt")  # 在文章中修正 (靜態)
jieba.add_word("反正我很閒")  # 新增詞彙 (動態)
jieba.add_word("樂咖")
# ["詞1", "詞2", "詞3"]
# 我中午吃牛排 -> 我 中午 吃 牛排(英文的排列方式)
sep = " ".join(jieba.cut(article))
print(sep)

print("關鍵詞:", extract_tags(article, 5))

