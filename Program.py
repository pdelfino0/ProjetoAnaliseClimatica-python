def load_data(file_name):
    with open(file_name) as f:
        f.readline()  # ignorar a primeira linha
        data = [line.strip().split(";") for line in f]
        return data


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


data = load_data("ArquivoDadosProjeto.csv")

day_list = []
for line in data:
    informations = (line[1], line[2], line[3],
                    line[4], line[5], line[6], line[7])
    day = [line[0], informations]
    day_list.append(day)


def seach_precipitation(year, month):
    result_list = []
    for i in range(len(day_list)):
        if ((day_list[i][0][6:]) == str(year)) and ((day_list[i][0][4:5]) == str(month)):
            # print((day_list[i][0][6:]))
            result_list.append((day_list[i]))
    print_search_result(result_list)


def print_search_result(result_list):
    for i in result_list:
        print()
        print(i)


teste = seach_precipitation(1961, 4)
print(teste)
