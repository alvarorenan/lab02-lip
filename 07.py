nome = input("Digite seu nome: ");
nome = "\n" +nome + "\t"
# Basicamente o lsstrip() remove os espaços em branco do início da string, 
# o rstrip() remove os espaços em branco do final da string 
# e o strip() remove os espaços em branco do início e do final da string.

print(nome.lstrip(), nome.rstrip(), nome.strip());

