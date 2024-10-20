import pandas as pd

# Lista
loja = ['Camisa', 'Calça', 'Jaqueta', 'Vestido', 'Bone']
quantidade = [50, 30, 15, 10, 25]

# Criando serie
pdt = pd.Series(quantidade, index=loja)

loja.append('Blusa')
quantidade.append(20)

# Exibir nova serie
nova = pd.Series(quantidade, index=loja)

#print(nova)

# Selecionando Itens
pdt_maior = pdt[pdt > 20]
#print(pdt_maior)

# Item 4
preco = [3500, 2500, 1200, 900, 1500]
precos = pd.Series(preco, index=pdt)
#print(precos)

# Item 5
## Total com a Blusa
total = (pdt * preco).sum()
print(total)
print(30*'=')

### Total sem a Blusa
total2 = (pdt[:-1] * preco[:-1]).sum()
print(total2)