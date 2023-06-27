import random 
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^()-_=-+][]{}/:<>?"

while True:
    try:
        
        len = int(input("Tamanho da senha: "))
        quantidade = int(input("Quantidade de Senhas? : ") )
    
    except ValueError:
        print("Entrada invalida!")
    
    else:
            for x in range (0,quantidade):
                senha = ""
                for x in range(0,len):
                    passchar = random.choice(char)
                    senha = senha + passchar
                print("Senha gerada",senha)
            
            break
