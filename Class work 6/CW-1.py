names = ['Sam', 'Don', 'Daniel']
# def changer(name_list):
#     return hash(name_list)
# res_names = map(changer, names)
res_names = map(lambda x : hash(x), names)
print(list(res_names))