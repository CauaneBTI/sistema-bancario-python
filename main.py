class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_VALOR = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.LIMITE_VALOR:
            print("Valor excede o limite por saque.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido.")

    def mostrar_extrato(self):
        print("\n========== EXTRATO ==========")
        print("Não houve movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=============================")


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"

    def criar_usuario(self):
        cpf = input("CPF: ")

        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("Usuário já existe.")
                return

        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")

        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)

        print("Usuário criado com sucesso!")

    def criar_conta(self):
        cpf = input("CPF do usuário: ")

        usuario = None
        for u in self.usuarios:
            if u.cpf == cpf:
                usuario = u

        if usuario:
            numero_conta = len(self.contas) + 1
            conta = Conta(self.agencia, numero_conta, usuario)
            self.contas.append(conta)
            print("Conta criada com sucesso!")
        else:
            print("Usuário não encontrado.")

    def listar_contas(self):
        for conta in self.contas:
            print(f"""
Agência: {conta.agencia}
Conta: {conta.numero_conta}
Titular: {conta.usuario.nome}
""")


def menu():
    return input("""
========= MENU =========

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair

=> """)


banco = Banco()

while True:

    opcao = menu()

    if opcao == "nu":
        banco.criar_usuario()

    elif opcao == "nc":
        banco.criar_conta()

    elif opcao == "lc":
        banco.listar_contas()

    elif opcao == "d":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor do depósito: "))

        conta = banco.contas[numero - 1]
        conta.depositar(valor)

    elif opcao == "s":
        numero = int(input("Número da conta: "))
        valor = float(input("Valor do saque: "))

        conta = banco.contas[numero - 1]
        conta.sacar(valor)

    elif opcao == "e":
        numero = int(input("Número da conta: "))
        conta = banco.contas[numero - 1]
        conta.mostrar_extrato()

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
