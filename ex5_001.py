"""
Programa Cálculo salarial
Descrição: O programa deve perguntar o número de horas trabalhadas, calcular e imprimir na tela o valor do salário bruto, do salário líquido e do total de descontos, sabendo que o desconto do imposto é 30% e que o valor da hora-aula é R$ 40,00.
Autor: Augusto Jacques
Data: 25/02/2025
Versão: 0.0.1
"""

# Alocação de memória

horas = int(0)
salario_bruto = float()
salario_liquido = float()
valor_hora = int(40)
imposto = float(0.3)
descontos = float()

# Entrada de dados

horas = float(input("\nQuantas horas você trabalhou?"))

# Processamento de dados

salario_bruto = horas * valor_hora
descontos = salario_bruto * imposto
salario_liquido = salario_bruto - descontos

# Saída de dados

print(f"O salário bruto é {salario_bruto} reais.")
print(f"O salário líquido é {salario_liquido} reais.")
print(f"Os descontos foram {descontos} reais.")