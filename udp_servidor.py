#######################################################
#  Servidor UDP
# Alunos:
# Denilson da Silva Sousa
# Vinicius Loiola Cavalheiro
#######################################################

import socket # Biblioteca que dá suporte ao canal de comunicação
import json # Biblioteca que dá suporte a objetos json

UDP_IP_ADDRESS = "127.0.0.1" #Constante com o endereço IP do Servidor
UDP_PORT_N0 = 4567 #Número da Porta que o Servidor vai ficar escutando

#Módulo (socket) informa ao S.O que quer utilizar a rede.
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Função que associa o objeto socket acima com a porta
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_N0))

print("Servidor UDP ouvindo...")
#Fica em um loop infinito aguardando mensagens
while True:
  # Função fica extrai o data e o endereço da mensagem enviada
  # Socket fica bloqueado e quando recebe mensagem, ele é desbloqueado
  data, addr = serverSock.recvfrom(1024)

  # Converte a string recebida em um objeto json/dicionario
  data = json.loads(data)
  # Extrai os dados da Mensagem (Mensagem e Porta)
  desc = data["desc"]
  porta = data["porta"]

  # Imprime a mensagem
  print("Menssagem: ", desc)

  # Cria a mensagem de retorno ao cliente
  message = "Olá cliente!"

  # Envia mensagem de retorno para o cliente
  serverSock.sendto(message.encode(), addr)

serverSock.close()
  