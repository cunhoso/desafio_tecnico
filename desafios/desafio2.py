def contar_a(s):
    return s.lower().count('a')

string = input("Digite uma string: ")
quantidade = contar_a(string)
print(f"A letra 'a' ocorre {quantidade} vezes na string.")
