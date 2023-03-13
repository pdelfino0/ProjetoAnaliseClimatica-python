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


'''dic= {}
#for i in day_list:
    ano = day_list[0][0][6:]
    mes = day_list[0][0][3:5]
    day_precipitation = day_list[0][1][1]
    dic_Index = ano + "/" + mes
    dic.get
    dic[dic_Index] = 

print(day_list[0][0][6:])
print(day_list[0][0][3:5])
print(day_list[0][1][1])
'''

dic = {'marco/2023': 220}
print(dic.get('marco/2023',0))