from funcoes import carregar_usuario, salvar_usuario, validar_email, buscar_usuario_por_email

def menu():
    while True:
        print("\n--- SISTEMA DE CADASTRO ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Todos")
        print("3. Buscar por E-mail")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = carregar_usuario()
            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()

            sucesso, mensagem = validar_email(email, usuario)
            if not sucesso:
                print(f"Erro: {mensagem}")
                continue
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("Erro: Idade deve ser um número!")
                continue

            novo_usuario = {"nome": nome, "email": email, "idade": idade}
            usuario.append(novo_usuario)
            salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            usuario = carregar_usuario()
            if not usuario:
                print("Nenhum usuário cadastrado.")
            for i, u in enumerate(usuario, 1):
                print(f"{i}, {u["nome"]} ({u["email"]}) - {u["idade"]} anos")
        elif opcao == "3":
            email_buscar = input("Digite o e-mail para buscar: ").strip()
            resultado = buscar_usuario_por_email(email_buscar)
            if resultado:
                print(f"\nUsuário Encontrado:\nNome: {resultado['nome']}\nIdade: {resultado['idade']}")
            else:
                print("Usuário não encontrado.")
        
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
