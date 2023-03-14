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
    dia = [line[0], informations]
    day_list.append(dia)

def busca_maior_precipitacao_mensal():
    
    def encontra_mes_mais_chuvoso(precipitacao):
        
        mes_mais_chuvoso = max(precipitacao, key = lambda k: precipitacao[k])
        mes,ano = mes_mais_chuvoso.split("/")
        
        return f"{get_nome_mes(int(mes))}/{ano}"
        
    def precipitacao_mes_mais_chuvoso(precipitacao):
                
        mes_mais_chuvoso = max(precipitacao, key = lambda k: precipitacao[k])
        maior_precipitacao_mensal = precipitacao[mes_mais_chuvoso]
        
        return maior_precipitacao_mensal
    
    dicionario_precipitacao = {}
    for day in day_list:
        ano = day[0][6:] # extrair o ano da string da data
        mes = day[0][3:5] # extrair o mês da string da data
        precipitacao_hoje = float(day[1][0]) # extrair o valor diário de precipitação como um float
        chave_do_dicionario = f"{mes}/{ano}" # criar uma chave no formato "MM/AAAA"
        # usar o método get() para recuperar o valor da chave (se ela existir), ou definir um valor padrão de 0 (se ela não existir), e adicionar o valor diário de precipitação a ele
        dicionario_precipitacao[chave_do_dicionario] = dicionario_precipitacao.get(chave_do_dicionario, 0) + precipitacao_hoje

    mes_mais_chuvoso = encontra_mes_mais_chuvoso(dicionario_precipitacao)
    maior_precipitacao_mensal = precipitacao_mes_mais_chuvoso(dicionario_precipitacao)
    print(f"O mês mais chuvoso de todo o período foi {mes_mais_chuvoso}, com {maior_precipitacao_mensal:5.2f} mm de chuva")

# Define uma função que recebe o número do mês como parâmetro e retorna o nome correspondente.
def get_nome_mes(mes):
    nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return nomes_meses[mes - 1] # retorna o nome do mês correspondente ao número passado como parâmetro, subtraindo 1 para ajustar ao índice da lista.

# Define uma função para imprimir os resultados da pesquisa de temperatura máxima nos primeiros 7 dias de cada mês em um ano específico.
def print_resultado_pesquisa_temperatura(lista_resultante):
    cont = 0 # contador de dias para imprimir o nome do próximo mês após 7 dias
    cont_meses = 2 # contador de meses para imprimir o nome do próximo mês
    print("Janeiro") # imprime o nome do primeiro mês

    # Itera sobre a lista de resultados
    for i in lista_resultante:
        # Verifica se a data corresponde aos primeiros 7 dias do mês atual
        if i[0][:2] == "07" and i[0][3:5] == "12": 
            # Se a data estiver dentro dos primeiros 7 dias do mês atual, imprime a data e a temperatura máxima registrada para essa data
            print(f"No dia {i[0]} a temperatura foi {i[1]} C")
            # Interrompe o loop for se encontrar a primeira data que está fora dos primeiros 7 dias do último mês que está imprimindo
            break
        # Se a data estiver dentro dos primeiros 7 dias do mês atual, imprime a data e a temperatura máxima registrada para essa data
        print(f"No dia {i[0]} a temperatura foi {i[1]} C")
        # Incrementa o contador de dias
        cont += 1
        # Se o contador de dias atingir 7, imprime o nome do próximo mês e redefine o contador de dias para 0
        if cont == 7:
            print(get_nome_mes(cont_meses))
            cont = 0
            # Incrementa o contador de meses
            cont_meses += 1

            
#inicia a pesquisa solicitada
def opcao_precipitação():
    
    #funções alinhadas devem ficar dentro da função principal
    def print_lista_resultante(lista_resultante):
        if len((lista_resultante)) == 0 : print("Não há dados para o período informado.")
        else:
            for i in lista_resultante:
                print(f"No dia {i[0]} a precipitação foi de: {i[1]}")
                print()
        # define a função procura_precipitacao para procurar por informações de precipitação de um determinado ano e mês
        #funções alinhadas devem ficar dentro da função principal
    
    def procura_precipitacao(ano, mes):
        lista_resultante = []
        # para cada dia em day_list, verifica se o ano e mês correspondem ao que está sendo procurado e adiciona a correspondência a lista_resultante
        for i in range(len(day_list)):
            if ((day_list[i][0][6:]) == str(ano)) and ((day_list[i][0][4:5]) == str(mes)):
                lista_resultante.append((day_list[i][0],day_list[i][1][0]))
        # chama a função print_lista_resultante para exibir os resultados
        print_lista_resultante(lista_resultante)


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
    procura_precipitacao(ano, mes)

# Define uma função que busca as temperaturas máximas para os primeiros 7 dias de cada mês em um determinado ano.
def busca_temperatura_maxima():
    
    # A função recebe um ano como entrada do usuário e cria duas strings, dias e meses, que contêm os dias e meses a serem pesquisados. 
    ano = input("Digite o ano que você quer buscar: ")
    
    dias = "01,02,03,04,05,06,07"
    meses = "01,02,03,04,05,06,07,08,09,10,11,12"
    lista_resultante = []
    
    # Um loop for é usado para verificar se a data correspondente em day_list (uma lista de tuplas contendo datas e temperaturas) atende aos critérios de busca.
    # para cada dia em day_list, verifica se o ano e mês correspondem ao que está sendo procurado e adiciona a correspondência a lista_resultante
    for i in range(len(day_list)):
        # Se a data corresponder aos critérios, ela é adicionada a uma lista de resultados.
        if (day_list[i][0][6:]) == str(ano) and (day_list[i][0][4:5] in meses) and (day_list[i][0][:2] in dias):
            lista_resultante.append((day_list[i][0], day_list[i][1][1]))
            
    # Por fim, a função chama outra função para imprimir os resultados da pesquisa.
    print_resultado_pesquisa_temperatura(lista_resultante)



# Exibe um menu para o usuário escolher qual tipo de pesquisa deseja fazer. 
print("O que você gostaria de pesquisar?")

# O loop while garante que apenas uma opção válida seja selecionada e, em seguida, 
op = 0
while True:
    print("1 para precipitação de um determinado mês de um determinado ano.")
    print("2 para pesquisa de temperaturas máximas nos primeiros 7 dias de cada mês em um ano.")
    print("3 para descobrir o mês mais chuvoso de todo o período.")
    op = int(input())
    if op != 1 and op != 2 and op != 3:
        print("Opção inválida. Tente novamente.")
    else:
        break

# chama a função correspondente com base na escolha do usuário.

if op == 1:
    opcao_precipitação()
    
if op == 2:
    busca_temperatura_maxima()
    
if op == 3:
    busca_maior_precipitacao_mensal()
        


