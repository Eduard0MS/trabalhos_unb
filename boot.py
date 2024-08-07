# -*- coding: iso-8859-1 -*-


############### YOUTUBE #####################
from iqoptionapi.stable_api import IQ_Option
import time


### preencha seu email e senha aqui abaixo ###
email = 'seu-email-aqui'
senha = 'suasenha'

API = IQ_Option(email,senha)


### Função para conectar na IQOPTION ###
check, reason = API.connect()
if check:
    print('Conectado com sucesso')
else:
    if reason == '{"code":"invalid_credentials","message":"You entered the wrong credentials. Please ensure that your login/password is correct."}':
        print('Email ou senha incorreta')
        
    else:
        print('Houve um problema na conexão')

        print(reason)

### Função para Selecionar demo ou real ###
while True:
    escolha = input('Selecione a conta em que deseja conectar: demo ou real  - ')
    if escolha == 'demo':
        conta = 'PRACTICE'
        print('Conta demo selecionada')
        break
    if escolha == 'real':
        conta = 'REAL'
        print('Conta real selecionada')
        break
    else:
        print('Escolha incorreta! Digite demo ou real')
        
API.change_balance(conta)

### Função abrir ordem e checar resultado ###
def compra(ativo,valor,direcao,exp,tipo):
    if tipo == 'digital':
        check, id = API.buy_digital_spot_v2(ativo,valor,direcao,exp)
    else:
        check, id = API.buy(valor,ativo,direcao,exp)


    if check:
        print('Ordem executada ',id)

        while True:
            time.sleep(0.1)
            status , resultado = API.check_win_digital_v2(id) if tipo == 'digital' else API.check_win_v4(id)

            if status:
                if resultado > 0:
                    print('WIN', round(resultado,2))
                elif resultado == 0:
                    print('EMPATE', round(resultado,2))
                else:
                    print('LOSS', round(resultado,2))
                break

    else:
        print('erro na abertura da ordem,', id)
        

#ativo = 'EURUSD'
valor = 10.50
direcao = 'call'
exp = 1
tipo = 'digital'


### chamada da função de compra ###
compra(ativo,valor,direcao,exp,tipo)





### Função para separar tipos de dados de uma ordem ###
def separar_dados(dados):
    dados = dados.split(';')
    dados = [float(i) for i in dados]
    return dados

### Função para pegar dados de uma ordem ###
def pegar_dados_dig(id,tipo):
    if tipo == 'digital':
        dados = API.get_digital_spot_profit_after_sale(id)
    else:
        dados = API.get_option_profit_after_sale(id)
    return dados
def pegar_dados_bin(id,tipo):
    if tipo == 'binaria':
        dados = API.get_digital_spot_profit_after_sale(id)
    else:
        dados = API.get_option_profit_after_sale(id)
    return dados

### Função para tratamento de dados ###
def tratamento_dados(dados):
    dados = dados.split(';')
    dados = [float(i) for i in dados]
    for j in range(len(dados)):
        if dados[j] == 0:
            return 0
        else:
            return dados[j]
