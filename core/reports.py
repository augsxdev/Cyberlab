from datetime import datetime
agora = datetime.now()
nome = agora.strftime("relatorio_%Y%m%d_%H%M%S.txt")
with open(nome,"w") as arquivo:
    arquivo.write(f"Relatório gerado em: {agora.strftime('%d/%m/%Y %H:%M:%S')}\n")
    arquivo.write("Conteúdo do relatório...\n")