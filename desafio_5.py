# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
    # a) Essa string pode ser informada através de qualquer entrada de sua 
#   preferência ou pode ser previamente definida no código;
    # b) Evite usar funções prontas, como, por exemplo, reverse;
    
def Lista(f):
    frase_invertida = ""
    for palavra in range(len(f)-1, -1, -1):
        frase_invertida += f[palavra]
       
    print("String original:", f)
    print("String invertida:", frase_invertida)
            
  
frase = input()
Lista(frase)

