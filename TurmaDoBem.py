# Projeto: NextLevel - Challenge Turma do Bem
# Programa com menu para orientar quem quer ajudar a Turma do Bem


# Exibe as opções para quem deseja ajudar a ONG.
def quero_ajudar():
    while True:
        print("\nComo você pode ajudar?")
        print("1 - Doar via Pix e demais formas")
        print("2 - Doar pela Nota Fiscal Paulista")
        print("3 - Quero ser voluntário")
        print("0 - Voltar ao menu principal")

        # Recebe a opção escolhida pelo usuário.
        forma = input("Escolha: ").strip()

        # Executa a ação correspondente à opção escolhida.
        match forma:
            case "1":
                registrar_doacao()
                return

            case "2":
                print("\nCadastre a Turma do Bem na Nota Fiscal Paulista.")
                print("Entenda os passos em: https://bit.ly/3VxBvzK")
                voltar()
                return

            case "3":
                voluntariado()
                return

            case "0":
                voltar()
                return

            # Executado quando a opção não corresponde às disponíveis.
            case _:
                opcao_invalida()
                continue


# ---------- REGISTRO DE DOAÇÕES ----------

# Lista que armazena temporariamente os registros de doação.
doacoes = []


# Solicita os dados do doador e registra sua intenção de doação.
def registrar_doacao():
    print("\n===== REGISTRO DE DOAÇÃO =====")

    # Solicita o nome e impede que fique vazio ou contenha apenas números.
    while True:
        nome = input("Nome do doador: ").strip()

        if nome == "" or nome.isdigit():
            print("Nome inválido. Digite seu nome corretamente.")
        else:
            break

    # Valida se o CPF contém 11 números e não é formado por um único dígito repetido.
    while True:
        cpf = input("CPF do doador (Somente números): ").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido. Digite os 11 números do CPF.")
        elif cpf == cpf[0] * 11:
            print("CPF inválido.")
        else:
            break

    # Solicita um valor numérico maior que R$ 5,00.
    while True:
        valor = input("Quanto deseja doar (R$): ").strip()

        if not valor.isdigit():
            print("Valor inválido. Digite um valor numérico.")
            continue

        # Converte o valor informado para o tipo numérico float.
        valor = float(valor)

        if valor <= 5:
            print("O valor deve ser maior que R$ 5,00.")
        else:
            break

    # Agrupa os dados da doação em um dicionário.
    doacao = {
        "nome": nome,
        "cpf": cpf,
        "valor": valor
    }

    # Adiciona o registro à lista de doações.
    doacoes.append(doacao)

    # Exibe os dados registrados e o link para realizar a doação.
    print("\nIntenção de doação registrada com sucesso!")
    print(f"Nome: {nome}")
    print(f"Valor: R$ {valor:.2f}")
    print("Acesse a plataforma para realizar sua doação:")
    print("https://bit.ly/3VCbkI6")

    voltar()


# Exibe as opções disponíveis para quem deseja ser voluntário.
def voluntariado():
    while True:
        print("\nComo você pode se voluntariar?")
        print("1 - Sou dentista e quero fazer parte da Turma do Bem")
        print("2 - Sou profissional de outra área")
        print("0 - Voltar ao menu principal")

        # Recebe a opção escolhida pelo usuário.
        voluntario = input("Escolha: ").strip()

        # Direciona o usuário conforme a opção escolhida.
        match voluntario:
            case "1":
                print("\nConheça todos os passos:")
                print("https://bit.ly/4hKyrb0")
                voltar()
                return

            case "2":
                print("\nEntre em contato pelo e-mail:")
                print("faleconosco@tdb.org.br")
                voltar()
                return

            case "0":
                voltar()
                return

            # Solicita uma nova opção quando a entrada é inválida.
            case _:
                opcao_invalida()
                continue


