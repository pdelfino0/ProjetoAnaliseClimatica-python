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
                print(f"No dia {i[0]} a precipitação foi de: {i[1]} mm")
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
    
def busca_informacoes_auge_inverno():
    
    import statistics
    
    decada_determinada = ["2006", "2007", "2008", "2009",
                        "2010", "2011", "2012", "2013", "2014", "2015", "2016"]

    temp_min = [] # Lista para armazenar as temperaturas mínimas
    um_relativa = []  # Lista para armazenar a umidade relativa do ar
    vel_vento = [] # Lista para armazenar a velocidade do vento

    soma_temp_min = 0.0 # Variável para armazenar a soma das temperaturas mínimas
    soma_vel_vento = 0.0 # Variável para armazenar a soma das velocidades do vento
    soma_um_relativa = 0.0 # Variável para armazenar a soma da umidade relativa do ar
    cont = 0  # Variável para contar o número de dias que correspondem aos critérios de seleção
    
     # Loop para percorrer a lista de dias e extrair as informações relevantes
    for day in day_list:
        ano = day[0][6:]  # extrair o ano da string da data
        mes = day[0][3:5]  # extrair o mês da string da data
        
        # Verifica se o mês é junho e se o ano está na década determinada
        if mes == "06" and ano in decada_determinada:
            temp_min.append((day[1][2]))  # Adiciona a temperatura mínima na lista correspondente
            um_relativa.append((day[1][5])) # Adiciona a umidade relativa do ar na lista correspondente
            vel_vento.append((day[1][6])) # Adiciona a velocidade do vento na lista correspondente

            soma_temp_min +=  float(day[1][2]) # Soma as temperaturas mínimas
            soma_um_relativa += float(day[1][5]) # Soma a umidade relativa do ar
            soma_vel_vento += float(day[1][6]) # Soma as velocidades do vento
            cont += 1 # Incrementa o contador
            
     # Calcula as médias das temperaturas mínimas, umidade relativa do ar e velocidades do vento
    media_temp_min = soma_temp_min / cont
    media_vel_vento = soma_vel_vento / cont
    media_um_relativa = soma_um_relativa / cont

    import statistics

    # Calcula as modas das temperaturas mínimas, umidade relativa do ar e velocidades do vento
    moda_temp_min = statistics.mode(temp_min)
    moda_um_relativa = statistics.mode(um_relativa)
    moda_vel_vento = statistics.mode(vel_vento)
    
    # Imprime as informações na tela
    print(f"A média da temperatura mínima no mês de Junho durante a década de 2006 a 2016 foi de {media_temp_min:2.1f} °C, com moda de {float(moda_temp_min)} °C")
    print(f"A média da umidade relativa do ar no mês de Junho durante a década de 2006 a 2016 foi de {media_um_relativa:2.1f} %, com moda de {float(moda_um_relativa)} %")
    print(f"A média da velócidade do vento no mês de Junho durante a década de 2006 a 2016 foi de {media_vel_vento:2.1f} m/s, com moda de {float(moda_vel_vento):.1f} m/s")

def precipitacao_acumulada_decadas():
    
     # função aninhada para imprimir os resultados
    def print_resultado_precipitacao_acumulada():
        for chave in dicionario:
            print(f"Na {chave}, a precipitação foi de {dicionario[chave]} mm")
            
    # inicializa um dicionário vazio para armazenar a precipitação acumulada por década
    dicionario = {}

    # define listas de anos que pertencem a cada década do período
    anos_decada_1 = ["61","62","63","64","65","66","67","68","69","70"]
    anos_decada_2 = ["71", "72", "73", "74", "75", "76", "77", "78", "79","80"]
    anos_decada_3 = ["81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]
    anos_decada_4 = ["91", "92", "93", "94", "95", "96", "97", "98", "99", "00"]
    anos_decada_5 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
    anos_decada_6 = ["11","12","13","14","15","16"]

    # loop pelos dias na lista de entrada, extrai o ano da data e atribui a década correspondente
    # à variável "chave_dicionario"
    for day in day_list:
        ano = day[0][8:]
        if ano in anos_decada_1:chave_dicionario = "Decada 1"
        elif ano in anos_decada_2:chave_dicionario = "Decada 2"
        elif ano in anos_decada_3:chave_dicionario = "Decada 3"
        elif ano in anos_decada_4:chave_dicionario = "Decada 4"
        elif ano in anos_decada_5:chave_dicionario = "Decada 5"
        else: chave_dicionario = "Decada 6"
        #extrai o valor da precipitação para aquele dia, adiciona ao total de precipitação
        precipitacao_hoje = float(day[1][0])
        #atribui o resultado à chave correspondente no dicionário
        dicionario[chave_dicionario] = (dicionario.get(chave_dicionario, 0) + precipitacao_hoje)
        
    # loop pelas chaves no dicionário e calcula a precipitação média para cada década
    for chave in dicionario:
        if chave == "Decada 6": anos = len(anos_decada_6)
        else: anos = 10
        # dividindo a precipitação total pelo número de anos naquela década (seja 10 ou 6),
        dicionario[chave] /= anos
        # e arredonda o resultado para uma casa decimal
        dicionario[chave] = round(dicionario[chave],1)
        
    #chama a função responsável por imprimir o resultado final em um formato legível para o usuário.
    print_resultado_precipitacao_acumulada()



# Exibe um menu para o usuário escolher qual tipo de pesquisa deseja fazer. 
print("O que você gostaria de pesquisar?")

# O loop while garante que apenas uma opção válida seja selecionada e, em seguida, 
op = 0
while True:
    print("1 para exibir a precipitação de um determinado mês de um determinado ano.")
    print("2 para exibir temperaturas máximas nos primeiros 7 dias de cada mês de um ano.")
    print("3 para exibir o mês mais chuvoso de todo o período.")
    print("4 para exibir informações sobre umidade relativa do ar, temperatura mínima e velocidade do vento na década de 2006 a 2016")
    print("5 para exibir a média de precipitação acumulada anual por décadas")
    
    op = int(input())
    if op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
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
    
if op == 4:
    busca_informacoes_auge_inverno()

if op== 5:
    precipitacao_acumulada_decadas()


