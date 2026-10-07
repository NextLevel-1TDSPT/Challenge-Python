# Projeto: NextLevel - Challenge Turma do Bem
# Programa com menu para orientar quem quer ajudar a Turma do Bem

while True:
    # ---------- MENU PRINCIPAL ----------
    print("\n===== TURMA DO BEM =====")
    print("\nDigite uma opção de contato:")
    print("1 - Quero ajudar")
    print("2 - Preciso de ajuda")
    print("3 - Contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao.isdigit():
        opcao = int(opcao)

        match opcao:
            case 1:
                print("\nComo você pode ajudar?")
                print("1 - Doar rápido via Pix e demais formas")
                print("2 - Doar pela Nota Fiscal Paulista")
                print("3 - Quero ser um dentista voluntário ou voluntário de outra especialidade")
                print("0 - Voltar ao menu principal")

                forma = input("Escolha: ")

                match forma:
                    case "1":
                        print("Hoje nós contamos com algumas formas de doação que podem ser acessadas em uma plataforma externa. É rápido, fácil e seguro. Acesse: https://bit.ly/3VCbkI6")

                    case "2":
                        print("Cadastre a Turma do Bem na Nota Fiscal Paulista.")
                        print("Entenda os passos em: https://bit.ly/3VxBvzK")

                    case "3":
                        print("\nComo você pode se voluntariar?")
                        print("1 - Sou dentista e quero fazer parte da turma do bem")
                        print("2 - Sou profissional de outra área e quero fazer parte da turma do bem")
                        print("0 - Voltar")

                        voluntario = input("Escolha: ")

                        match voluntario:
                            case "1":
                                print("Acesse e conheça todos os passos aqui: https://bit.ly/4hKyrb0")
                            case "2":
                                print("Para outras especialidades entre em contato pelo e-mail faleconosco@tdb.org.br")
                            case "0":
                                print("Voltando...")
                            case _:
                                print("Opção inválida. Digite apenas números.")

                    case "0":
                        print("Voltando ao menu principal...")

                    case _:
                        print("Opção inválida. Digite apenas números.")

            # ---------- OPÇÃO 2: PRECISO DE AJUDA ----------
            case 2:
                nome = input("\nQual o seu nome? ")
                idade = input("\nQual a sua idade? ")

                if idade.isdigit():
                    idade = int(idade)
                    # Regra de negócio: A ong atende pessoas em vulnerabilidade sócio econömica entre 11 e 17 anos
                    if idade <= 17 and idade >= 11:
                        print(f"Olá, {nome} com {idade} anos, você pode receber tratamentos pela ong entre em contato pelo site https://turmadobem.org.br/contato/")
                    else:
                        print(f"Infelizmente {nome} com {idade} anos, não é possível se cadastrar no programa. Atendemos apenas na faixa de 11 a 17 anos")
                else:
                    print("Idade inválida! Digite apenas números.")

            # ---------- OPÇÃO 3: Contato ----------
            case 3:
                nome = input("\nQual é o seu nome? ")
                telefone = input("\nQual é o seu telefone? ")
                mensagem = input("Escreva sua mensagem: ")
                print(f"Obrigado, {nome}! Recebemos sua mensagem \"{mensagem}\". Caso necessite de uma resposta entraremos em contato em breve.")

            # ---------- OPÇÃO 4: SAIR ----------
            case 4:
                print("Obrigado por visitar a Turma do Bem. Até logo!")
                break

            # Qualquer outro número
            case _:
                print("Opção inválida! Escolha de 1 a 4.")

    else:
        # programa volta ao menu
        print("Opção inválida! Digite apenas números.")