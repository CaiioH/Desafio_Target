
def pertence_fibo(funcao): #Decorador 
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs) #executa a função
        if numero in resultado:
            print('Este número faz parte da sequencia de fibonacci! ')
        else:
            print('Este número não faz parte da sequencia de fibonacci! ')
        
    return envelope
        
    
@pertence_fibo
def fibonacci(n): #Função
    contagem = 0 #contagem 
    c = [] #lista vazia
    f = 0 #fibonacci
    while contagem != n: #Enquanto a contagem for diferente do numero digitado pelo usuário
        if len(c) >= 2: #se a quantidade da lista for igual a 2: 
            f = (c[-1]) + (c[-2]) #fibonacci recebe o ultimo indice da lista + o penultimo indice da lista
        else: #se não
            f = contagem #fibonacci recebe o valor da contagem
        c.append(f) #adiciona o valor de fibonacci na lista
        contagem +=1 #contagem recebe +1
        print(f'{f}', end=" ➜ ")  #mostra a sequencia
    print('Fim.')
    return c #retorna para poder usar no decorador (pertence_fibo)

    
numero = eval(input('Número: ')) #usuario digita um numero
fibonacci(numero) #Executa a função com o valor digitado pelo usuario
