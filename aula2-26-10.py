# comando input(): permite que
# usuário digite algo.
nome = input("Digite seu nome:\n");

idade = int(input("Digite sua idade:\n"))
print("Seu nome é {} e sua idade é {}".format(nome, idade))

dobro = idade*2;

a = input("O dobro da sua idade é "+str(dobro)+"? s/n \n");



if(a=="s"):
  print("Ao menos sabe matematica e é atento.")

else:
  print("Ou você não sabe multiplicar por 2 ou faltou com atenção. Mais atenção")


