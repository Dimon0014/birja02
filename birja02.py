import json
import math
import requests

res = requests.get('https://yobit.net/api/3/info') # получаем данные info
res_obj = json.loads(res.text) # переводим полученный текст в объект с данными

pairs = [pair for pair in res_obj['pairs']] # создадим массив названий пар
p=0
b=int(len(pairs))
k=int(math.ceil(len(pairs)/23))+23
#k=k+16
print("вне цикла k=", k)
for i in range (0, b+k, 23):
    pairs.insert(i,"\n")
    p=p+1
      # b=b+p
       #print("в цикле b=", b)

    #print("вне цикла b=", b)
   # print("вне цикла p=", p)

pairs_str = '-'.join(pairs)
print(pairs_str)
print(p)