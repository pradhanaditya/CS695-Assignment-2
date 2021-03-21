#!/usr/bin/env python3

import socket
import time
import random

from _thread import *
import threading

displayLock = threading.Lock()

available_modes = {'LOW_LOAD' : 0, 'HIGH_LOAD' : 1}

current_mode = 1

low_load_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
high_load_list = [30, 31, 32, 33, 34, 35]

nServers = 1

def client_thread(server_ip, server_port):
    sleep_time = 0.2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        while True:
            if current_mode == available_modes['LOW_LOAD']:
                s.sendall(str(random.choice(low_load_list)).encode('utf-8'))
                response = s.recv(1024)
                result = int(response.decode('utf-8'))
                displayLock.acquire()
                print("Received the result: " + str(result))
                displayLock.release()
                time.sleep(sleep_time)    
            elif current_mode == available_modes['HIGH_LOAD']:
                s.sendall(str(random.choice(high_load_list)).encode('utf-8'))
                response = s.recv(1024)
                result = int(response.decode('utf-8'))
                displayLock.acquire()
                print("Received the response: " + str(result))
                displayLock.release()
            else:
                displayLock.acquire()
                print("Unexpected error!")
                displayLock.release()

def Main():
    start_new_thread(client_thread, ('192.168.122.2', 12345, ))
    exit_msg = input("Press Enter to exit.")

if __name__ == '__main__':
    Main()