from funcoes import carregar_usuario, salvar_usuario, validar_email, buscar_usuario_por_email


def menu():
    while True:
        print("\n--- SISTEMA DE CADASTRO ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Todos")
        print("3. Buscar por E-mail")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            usuarios = carregar_usuario()

            nome = input("Nome: ").strip()
            if not nome:
                print("Erro: Nome não pode ficar vazio!")
                continue

            email = input("E-mail: ").strip()
            sucesso, mensagem = validar_email(email, usuarios)
            if not sucesso:
                print(f"Erro: {mensagem}")
                continue

            try:
                idade = int(input("Idade: "))
                if idade < 0:
                    print("Erro: Idade não pode ser negativa!")
                    continue
            except ValueError:
                print("Erro: Idade deve ser um número!")
                continue

            novo_usuario = {
                "nome": nome,
                "email": email,
                "idade": idade
            }

            usuarios.append(novo_usuario)
            salvar_usuario(usuarios)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            usuarios = carregar_usuario()

            if not usuarios:
                print("Nenhum usuário cadastrado.")
                continue

            print("\n--- LISTA DE USUÁRIOS ---")
            for i, u in enumerate(usuarios, 1):
                print(f"{i}. {u['nome']} ({u['email']}) - {u['idade']} anos")

        elif opcao == "3":
            email_buscar = input("Digite o e-mail para buscar: ").strip()
            resultado = buscar_usuario_por_email(email_buscar)

            if resultado:
                print("\n--- USUÁRIO ENCONTRADO ---")
                print(f"Nome: {resultado['nome']}")
                print(f"E-mail: {resultado['email']}")
                print(f"Idade: {resultado['idade']}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()