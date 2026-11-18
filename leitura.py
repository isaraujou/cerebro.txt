ARQUIVO_CEREBRO = "cerebro.txt"
SEPARADOR = "|||"  # Evita erros caso a pergunta tenha hífen (-)

def carregar_dados():
    """Lê o arquivo e retorna um dicionário {pergunta: resposta}."""
    base_dados = {}
    try:
        with open(ARQUIVO_CEREBRO, "r", encoding="utf-8", errors="replace") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(SEPARADOR, 1)
                if len(dados) == 2:
                    pergunta, resposta = dados
                    base_dados[pergunta] = resposta
    except FileNotFoundError:
        pass
    return base_dados


def salvar_dados(base_dados):
    """Salva o dicionário inteiro no arquivo, evitando perguntas duplicadas."""
    with open(ARQUIVO_CEREBRO, "w", encoding="utf-8") as arquivo:
        for pergunta, resposta in base_dados.items():
            arquivo.write(f"{pergunta}{SEPARADOR}{resposta}\n")


def ensinar():
    pergunta = input("Digite a pergunta: ").strip().lower()
    # Não usamos .lower() na resposta para manter letras maiúsculas/pontuação corretas
    resposta = input("Digite a resposta: ").strip()

    if not pergunta or not resposta:
        print("bot: Pergunta e resposta não podem ficar vazias!")
        return

    base_dados = carregar_dados()
    base_dados[pergunta] = resposta  # Atualiza se já existir, ou cria se for nova
    salvar_dados(base_dados)
    print("bot: Aprendido com sucesso!")


def conversar():
    base_dados = carregar_dados()

    if not base_dados:
        print("bot: Meu cérebro está vazio! Me ensine algo primeiro (opção 2).")
        return

    fala = input("Você: ").strip().lower()

    if fala in base_dados:
        print(f"bot: {base_dados[fala]}")
    else:
        print("bot: Desculpe, não sei a resposta. Use a opção 2 para me ensinar.")


def listar_conhecimento():
    base_dados = carregar_dados()

    if not base_dados:
        print("Nenhum dado cadastrado ainda.")
        return

    print("\n--- MEMÓRIA DO PYBOT (ORDENADA) ---")
    # sorted(base_dados.items()) ordena alfabeticamente pelas perguntas
    for pergunta, resposta in sorted(base_dados.items()):
        print(f"Pergunta: {pergunta} -> Resposta: {resposta}")


# --- LOOP PRINCIPAL ---
while True:
    print("\n--- PYBOT ---")
    print("1 - Conversar")
    print("2 - Ensinar")
    print("3 - Listar conhecimentos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        conversar()
    elif opcao == "2":
        ensinar()
    elif opcao == "3":
        listar_conhecimento()
    elif opcao == "0":
        print("Encerrando o PyBot...")
        break
    else:
        print("Opção inválida!")