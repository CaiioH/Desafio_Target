# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def resumo(funçao):
    def envelope(*args, **kwargs):
        resultado = funçao(*args, **kwargs)
        
        if resultado == 0:
            print('A frase não contém a letra "A". ')
        else:
            print(f'A letra "A" aparece {resultado} vezes na frase.')
    return envelope       
        
@resumo
def encontra_a(f):
    qt_a = 0
    for letra in f:
        if letra == 'a' or letra == 'A':
            qt_a += 1
    return qt_a
            
            
frase = input()
print(frase)
encontra_a(frase)        
        