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


decada_determinada = ["2006", "2007", "2008", "2009",
                      "2010", "2011", "2012", "2013", "2014", "2015", "2016"]

temp_min = []
um_relativa = []
vel_vento = []

soma_temp_min = 0.0
soma_vel_vento = 0.0
soma_um_relativa = 0.0
cont = 0
for day in day_list:
    ano = day[0][6:]  # extrair o ano da string da data
    mes = day[0][3:5]  # extrair o mês da string da data
    if mes == "06" and ano in decada_determinada:
        temp_min.append((day[1][2]))
        um_relativa.append((day[1][5]))
        vel_vento.append((day[1][6]))

        soma_temp_min = soma_temp_min + float(day[1][2])
        soma_um_relativa = soma_um_relativa + float(day[1][5])
        soma_vel_vento = soma_vel_vento + float(day[1][6])
        cont += 1

media_temp_min = soma_temp_min / cont
media_vel_vento = soma_vel_vento / cont
media_um_relativa = soma_um_relativa / cont
print(f"{media_temp_min:5.1f}C")
print(f"{media_vel_vento:5.1f}")
print(f"{media_um_relativa:5.1f}")
