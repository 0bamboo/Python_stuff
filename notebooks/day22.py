# ========================= Q90 ==============================
print('========================== Q90 ==========================')
st = input('Enter a string :')
dic = {}
sorted_dic = {}
i = 0
for char in st:
    dic[char] = st.count(char)
sorted_dic = dic.items()
dic = sorted(sorted_dic)
for i in dic:
    print(i)
# print(dic)
print('The dict after sorting keys :', sorted_dic)
# for i in sorted_key:
#     print('{},{}'.format(dic[i],i))