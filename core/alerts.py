from __future__ import annotations


RULES = {
    23: ("critical", "Telnet ativo: protocolo sem criptografia."),
    21: ("medium", "FTP exposto: valide se TLS e credenciais fortes estão ativos."),
    445: ("high", "SMB exposto: restrinja à rede necessária e mantenha atualizações."),
    3389: ("high", "RDP exposto: limite acesso, use MFA e políticas de bloqueio."),
}


def evaluate(open_ports: list[dict]) -> list[dict]:
    alerts = []
    for item in open_ports:
        if item["port"] in RULES:
            severity, message = RULES[item["port"]]
            alerts.append({"severity": severity, "port": item["port"], "message": message})
    return alerts
