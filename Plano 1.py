loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print("Where are you?")
    
###########################################################

a = 3
b = 6
c = 9

if (a + b >= c) and (a + c >= b) and (b + c >= a):
    print('Triângulo Válido')
else:
    print('Triângulo é inválido')

###########################################################

l = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in l:
    list_sum += num
print(list_sum)

###########################################################

s = 'Hello Python'
for i in s[6:]:
    print(i)
    
############ muito bom ####################################

x = 0
while x < 10:
    print('x atualmente: ', x)
    print(' x continua menor que 10, adicionando 1 ao x')
    x += 1
else:
    print('Tudo certo!!!')

############### DESENHO #############################################

x = 0
while x < 11:
    print('*' * x)
    x += 1
while x > 0:
    print('*' * x)
    x -= 1

################# EXEMPLO DO USO DE RANGE  #########################

for i in range(1,51):
    if i % 2 == 0 and i % 5 ==0:
        print(i,'- Múltiplo de 2 e 5')
    elif i % 2 == 0:
        print(i, '- Múltiplo de 2')
    elif i % 5 == 0:
        print(i, '- Múltiplo de 5')
    else:
        print(i, '- Não é múltiplo de 2 ou 5')

########################## SOMAS com imput #########################

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
soma = a + b
print("A soma de", a, "+", b, "é igual a", soma)

####################################################################

def cumprimento(nome):
    print('Olá , %s' %nome)
cumprimento('Luiz')

################# Checar numero primo ################################

def is_prime(num):
    '''
    Metódo para checar se é primo
    '''
    for n in range(2,num):
        if num % n == 0:
            print('Não é primo')
            break
        else:
            print("Primo")
is_prime(3)

###################### Converter segundos ############################

segundos_str = input("Por gentileza, insira o valor em segundos que deseja converter: ")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos =  segs_restantes // 60
segs_restantes_final = segs_restantes  % 60

print("Horas=", horas, "minutos=", minutos, "segundos=", segs_restantes_final)

###################### area de um circulo #############################

raio_1 = input("Insira o valor do raio: ")
raio = int(raio_1) ** 2
area = 3.14 * raio

print (area)

####################### area de um retangulo ############################

base = input('Insira o valor da base: ')
altura = input('Agora insira o valor da altura: ')

area = int(base) * int(altura)

print (area)

###################### KM por litro ######################################

km = input('Insira os quilometros percorridos: ')
litros = input('Agora insira os litros de gasolina consumidos: ')
km_por_litro = int(km) / int(litros)

print (km_por_litro)

######################## Converter Celsius em Fahrenheit #################

celsius = input('Para a conversão ,insira a temperatura em CELSIUS: ')
fahrenheit = int(celsius) / int(5) * int(9) + int(32)

print (fahrenheit)
