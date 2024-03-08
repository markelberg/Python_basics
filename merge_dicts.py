dict1 = {
    "nombre": "Pepe",
    "edad": 33,
    "dni": 46565959
}

dict2 = {
    "nacionalidad": "española",
    "lugar de nacimiento": "Madrid"
}

merge_dict = {}
merge_dict.update(dict1)

for key, value in dict2.items():
    merge_dict[key] = value

print(merge_dict)