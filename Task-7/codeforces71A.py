string='localization is good but internationalization is better'
list=string.split(' ')
# print(list)
new_list=[]
for i in list:
    if len(i)>10:
        k=i[0]+str(len(i)-2)+i[-1]
        new_list.append(k)
    else:
        new_list.append(i)
print(new_list)
