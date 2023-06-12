print("Seja bem vindo ao quiz do léo xD")
answer_user = input("Quer começar? (digite s/n)")

if answer_user != "s":
    quit()

score = 0

print("começando...")
print("Você tem alguma ideia do que é python? \n (a) Sim \n (b) Não \n (c) âãÂÃA?\n")
answer_1 = input("resposta: ")

if answer_1 == "c":
    print("Boa caraai")
    score = score + 1
else:
    print("que merda em cara, errou")

print(
    "Você quer me pagar um lanche? \n (a) Sim \n (b) Não \n (c) Sai daqui seu gordo!\n"
)
answer_1 = input("resposta: ")

if answer_1 == "c":
    print("Boa caraai")
    score = score + 1
else:
    print("que merda em cara, errou")

print(
    "Eu vim da bahia meu nome é ninguem, quem te comeu? \n (a) Seu pai \n (b) ninguem \n (c) Um cachorro\n"
)
answer_1 = input("resposta: ")

if answer_1 == "b":
    print("Boa caraai")
    score = score + 1
else:
    print("que merda em cara, errou")

print(
    "Você quer sair desse troço? \n (a) Sim \n (b) Não \n (c) resposta a na alternativa c... q?\n"
)
answer_1 = input("resposta: ")

if answer_1 == "c":
    print("Boa caraaai")
    score = score + 1
else:
    print("que merda em cara, errou")

print(f"chega de perguntas... sua pontuação é {score}/4")