# Consulta os registros de doação usando o nome e o CPF.
def consultar_doacoes():
    print("\n===== CONSULTAR DOAÇÕES =====")

    # Solicita o nome informado no cadastro.
    nome = input("Digite seu nome: ").strip()

    # Valida o formato do CPF antes de realizar a consulta.
    while True:
        cpf = input("Digite seu CPF (Somente números): ").strip()

        if cpf.isdigit() and len(cpf) == 11 and cpf != cpf[0] * 11:
            break

        print("CPF inválido. Digite os 11 números do CPF.")

    # Cria uma lista para armazenar os registros que correspondem aos dados informados.
    encontradas = []

    # Percorre os registros e compara nome e CPF.
    for doacao in doacoes:
        if doacao["nome"].lower() == nome.lower() and doacao["cpf"] == cpf:
            encontradas.append(doacao)

    # Exibe os registros encontrados e calcula o valor total.
    if encontradas:
        print(f"\nRegistros encontrados para {nome}:")

        total = 0

        # Numera os registros e soma os valores das doações.
        for i, doacao in enumerate(encontradas, start=1):
            print(f"\nRegistro {i}")
            print(f"Valor: R$ {doacao['valor']:.2f}")
            total += doacao["valor"]

        print(f"\nTotal registrado: R$ {total:.2f}")

    # Informa quando não existem registros correspondentes.
    else:
        print("\nNenhum registro encontrado para esses dados.")

    voltar()


# Coleta os dados de quem procura ajuda e identifica o programa adequado.
def preciso_de_ajuda():
    print("\nA ONG Turma do Bem oferece ajuda a pessoas em situação")
    print("de vulnerabilidade socioeconômica.")
    print("- Dentista do Bem: jovens de 11 a 17 anos.")
    print("- Apolônias do Bem: mulheres cis e trans vítimas de")
    print("  agressões físicas.")

    # Solicita um nome não vazio e que não contenha apenas números.
    while True:
        nome = input("\nQual o seu nome? ").strip()

        if nome == "" or nome.isdigit():
            print("Nome inválido.")
        else:
            break

    # Verifica se a idade informada é numérica e maior que zero.
    while True:
        idade = input("Qual a sua idade? ").strip()

        if not idade.isdigit() or int(idade) <= 0:
            print("Idade inválida. Digite uma idade válida.")
        else:
            # Converte a idade para inteiro após a validação.
            idade = int(idade)
            break

    # Solicita o gênero por meio de opções numeradas.
    while True:
        print("\nQual é o seu gênero?")
        print("1 - Feminino")
        print("2 - Masculino")
        print("3 - Não-binário")
        print("4 - Outro")

        genero_opcao = input("Escolha: ").strip()

        # Converte a opção numérica no texto correspondente ao gênero.
        match genero_opcao:
            case "1":
                genero = "Feminino"
                break
            case "2":
                genero = "Masculino"
                break
            case "3":
                genero = "Não-binário"
                break
            case "4":
                genero = "Outro"
                break
            case _:
                opcao_invalida()
                continue

    # Direciona jovens de 11 a 17 anos para o Dentista do Bem.
    if 11 <= idade <= 17:
        dentista_do_bem(nome, idade, genero)

    # Direciona mulheres fora dessa faixa etária para o Apolônias do Bem.
    elif genero == "Feminino":
        apolonias_do_bem(nome)

    # Informa quando a pessoa não se enquadra nos critérios tratados.
    else:
        print(f"\nInfelizmente, {nome}, com {idade} anos, não se enquadra na faixa etária do Dentista do Bem.")
        voltar()


# Apresenta informações sobre o programa Apolônias do Bem.
def apolonias_do_bem(nome):
    while True:
        # Pergunta se a pessoa deseja saber como participar.
        entrar = input(
            "\nO programa Apolônias do Bem oferece ajuda a mulheres cis e trans vítimas de agressões físicas.\n"
            "Gostaria de saber como participar? (sim ou não): "
        ).strip().lower()

        if entrar == "sim":
            print("\nEntre em contato com a Turma do Bem pelo WhatsApp, 11 98965-8599.")
            print("Será solicitado um boletim de ocorrência e, posteriormente, ocorrerão uma entrevista e um exame clínico.")
            voltar()
            return

        # Aceita as duas formas de escrever a resposta negativa.
        elif entrar == "não" or entrar == "nao":
            print(f"\nTudo bem, {nome}! Agradecemos seu contato com a Turma do Bem.")
            voltar()
            return

        # Solicita novamente uma resposta válida.
        else:
            print("Resposta inválida. Digite sim ou não.")
            continue


