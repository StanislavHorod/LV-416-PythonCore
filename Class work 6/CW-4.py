km_list = [1, 2, 3, 4, 5]
# def convertor(resources):
#     return resources*1.6
# miles_list = map(convertor, km_list)

miles_list = map(lambda x: x*1.6, km_list)