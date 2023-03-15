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

    def get_nome_mes(mes):
        nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                       "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        # retorna o nome do mês correspondente ao número passado como parâmetro, subtraindo 1 para ajustar ao índice da lista.
        return nomes_meses[mes - 1]

def precipitacao_acumulada_decadas():
    
    def print_resultado_precipitacao_acumulada():
        for chave in dicionario:
            print(f"Na {chave}, a precipitação foi de {dicionario[chave]} mm")
    
    dicionario = {}

    anos_decada_1 = ["61","62","63","64","65","66","67","68","69","70"]
    anos_decada_2 = ["71", "72", "73", "74", "75", "76", "77", "78", "79","80"]
    anos_decada_3 = ["81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]
    anos_decada_4 = ["91", "92", "93", "94", "95", "96", "97", "98", "99", "00"]
    anos_decada_5 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
    anos_decada_6 = ["11","12","13","14","15","16"]

    for day in day_list:
        ano = day[0][8:]
        if ano in anos_decada_1:chave_dicionario = "Decada 1"
        elif ano in anos_decada_2:chave_dicionario = "Decada 2"
        elif ano in anos_decada_3:chave_dicionario = "Decada 3"
        elif ano in anos_decada_4:chave_dicionario = "Decada 4"
        elif ano in anos_decada_5:chave_dicionario = "Decada 5"
        else: chave_dicionario = "Decada 6"
        precipitacao_hoje = float(day[1][0])
        dicionario[chave_dicionario] = (dicionario.get(chave_dicionario, 0) + precipitacao_hoje)
        

    for chave in dicionario:
        if chave == "Decada 6": anos = len(anos_decada_6)
        else: anos = 10
        dicionario[chave] /= anos
        dicionario[chave] = round(dicionario[chave],1)
        
        
    print_resultado_precipitacao_acumulada()

precipitacao_acumulada_decadas()
#Década 1: 1961 - 1970
#Década 2: 1971 - 1980
#Década 3: 1981 – 1990
#Década 4: 1991 – 2000
#Década 5: 2001 – 2010
#Década 6: 2011 – 2016
