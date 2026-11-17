def ensinar():
    pergunta = input("Digite a pergunta:").strip().lower()
    resposta = input ("digite a resposta:").strip().lower()

    with open ("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta}-{resposta}\n")

def conversar():
    fala = input ("voce: ").strip().lower()
    encontrou= False

try:
    with open ("cerebro.txt", "r", encoding="utf-8") as arquivo:
        linhas= arquivo.readlines()

        for linha in linhas:
            dados=linhas.strip().split(" - ")
            if len(dados) == 2:
                pergunta_salva,resposta_salva = dados [0], dados [1]
                if fala == pergunta:
                    print(f"bot: {resposta}")
                    encontrou: True 
                    break
                if not encontrou:
                    print("bot: desculape, não sei a resposta. use a opção 2 para me ensinar.  ")


except FileNotfoundError:
     print("bot: meu cérebro está vazio! ME ensine algo primeiro .")


def listar_conhecimento():
    base_dados = []
    try: 
        with open ("crebro.txt", "r", encoding="utf-8")
        as arquivo: 
        linhas = arquivo.readlines()
        for linha in linhas:
            dados=linha.strip().slipt(" - ")
            if len(dados) == 2:
                #cria tupla (pergunta, resposta e adiciona na lista)
                base_dados.append((dados[0], dados [1]))

#Ordena alfabeticamente pela primeira posição da tupla (pergunta)
base_dados.sort()
