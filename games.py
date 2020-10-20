import random
import requests
#调用requests库
from bs4 import BeautifulSoup

#获取数据
res_foods=requests.get('https://www.xiachufang.com/explore')
#解析数据
bs_foods=BeautifulSoup(res_foods.text,'html.parser')

#查找关于菜单的和URL的<p>标签
tag_name=bs_foods.find_all('p',class_='name')
#查找包含食材的<p>标签
tag_ingredients=bs_foods.find_all('p',class_='ing elipsis')
#创建空列表,用于存储信息
list_all=[]
#启动一次循环，次数等于菜名的数量
for x in range(len(tag_name)):
  #提取信息,封装为列表。此处使用的是<p>标签，之前用的是<a>
  list_food=[tag_name[x].text.strip(),tag_name[x],find('a')['href'],tag_ingredients[x].text.strip()]
  #将信息添加进list_all中
  list_all.append(list_food)
  #打印
print(list_all)
