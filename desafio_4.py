# 4) Dado o valor de faturamento mensal de uma distribuidora. 
# detalhado por estado:

    # • SP – R$67.836.43
    # • RJ – R$36.678.66
    # • MG – R$29.229.88
    # • ES – R$27.165.48
    # • Outros – R$19.849.53

# Escreva um programa na linguagem que desejar onde calcule o percentual 
#de representação que cada estado teve dentro do valor total mensal da 
#distribuidora.  

class Estado:
    def __init__(self, nome, faturamento):
        self._nome = nome
        self._faturamento = faturamento
        
    @property
    def nome(self): #pra acessar o nome
        return self._nome
    
    @property
    def faturamento(self): #pra acessar o faturamento
        return self._faturamento
    
    def calc_percentual(self, fatu_total): # pra calcular o percentual do Estado
        percentual = (self.faturamento / fatu_total) * 100
        print(f"Percentual de {self.nome}: {percentual:.2f}%")
        
def calc_fat_total(fat): #pra calcular o faturamento total (soma de todos os estados)
    soma = 0
    for i in fat: #pra cada item, soma o segundo indice do item
        soma += i[1]
    
    print(f'Faturamento total: R${soma} \n')
    return soma
             

def main():
    
    faturamentos = [('SP', 67836.43), ('RJ', 36678.66), ('MG', 29229.88),
    ('ES', 27165.48), ('Outros', 19849.53)]

    fat_total = calc_fat_total(faturamentos)

    for i in faturamentos: #pra cada estado
        estado = Estado(i[0], i[1]) #estado recebe como parametro o primeiro valor do loop com o primeiro indice(nome) e o segundo indice(valor)
        estado.calc_percentual(fat_total)
        
main()