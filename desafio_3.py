import json

def processar_faturamento(dados):
    valores = [] #Lista vazia
    
    # Loop para extrair os valores de faturamento e ignorar os valores zerados
    for item in dados:
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

# Exemplo de como carregar os dados JSON de um arquivo
with open('dados.json', 'r') as file:
    dados_json = json.load(file)

# Chama a função com os dados JSON
processar_faturamento(dados_json)
