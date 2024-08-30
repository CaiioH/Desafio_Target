import json

def processar_faturamento(dados_json):
    # Carregar os dados do JSON
    dados = json.loads(dados_json)
    
    # Inicializar listas para armazenar os valores de faturamento
    valores = []
    
    # Loop para extrair os valores de faturamento, ignorando valores zero
    for item in dados["faturamento"]:
        valor = item["valor"]
        if valor > 0:
            valores.append(valor)
    
    # Verifica se há valores para evitar divisão por zero
    if not valores:
        print("Não há dados de faturamento válidos.")
        return
    
    # Inicializa variáveis para o menor e maior valor de faturamento
    menor_valor = valores[0]
    maior_valor = valores[0]
    
    # Loop para calcular o menor e o maior valor
    for valor in valores:
        if valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor
    
    # Calcula a média mensal
    soma_valores = sum(valores)
    quantidade_dias = len(valores)
    media_mensal = soma_valores / quantidade_dias
    
    # Conta os dias com faturamento acima da média
    dias_acima_media = 0
    for valor in valores:
        if valor > media_mensal:
            dias_acima_media += 1
    
    # Mostra os resultados
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# Exemplo de dados JSON 
#(em uma aplicação real, poderia ler isso de um arquivo)
dados_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 1500},
        {"dia": 2, "valor": 2000},
        {"dia": 3, "valor": 0},
        {"dia": 4, "valor": 1800},
        {"dia": 5, "valor": 0},
        {"dia": 6, "valor": 0},
        {"dia": 7, "valor": 2500}
    ]
}
'''

# Chama a função com os dados JSON
processar_faturamento(dados_json)