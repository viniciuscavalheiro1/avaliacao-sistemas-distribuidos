#######################################################
#  Cliente TCP
# Alunos:
# Denilson da Silva Sousa
# Vinicius Loiola Cavalheiro
#######################################################

import socket # Biblioteca que dá suporte ao canal de comunicação
import time # Biblioteca para gerenciar tempo real
import statistics # Módulo para facilitar calculos matematicos

HOST = '127.0.0.1' #Constante com o endereço IP do Servidor
PORT = 65432  #Número da Porta que o Servidor vai ficar escutando

times = []

# Aqui é criado o objeto do tipo socket, para dar suporte a conexão
# Diferente do UDP aqui é criado um STREAM ao invés de um DGRAM
# O with é um recurso do python para fechar o socket após o programa encerrar
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # Como o TCP é orientado a conexão, é necessário estabelecer uma conexão com o servidor
  # Se ocorrer tudo como esperado, o Servidor deve aceitar a conexão
  s.connect((HOST, PORT))

  for x in range(10):
    #Captura o tempo inicial
    t0 = time.time()
    #Envia mensagem ao Servidor
    s.sendall('Olá Servidor. Numero da requisição:{}'.format(x+1).encode())
    #Fica aguardando mensagem de retorno do Servidor
    data = s.recv(1024)
    #Imprime mensagem de retorno do Servidor
    print('Recebido do servidor: ', data.decode())
    t1 = time.time()
    #Imprime o tempo de ida e volta da mensagem
    print("Time: {} ".format(t1-t0))
    #Adiciona o tempo na lista de tempos
    times.append(t1-t0)

print("-----------------------")
print("Relatório")
print("-----------------------")
#Imprime a Média
print("Média: {} ".format(statistics.mean(times)))
#Imprime o Desvio Padrão
print("Desvio Padrão: {}".format(statistics.pstdev(times)))
#Imprime o Maior Tempo
print("Tempo Máximo: {} ".format(max(times)))
#Imprime o Menor Tempo
print("Tempo Minimo: {}".format(min(times)))