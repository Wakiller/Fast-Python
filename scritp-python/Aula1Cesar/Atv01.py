quantidade = int(input("Quantos de carros vendidos: "))
venda = float(input("Valor das vendas: "))
salario = float(input("Qual Salario: "))
comissao = float(input(("Qual a comissão: ")))

salario_final = salario + (quantidade*comissao) + (venda*0.05)

print(f"O salário do vendedor é {salario_final:.2f}")
