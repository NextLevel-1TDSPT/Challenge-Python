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
                print("\nA ONG Turma do Bem oferece ajuda à pessoas em situação de vulnerabilidade socio-econômica.\n - O programa Dentista do Bem, atende jovens de 11 à 17 anos;\n - O programa Apolônias do Bem, oferece ajuda à mulheres cis e trans vítimas de agressões físicas.")
                nome = input("\nQual o seu nome? ")
                idade = input("\nQual a sua idade? ")
                genero = input("\nQual é o seu gênero?(Digite o número)\n 1- Feminino\n 2- Masculino\n 3- Não-binário\n 4- Outro\n")

                match genero:
                    case "1":
                        genero = "Feminino"
                    case "2":
                        genero = "Masculino"
                    case "3":
                        genero = "Não-binário"
                    case "4":
                        genero = "Outro"
                    case _:
                        print("\nOpção inválida, digite uma das opções.\n")
                        continue

                if idade.isdigit():
                    idade = int(idade)
                    # Regra de negócio: A ong atende pessoas em vulnerabilidade sócio econômica entre 11 e 17 anos
                    if idade <= 17 and idade >= 11:
                        print(f"Olá, {nome} com {idade} anos do gênero {genero}, você pode receber tratamentos pela ong entre em contato pelo site:\n - https://turmadobem.org.br/contato/")

                    elif idade < 11 or idade > 17 and genero == "Feminino":
                        entrar = str(input("O programa Apolônias do Bem, oferece ajuda à mulheres cis e trans vítimas de agressões físicas.\n Gostaria de fazer parte?(sim ou não)? ")).lower()
                        if entrar == "sim":
                            print("Ao entrar em contato com a Tdb pelo WhatsApp 11 98965-8599, será solicitado um B.O. (Boletim de Ocorrência) da agressão sofrida e, posteriormente, ocorrerá uma entrevista e o exame clínico.")
                        elif entrar == "não" or entrar == "nao":
                                print(f"Infelizmente {nome} com {idade} anos do gênero {genero}, não é possível se cadastrar no programa Dentista do Bem. Atendemos apenas na faixa de 11 a 17 anos")
                    else:
                        print(f"Infelizmente {nome} com {idade} anos do gênero {genero}, não é possível se cadastrar no programa Dentista do Bem. Atendemos apenas na faixa de 11 a 17 anos")
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