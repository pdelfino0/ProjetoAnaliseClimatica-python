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

def busca_precipitacao_mensal():
    
    def encontra_mes_mais_chuvoso(precipitacao):
        
        mes_mais_chuvoso = max(precipitacao, key = lambda k: precipitacao[k])
        mes,ano = mes_mais_chuvoso.split("/")
        
        return f"{mes}/{ano}"
        
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

busca_precipitacao_mensal()