import socket

print("=== CyberLab Network ===")

rede = input("Digite a rede: ")

portas = [80, 443, 22, 445, 3389]

for host in range(1, 255):
    ip = f"{rede}.{host}"
    

    for porta in portas:
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.settimeout(0.05)
     print(f"Testando {ip}:{porta}")
     resultado = sock.connect_ex((ip, porta))
     print(resultado)
     
     sock.close()
     if resultado == 0:
        print(f"✓ Dispositivo encontrado: {ip}")

        break
      