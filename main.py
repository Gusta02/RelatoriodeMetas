# Bibliotecas:
# Pandas
import pandas as pd

# Openpyxl

# Twilio
from twilio.rest import Client

#carrega token e conta do twilio

accont_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

client = Client(accont_sid, auth_token)

# Passo a Passo da solução

# Abrir os arquivos em Excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if(tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} alguém bateu a meta. Vendedor: {Vendedor}, Vendas: {Vendas}')
        menssage = client.messages.create(
            to="xxxxxxxxxxxx",
            from_="xxxxxxxx", # exemplo de numero +5521987586557
            body=f'No mes {mes} alguém bateu a meta. Vendedor: {Vendedor}, Vendas: {Vendas}')
        print(menssage.sid)





# Para cada arquivo:

# Verificar se algum valor na colona de vendas daquele arquivo Ultrapassol dos 55 mil.

# se for maior do que 55k >> Envia um SMS com Nome, mes, vendas do vendedor.

# Caso n passe dos 55k >> n faça nada.
