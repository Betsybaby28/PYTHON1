str1="hello world"
print(str1.upper())
str2="HELLO WORLD"
print(str2.lower())
print(str1.title())
print(str1.capitalize())
print(str1.startswith('h'))
print(str1.startswith('e'))
print(str1.endswith('d'))
print(str1.endswith('r'))
print(str1.isdigit())
str3="444"
print(str3.isdigit())
str4="d3"
print(str4.isdigit())
print(str1.isalpha())
print(str3.isalpha())
print(str1.isspace())
str5="     "
print(str5.isspace())
print(str1.replace('h','w'))
print(str1.split())
print(str3.split())
print(str1.strip())
str6="    hello     "
print(str6.strip())
str7="%%%friends%%%"
print(str7.strip('%'))
print(str6.rstrip())
print(str7.lstrip('%'))
str8="hello world welcome"
print(str8.split())
print(str8.replace('o','m'))
str9="ddi"
print(str9.isalpha())
print(len(str9))