import jieba

strs=["圍魏救趙"]
for str in strs:
    seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
    print("Paddle Mode: " + '/'.join(list(seg_list)))

seg_list = jieba.cut("圍魏救趙", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("圍魏救趙", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

#seg_list = jieba.cut("如果沒有好好處理錯誤狀況")  # 默认是精确模式
#print(", ".join(seg_list))

seg_list = jieba.cut_for_search("圍魏救趙")  # 搜索引擎模式
print(", ".join(seg_list))