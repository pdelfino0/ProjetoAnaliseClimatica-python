import matplotlib.pyplot as plt




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
    return dicionario

dicionario_precipitacao_acumulada = precipitacao_acumulada_decadas()

valores = [ valor for valor in dicionario_precipitacao_acumulada.values()]
decadas = [chave for chave in dicionario_precipitacao_acumulada]

plt.bar(decadas,valores)
plt.show()


