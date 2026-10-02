nome = input("Digite o nome: ")
senha = input("Digite sua senha: ")
senha_cadastrada = '123'
nome_cadastrado = 'gabriel'

while senha != senha_cadastrada or nome != nome_cadastrado:
    print("Nome ou senha incorreto! Tente novamente.")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

print(f"{nome}, Bem vindo ao sistema...")