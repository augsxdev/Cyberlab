import socket

print("Iniciando scanner...")

print("=== CyberLab Scanner ===")

ip = input("digite o IP: ")

for porta in range(1,1025):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.settimeout(0.05)
   resultado = sock.connect_ex((ip, porta))
   if resultado == 0:
      print(f"[+] Porta {porta} aberta")
   sock.close()


print("Scanner finalizado.")