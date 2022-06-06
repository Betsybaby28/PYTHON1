dict1={'id':'1','name':'anu','age':'20'}
print(dict1['name'])
print(dict1['age'])
dict1['place']="kochi"
print(dict1)
dict1['name']="arya"
print(dict1)
del dict1['id']
print(dict1)
dict2={'company':'spectrum','mobile':'55555'}
dict1.update(dict2)
print(dict1)
print('age' in dict1)
dict1.clear()
print(dict1)
del dict2
print(dict2)