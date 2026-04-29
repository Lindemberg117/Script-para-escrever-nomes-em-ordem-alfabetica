#Script para escrever nomes em ordem alfabetica

#print('Digite os nomes separados por espaços: ')
print("Script para escrever nomes em ordem alfabetica")
#input recebe os nomes, split divide em lista , sorted organiza
#nomes = sorted(input().split(), key=str.lower)

with open('nomes.txt', 'r') as content:
  nomes = sorted(content.readlines(), key=str.lower)
print("\nLista organizada: ")
cont = 1
for name in nomes:
  print(cont, name)
  cont+=1