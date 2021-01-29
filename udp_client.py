#######################################################
# Cliente UDP
# Alunos:
# Denilson da Silva Sousa
# Vinicius Loiola Cavalheiro
#######################################################

import socket # Biblioteca que dá suporte ao canal de comunicação
import json # Biblioteca que dá suporte a objetos json
import time # Biblioteca para gerenciamento de tempo
import statistics # Módulo para facilitar calculos matematicos

UDP_IP_ADDRESS_server = "172.17.0.2"
UDP_IP_ADDRESS_client = "172.17.0.3"

UDP_IP_ADDRESS =  #Constante com o endereço IP do Servidor
UDP_PORT_N0 = 4567 # Número da Porta que o Servidor vai ficar escutando

UDP_PORT_N1 = 7654 # Número da Porta que o Cliente vai esperar o retorno

#Módulo (socket) informa ao S.O que quer utilizar a rede.
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associa o objeto socket acima a uma porta
clientSock.bind((UDP_IP_ADDRESS_client, UDP_PORT_N1))

# Loop de 10 iterações
times = []
for x in range(10):

  # Pego o tempo inicial
  t0 = time.time()

  # Cria  a mensagem com duas informações, a mensagem literal e a porta em que o cliente vai receber o retorno
  message = {"desc": "Olá Servidor, requisição de n° {}".format(x+1) , "porta": UDP_PORT_N1}
  # Envia a mensagem, lembrando que o dicionário acima é convertido em uma string
  clientSock.sendto(json.dumps(message).encode(), (UDP_IP_ADDRESS_server, UDP_PORT_N0)) 

  # Captura a mensagem e o endereço retornado pelo servidor 
  data, addr = clientSock.recvfrom(1024)

  #Imprime a mensagem recebida de retorno pelo servidor
  print(data.decode())

  #Pega o tempo final
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

#Fecha a conexão
clientSock.close()