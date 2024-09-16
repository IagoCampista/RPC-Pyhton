from xmlrpc.server import SimpleXMLRPCServer
import time
import socket

def calcular_pagamento(salario_mensal, horas_trabalhadas, horas_extras, mes_vigente):
    tempo_processamento = time.time()
    
    # Cálculo do décimo terceiro salário
    if mes_vigente == 12:
        salario_mensal += salario_mensal

    # Cálculo do valor da hora trabalhada
    valor_hora = salario_mensal / (horas_trabalhadas * 30)
    
    # Cálculo do valor das horas extras
    valor_horas_extras = horas_extras * valor_hora * 1.5
    
    # Cálculo do descanso semanal remunerado (DSR)
    dsr = (valor_horas_extras / 6)
    
    # Cálculo da contribuição ao INSS
        # primeira faixa do inss - 1412*0.075 = 105.9
        # segunda faixa do inss - (2666.68 - 1412) *0.09 = 112.92
        # terceira faixa do inss - (4000.03 - 2666.68) * 0.12 = 160
        # quarta faixa do inss - (7786.02 - 4000.03 ) * 0.14 = 530.03
        
    if salario_mensal <= 1212.00:
        inss = salario_mensal * 0.075
    elif salario_mensal <= 2666.68:
        inss = ((salario_mensal - 1412) * 0.09) + 105.9 
    elif salario_mensal <= 4000.03:
        inss = ((salario_mensal - 2666.68) * 0.12) + 105.9 + 112.92
    elif salario_mensal <= 7786.02:
        inss = ((salario_mensal - 4000.03) * 0.14) + 105.9 + 112.92 + 160.00
    else:
        #teto de contribuicao do inss
        inss = 105.9 + 112.92 + 160 + 530.03
    
    # Valor total a ser pago
    valor_total = salario_mensal + valor_horas_extras + dsr - inss
    
    # Exibe o tempo de processamento e o IP do cliente
    tempo_processamento = time.time() - tempo_processamento
    ip_cliente = socket.gethostbyname(socket.gethostname())
    print(f"Tempo de processamento: {tempo_processamento:f} segundos")
    print(f"IP do cliente: {ip_cliente}")

    return {
        'valor_total': valor_total,
        'dsr': dsr,
        'inss': inss
    }

# Configura o servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor pronto para receber chamadas...")
server.register_function(calcular_pagamento, "calcular_pagamento")
server.serve_forever()