# Apresenta informações sobre o programa Dentista do Bem.
def dentista_do_bem(nome, idade, genero):
    while True:
        # Pergunta se a pessoa deseja saber como participar.
        entrar = input(
            f"\nOlá, {nome}! Com {idade} anos, você está na faixa etária do programa Dentista do Bem.\n"
            "Gostaria de saber como participar? (sim ou não): "
        ).strip().lower()

        if entrar == "sim":
            print("\nEntre em contato pelo site:")
            print("https://turmadobem.org.br/contato/")
            voltar()
            return

        elif entrar == "não" or entrar == "nao":
            # Se a pessoa for do gênero feminino, apresenta também o outro programa.
            if genero == "Feminino":
                apolonias_do_bem(nome)
            else:
                print(f"\nTudo bem, {nome}! Agradecemos seu contato com a Turma do Bem.")
                voltar()
            return

        # Solicita novamente uma resposta válida.
        else:
            print("Resposta inválida. Digite sim ou não.")
            continue


# Recebe os dados de quem deseja entrar em contato com a ONG.
def contato():
    # Valida o nome informado.
    while True:
        nome = input("\nQual é o seu nome? ").strip()

        if nome == "" or nome.isdigit():
            print("Nome inválido.")
        else:
            break

    # Verifica se o telefone contém apenas números e tem pelo menos 10 dígitos.
    while True:
        telefone = input("Qual é o seu telefone (Somente números?): ").strip()

        if telefone.isdigit() and len(telefone) >= 10:
            break

        print("Telefone inválido. Digite um número com DDD.")

    # Impede que a mensagem enviada fique vazia.
    while True:
        mensagem = input("Escreva sua mensagem: ").strip()

        if mensagem == "":
            print("A mensagem não pode ficar vazia.")
        else:
            break

    # Agrupa os dados do contato em uma lista.
    dados_contato = [nome, telefone, mensagem]

    # Exibe os dados recebidos.
    print("\nDados recebidos:")
    print(f"1 - Nome: {dados_contato[0]}")
    print(f"2 - Telefone: {dados_contato[1]}")
    print(f"3 - Mensagem: {dados_contato[2]}")

    # Confirma o recebimento da mensagem.
    print(f"\nObrigado, {nome}! Recebemos sua mensagem {mensagem}. Caso necessite de uma resposta, entraremos em contato em breve.")

    voltar()


# Informa que a opção escolhida não é válida.
def opcao_invalida():
    print("\nOpção inválida. Digite apenas números.\n")


# Exibe uma mensagem indicando o retorno ao menu principal.
def voltar():
    print("\nVoltando ao menu principal...\n")


# ---------- MENU PRINCIPAL ----------

# Armazena os nomes das opções exibidas no menu.
opcoes_menu = [
    "Quero ajudar",
    "Preciso de ajuda",
    "Contato",
    "Consultar registro de doações",
    "Sair"
]

# Mantém o menu principal em execução até o usuário escolher sair.
while True:

    print("\n===== TURMA DO BEM =====")
    print("Digite uma opção de contato:")

    # Exibe cada opção com seu número correspondente, começando em 1.
    for i, opcao in enumerate(opcoes_menu, start=1):
        print(f"{i} - {opcao}")

    # Recebe a opção escolhida pelo usuário.
    opcao = input("Escolha uma opção: ")

    # Executa a função correspondente à opção escolhida.
    match opcao:
        case "1":
            quero_ajuda()

        # ---------- OPÇÃO 2: PRECISO DE AJUDA ----------
        case "2":
            preciso_de_ajuda()

        # ---------- OPÇÃO 3: CONTATO ----------
        case "3":
            contato()

        # ---------- OPÇÃO 4: CONSULTAR DOAÇÕES ----------
        case "4":
            consultar_doacoes()

        # ---------- OPÇÃO 5: SAIR ----------
        case "5":
            print("Obrigado por visitar a Turma do Bem. Até logo!")
            break

        # Trata opções que não correspondem às disponíveis.
        case _:
            opcao_invalida()