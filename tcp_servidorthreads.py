#######################################################
#  Servidor TCP com Threads
# Alunos:
# Denilson da Silva Sousa
# Vinicius Loiola Cavalheiro
#######################################################

import socket # Biblioteca que dá suporte ao canal de comunicação
import threading

class ClientThread(threading.Thread):  
  def __init__(self, ip, port, conn):
    threading.Thread.__init__(self)
    self.ip = ip
    self.port = port
    self.conn = conn
    print("Cliente no endereço {} e na porta {} pronto".format(ip, port))
    
  def run(self):   
    while True:
      data = self.conn.recv(1024)
      print(data.decode())
      if not data:
        break
      # Mensagem que vai ser retornada
      msg = "Olá cliente {}".format(self.ip)
      #Envia uma mensagem de retorno para o cliente
      self.conn.send(msg.encode())


def main():
  HOST = '172.17.0.2' #Constante com o endereço IP do Servidor
  PORT = 65432  #Número da Porta que o Servidor vai ficar escutando

  # Aqui é criado o objeto do tipo socket, para dar suporte a conexão
  # Diferente do UDP aqui é criado um STREAM ao invés de um DGRAM
  # O with é um recurso do python para fechar o socket após o programa encerrar
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Associa uma porta ao host
    s.bind((HOST, PORT))
    threads = []

    while True:    
      #Faz o servidor ficar esperando por uma conexão
      s.listen()
      # Aqui o servidor "aceita" a conexão com o cliente
      # Retorna duas informações: a conexão e o endereço do cliente
      (conn, (ip, port)) = s.accept()
      nThread = ClientThread(ip, port, conn)
      nThread.start()
      threads.append(nThread)
    
    for thread in threads:
      thread.join()

if __name__ == '__main__':
  main()