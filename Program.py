# define a função load_data para carregar dados de um arquivo CSV
def load_data(file_name):
    with open(file_name) as f:
        # ignora a primeira linha do arquivo
        f.readline()
        # lê o restante do arquivo e armazena cada linha como uma lista de valores separados por ponto e vírgula
        data = [line.strip().split(";") for line in f]
        # retorna a lista de dados
        return data


# chama a função load_data para carregar os dados do arquivo "ArquivoDadosProjeto.csv" e armazena-os na variável data
data = load_data("ArquivoDadosProjeto.csv")

# cria uma lista vazia day_list para armazenar informações do dia
day_list = []
# para cada linha em data, extrai as informações relevantes e adiciona-as a day_list
for line in data:
    informations = (line[1], line[2], line[3],
                    line[4], line[5], line[6], line[7])
    day = [line[0], informations]
    day_list.append(day)

# define a função search_precipitation para procurar por informações de precipitação de um determinado ano e mês
def print_search_result(result_list):
    for i in result_list:
        print(f"No dia {i[0]} a precipitação foi de: {i[1]}")
        print()

def search_precipitation(year, month):
    result_list = []
    # para cada dia em day_list, verifica se o ano e mês correspondem ao que está sendo procurado e adiciona a correspondência a result_list
    for i in range(len(day_list)):
        if ((day_list[i][0][6:]) == str(year)) and ((day_list[i][0][4:5]) == str(month)):
            result_list.append((day_list[i][0],day_list[i][1][0]))
    # chama a função print_search_result para exibir os resultados
    print_search_result(result_list)

# define a função auxiliar get_nome_mes para obter o nome do mês correspondente a um número de mês


def get_nome_mes(mes):
    nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return nomes_meses[mes - 1]

# define a função print_search_result para imprimir os resultados de pesquisa


def print_resultado_pesquisa_temperatura(result_list):
    cont = 0
    cont_meses = 2
    print("Janeiro")
    for i in result_list:
        if i[0][:2] == "07" and i[0][3:5] == "12": 
            print(f"No dia {i[0]} a temperatura foi {i[1]} C")
            break
        print(f"No dia {i[0]} a temperatura foi {i[1]} C")
        cont += 1
        if cont == 7:
            print(get_nome_mes(cont_meses))
            cont = 0
            cont_meses += 1

def opcao_precipitação():

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

    # solicita ao usuário que selecione um mês e verifica se a entrada é válida
    mes = 0
    while mes < 1 or mes > 12:
        mes = int(input("Digite o número do mês desejado: "))
        if mes < 1 or mes > 12:
            print("Valor inválido! Tente novamente.")

    # solicita ao usuário que insira um ano
    ano = int(input("Digite o ano desejado: "))
    # exibindo o resultado
    print("Você selecionou o mês de", get_nome_mes(mes), "de", ano)
    search_precipitation(ano, mes)

def busca_temperatura_maxima():
    
    ano = input("Digite o ano que você quer buscar: ")
    
    dias = "01,02,03,04,05,06,07"
    meses = "01,02,03,04,05,06,07,08,09,10,11,12"
    result_list = []
    # para cada dia em day_list, verifica se o ano e mês correspondem ao que está sendo procurado e adiciona a correspondência a result_list
    for i in range(len(day_list)):
        if (day_list[i][0][6:]) == str(ano) and (day_list[i][0][4:5] in meses) and (day_list[i][0][:2] in dias):
            result_list.append((day_list[i][0], day_list[i][1][1]))
    # chama a função print_search_result para exibir os resultados
    print_resultado_pesquisa_temperatura(result_list)


# exibe o menu para o usuário

print("O que você gostaria de pesquisar?")

op = 0
while True:
    print("1 para precipitação de um determinado mês de um determinado ano.")
    print("2 para pesquisa de temperaturas máximas nos primeiros 7 dias de cada mês em um ano.")
    op = int(input())
    if op != 1 and op != 2:
        print("Opção inválida. Tente novamente.")
    else:
        break

if op == 1:
    opcao_precipitação()
    
if op == 2:
    busca_temperatura_maxima()


