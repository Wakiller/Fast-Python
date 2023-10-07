def conversao_minutos(horas):
    conversao=horas*60
    return conversao
def conversao_segundos(minutos):
    conversao=minutos*3600
    return conversao
horas=int(input("Valor em horas para conversão: "))
op=int(input("1-Converter em minutos \n"
              "2-Converter em segundos"))
minutos=conversao_minutos(horas)
segundos=conversao_segundos(horas)
if op==1:
    print(f"{horas} horas é igual a {minutos:.2f} minutos")
else:
    print(f"{horas} horas é igual a {segundos:.2f} segundos")