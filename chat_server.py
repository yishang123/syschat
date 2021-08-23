#!/usr/bin/python3
#-*- coding:UTF-8 -*-
import socketserver

class Chat_server(socketserver.StreamRequestHandler):
   def handle(self):
       conn = self.request
       try:
           while True:
               data_b = conn.recv(1024)
               print('data_b = ', data_b)
               if conns.count(conn) == 0:
                   conns.append(conn)
                   name_s = data_b.decode('utf-8')
                   users.setdefault(conn, name_s)
                   data_s = ''
                   data = 'Welcome' + name_s + '!'
               else:
                   name_s = users.get(conn)
                   data_s = data_b.decode('utf-8')
                   data = name_s + ': ' + data_s
               print('data = ', data)
               data_b = data.encode('utf-8')
               for cn in conns:
                   cn.send(data_b)
               if data_s.upper()[0:3] == 'BYE':
                   print('%s is exited!' % name_s)
                   conns.remove(conn)
                   del(users[conn])
                   break;
       except Exception as e:
           print('Error is ', e)
conns = []
users = {}
ip = '127.0.0.1'  #注意这里是服务器的内网地址不是公网地址
server = socketserver.ThreadingTCPServer((ip, 9988), Chat_server)
print('Wait for TCP connecting...')
server.serve_forever()
