# CeWL

![descrição do desafio](https://github.com/tom-xs/CTF_notes/blob/master/sqrt-i/14-01-2021/Cewl%20challenge.PNG)

seguindo a diga que o nome do desafio nos da encontramos o repositorio para [CeWL](https://github.com/digininja/CeWL), um programa que retira possiveis palavras chaves de um site.
Peguei palavras chaves com tamanho maior que 12 e adicionei "surgeon" ao final delas. Apos isso encriptei todas em sha256 e procurei qual palavra correspondia ao sha256 mostrado
```86515c560fe63bb69f89661e9c6a9a0b5f9a79703af9ddf5eee6e27a117ea1e1``` que resultou em ```Revascualrisationsurgeon```
