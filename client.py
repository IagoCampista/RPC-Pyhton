import xmlrpc.client

def main():
    # Solicita os dados do usuário
    salario_mensal = float(input("Digite o valor do salário mensal: "))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas na jornada diária contratada: "))
    horas_extras = float(input("Digite a quantidade de horas extras: "))
    mes_vigente = input("Digite o mês vigente: ")

    # Conecta ao servidor
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        # Chama o método remoto
        resultado = proxy.calcular_pagamento(salario_mensal, horas_trabalhadas, horas_extras, mes_vigente)
        
        # Exibe os resultados
        print(f"Valor total a ser pago: R${resultado['valor_total']:.2f}")
        print(f"Valor do descanso semanal remunerado: R${resultado['dsr']:.2f}")
        print(f"Valor da contribuição ao INSS: R${resultado['inss']:.2f}")

if __name__ == "__main__":
    main()
