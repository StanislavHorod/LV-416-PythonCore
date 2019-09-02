try:
    name_list = ("Lubov", "Natalia", "Vira", "Nadia")
    name_list = list(name_list)
    parse_names = []
    changer = []

    for j in range(len(name_list)):
        parse_names = list(name_list[j])
        print(" ")
        for q in range(len(parse_names)):
            changer = list(parse_names[q])
            print(changer, end="#")
except IndexError as ind:
        print(ind)