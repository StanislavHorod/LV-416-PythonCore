colors =  ["red", "green", "black", "red", "brown", "ed", "blue", "red", "red", "yellow" ]

# def filtered(colores):
#     return colores == "red"

# results = filter(filtered, colors)
results = filter(lambda x: x=="red", colors )
print(list(results))