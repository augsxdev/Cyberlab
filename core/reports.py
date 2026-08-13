from datetime import datetime
agora = datetime.now()
nome = agora.strftime("relatorio_%Y%m%d_%H%M%S.txt")
with open(nome,"w") as arquivo:
    arquivo.write(f"Relatório gerado em: {agora.strftime('%d/%m/%Y %H:%M:%S')}\n")
    arquivo.write("Conteúdo do relatório...\n")
    arquivo.write("=====================================\n")
arquivo.write("        CYBERLAB REPORT\n")
arquivo.write("=====================================\n\n")

arquivo.write(f"Data: {agora.strftime('%d/%m/%Y')}\n")
arquivo.write(f"Hora: {agora.strftime('%H:%M:%S')}\n\n")
arquivo.write("Tipo: Scanner de Portas\n\n")
arquivo.write("Resultados:\n")
arquivo.write("-----------------------------\n")
arquivo.write("Nenhum resultado registrado.\n\n")
arquivo.write("=====================================\n")
arquivo.write("Fim do relatório\n")
arquivo.write("=====================================\n")