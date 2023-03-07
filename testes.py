def load_data(file_name):
    with open(file_name) as f:
        # ignorar a primeira linha
        f.readline()
        data = [line.strip().split(";") for line in f]
        return data


data = load_data("ArquivoDadosProjeto.csv")

day_list = []
for line in data:
    informations = (line[1], line[2], line[3],
                    line[4], line[5], line[6], line[7])
    day = [line[0], informations]
    day_list.append(day)


def search_precipitation(year, month):
    result_list = []
    for i in range(len(day_list)):
        if ((day_list[i][0][6:]) == str(year)) and ((day_list[i][0][4:5]) == str(month)):
            result_list.append((day_list[i]))
    print_search_result(result_list)


def print_search_result(result_list):
    for i in result_list:
        print()
        print(i)

# função auxiliar para obter o nome do mês


def get_nome_mes(mes):
    nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return nomes_meses[mes - 1]


# exibindo o menu para o usuário
print("Selecione um mês e um ano:")
print("1 - Janeiro")
print("2 - Fevereiro")
print("3 - Março")
print("4 - Abril")
print("5 - Maio")
print("6 - Junho")
print("7 - Julho")
print("8 - Agosto")
print("9 - Setembro")
print("10 - Outubro")
print("11 - Novembro")
print("12 - Dezembro")

# solicitando ao usuário que selecione um mês
#mes = int(input("Digite o número do mês desejado: "))
mes = 0
while mes < 1 or mes > 12:
    mes = int(input("Digite o número do mês desejado: "))
    if mes < 1 or mes > 12:
        print("Valor inválido! Tente novamente.")


# solicitando ao usuário que insira o ano
ano = int(input("Digite o ano desejado: "))

# exibindo o resultado
print("Você selecionou o mês de", get_nome_mes(mes), "de", ano)

search_precipitation(ano, mes)



