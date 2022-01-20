"""
Tipo Booleano
Algebra Booleana, 2 constantes: verdadeiro ou falso
True --> Verdadeiro
False --> Falso

"""
print("\nTrue ou False:")
ativo = False
outro = True

print(ativo)
print(outro)

"""
Operações básicas
"""

#Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado, e falso será verdadeiro
"""
print("\nOperação not:")
print(not ativo)
print(not outro)

#Ou (or)
"""
É uma operação binária, ou seja, dependendo de 2 valores. Ou um ou outro deve ser verdadeiro
True or True ---> True
True or False ---> True
False or True ---> True
False ou False ---> False"""
verdadeiro = True
falso = False

print("\nOperação Ou (or):")
print(verdadeiro or verdadeiro)
print(verdadeiro or falso)
print(falso or verdadeiro)
print(falso or falso)

# E (and):
"""
Depende de dois valores, ambos verdadeiros
True or True ---> True
True or False ---> False 
False or True ---> False
False ou False ---> False
"""

print("\nOperação E (and):")
print(verdadeiro and verdadeiro)
print(verdadeiro and falso)
print(falso and verdadeiro)
print(falso and falso)
