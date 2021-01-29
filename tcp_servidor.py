#######################################################
#  Servidor TCP
# Alunos:
# Denilson da Silva Sousa
# Vinicius Loiola Cavalheiro
#######################################################

import socket # Biblioteca que dá suporte ao canal de comunicação

HOST = '172.17.0.2' #Constante com o endereço IP do Servidor
PORT = 65432  #Número da Porta que o Servidor vai ficar escutando

# Aqui é criado o objeto do tipo socket, para dar suporte a conexão
# Diferente do UDP aqui é criado um STREAM ao invés de um DGRAM
# O with é um recurso do python para fechar o socket após o programa encerrar
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  #Associa uma porta ao host
  s.bind((HOST, PORT))

  #Faz o servidor ficar esperando por uma conexão
  s.listen()

  # Aqui o servidor "aceita" a conexão com o cliente
  # Retorna duas informações: a conexão e o endereço do cliente
  conn, addr = s.accept()

  # O with é um recurso do python para fechar a conexão após o encerramento deste trecho de código
  with conn:
    #Imprime com qual cliente está conectado, neste caso identificado pelo seu endereço
    print('Conectando com', addr)
    # Aqui é criado um loop infinito, já que um servidor fica ouvindo enquanto estiver ligado.
    while True:
      # Aguarda uma requisição do cliente
      data = conn.recv(1024)
      # Mensagem recebida do cliente
      print(data.decode())
      #Recurso para destravar o servidor caso o cliente não envie nada
      if not data:
        break
      # Mensagem que vai ser retornada
      msg = "Olá cliente {}".format(addr)
      #Envia uma mensagem de retorno para o cliente
      conn.sendall(msg.encode())
