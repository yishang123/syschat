#!/usr/bin/python3
# coding:utf-8
import socket
import threading
import tkinter as tk
def send_msg():
    txt = bt_txt.get()
    if txt == 'Logon':
        bt_txt.set('Send')
    msg = et_txt.get()
    et_txt.set('')
    print('msg = ', msg)
    msg_b = msg.encode('utf-8')
    s.send(msg_b)
    if msg.upper()[0:3] == 'BYE':
        chat_send.config(state = tk.DISABLED)
        s.close()

def receive_msg():
    while True:
        try:
            data_b = s.recv(1024)
            data_s = data_b.decode('utf-8')
            print('data_s = ', data_s)
            chat_list.insert(tk.END, data_s)
            chat_list.see(tk.END)
        except Exception as e:
            print('Error is ', e)
            print('Exist!')
            break

#ip = '192.168.213.128'
ip = '106.14.1.83'
#ip = 'localhost'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 9988))
t = threading.Thread(target = receive_msg)
t.start()
root = tk.Tk()
root.title('Chatting room')
root.geometry('300x350')
root.resizable(width = False, height = True)
fm = tk.Frame(root, width=300, height=300)
scrl = tk.Scrollbar(fm)
chat_list = tk.Listbox(fm, width=300, selectmode=tk.BROWSE)
chat_list.configure(yscrollcommand=scrl.set)
scrl['command'] = chat_list.yview
bt_txt = tk.StringVar(value='Logon')
et_txt = tk.StringVar(value='')
chat_txt = tk.Entry(root, bd=5, width=280, textvariable=et_txt)
chat_send = tk.Button(root, textvariable=bt_txt, command=send_msg)
scrl.pack(side=tk.RIGHT, fill=tk.Y)
chat_txt.pack()
chat_send.pack()
chat_list.pack()
fm.pack()
root.mainloop()
