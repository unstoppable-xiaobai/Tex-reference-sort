# -*-coding:utf-8-*-
import os
import cv2
import re

Data_li =[] #所有参考文献的数据集

li_cite_label=[]
li_name=[]
li_titile = []
li_jornal = []
li_year = []
li_volume = []
li_page = []

Counter_li =[]#给index函数用的

with open("./Input.txt" , encoding='utf-8') as Input_data:
    lines  = Input_data.readlines()
    for line in lines:
        if len(line) > 3:
            Data_li.append(line)
for i in range(len(Data_li)) :
    Counter_li.append(0)
    li_cite_label .append("##")
    li_name.append("##")
    li_titile .append("##")
    li_jornal .append("##")
    li_year.append("##")
    li_volume.append("##")
    li_page.append("##")#初始化

def split_the_bib(Data_li, aim_li, split_label, Counter_li):#数据集、目标列表、分隔符标志、开始位置集
    for i in range(len(Counter_li)) : 
        a = Data_li[i].find(split_label, Counter_li[i], len(Data_li[i])-1)
        if a != -1:
            aim_li[i] = Data_li[i][Counter_li[i]:a+1]
            Counter_li[i] = a+1

split_the_bib(Data_li, li_cite_label,"}",Counter_li)
split_the_bib(Data_li, li_name,".",Counter_li)
split_the_bib(Data_li, li_titile,".",Counter_li)
split_the_bib(Data_li, li_jornal,",",Counter_li)
split_the_bib(Data_li, li_year,",",Counter_li)
split_the_bib(Data_li, li_volume,":",Counter_li)
split_the_bib(Data_li, li_page,".",Counter_li)

for i in range (len(Data_li)): #处理作者格式
    names = li_name[i].replace('.', ',')
    names_li = names.split(',')
    if i ==3:
        print(1)
    for j in range(len(names_li)):
        name =names_li[j]
        name_li = name.split(' ')
        name_li.append('1')
        if name_li[0] != '':
            name_li[len(name_li)-1] = name_li[0]
        else:
            name_li[len(name_li)-1]= name_li[1]
            del(name_li[0])
        del(name_li[0])
        names_li[j] = '. '.join(name_li)
    result_name = ', '.join(names_li)
    result_name = result_name[0:len(result_name)-2]
    result_name = result_name.replace('.,', ',')
    result_name= result_name+","
    result_name = result_name.replace('. ,', ',')
    li_name[i] = result_name

for i in range(len(Data_li)):
    if li_page != '##':
        result =  li_cite_label[i]+str(li_name[i])+str(li_titile[i])+str(li_jornal[i].replace(',',''))+str(li_volume[i].replace(':', ''))+" ("+str(li_year[i].replace(',', ''))+")"+str(li_page[i])
        result = result.replace('##','')
        result = result.replace('( ', '(')
        Data_li[i] = result
    else:
        result = li_cite_label[i]+str(li_name[i])+str(li_titile[i])+str(li_jornal[i])+str(li_volume[i])+str(li_year[i])+str(li_page[i])
        Data_li[i] = result
    
with open("./Output.txt", 'w', encoding='utf-8') as f:
    for lin in Data_li:
        f.write(lin +"\n"+"\n")
      

print(Data_li[1])




# def march_and_add_to_list(str1, star, end, list1):
#     a = 0
#     b = 0
#     len_star = len(star)
#     while str1.find(star, a) != -1:
#         a = str1.find(star, a)
#         b = str1.find(end, a)
#         a = a + len_star
#         result = str1[a:b]
#         if result not in list1:  #多篇参考文献，这种样子：\cite{Young_1985,Khmelnitskaya,Calvo_2014}
#             if len(result.split(","))==1:
#                 list1.append(result)
#             else:
#                 for k in range(len(result.split(","))):
#                     if result.split(",")[k] not in list1:
#                         list1.append(result.split(",")[k])
#     return 0


# if os.path.exists("./参考文献排序结果.txt"):
#     os.remove("./参考文献排序结果.txt")


# path = r"./"
# files_list = os.listdir(path)
# for i in range(0, len(files_list)):
#     if "txt" in str(files_list[i]):
#         file_name = str(files_list[i])  # 自动找到文件名称
# Date_file_path = "./" + file_name
# file_open = open(Date_file_path, "r", encoding="utf-8", errors="ignore")
# lines = file_open.readlines()  # 逐行读取内容形成列表


# star = "cite{"
# end = "}"
# Author_list = []
# Refrence_list = []

# len_lines = len(lines)
# star_lin = 0


# for i in range(0, len_lines):
#     if lines[i].find("begin{thebibliography}") != -1:
#         star_lin = i
#     if lines[i] != "%":  #避免注释的影响
#         march_and_add_to_list(lines[i], star, end, Author_list)
#         # txt1.write(str(Author_list)+"\n")

# with open("./参考文献排序结果.txt", "w", encoding="utf-8") as txt1:
#     for keyword in Author_list:
#         re_bulid_keyword = "\\bibitem{" + keyword + "}"
#         len_re_bulid_keyword = len(re_bulid_keyword)
#         for i in range(star_lin, len_lines):
#             if lines[i].find(re_bulid_keyword) != -1:
#                 targe_lin = lines[i]
#                 txt1.write(str(targe_lin) + "\n")
#                 # Refrence_list.append(targe_lin+'\n')
# txt1.close()



# print((Author_list))
# print("一共有："+str(len(Author_list))+"篇参考文献！")
# print(star_lin, len_lines)
