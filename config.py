import random
import time

def add_to_history(chosen, win):
    choosenstr = ''
    winstr = ''
    for i in chosen:
        choosenstr += str(i) + ","
    for j in win:
        winstr += str(j) + ","
    with open('history.txt', 'a') as f:
        f.write(f"Chosen by you: {choosenstr}\n")
        f.write(f"Winning: {winstr}\n\n")


def receive_message(sock):
    data = b''
    while b'\r\n\r\n' not in data:
        data += sock.recv(1)
    return data.decode()

def send_message(sock, message):
    message += '\r\n\r\n'
    sock.sendall(message.encode())


def generate_numbers():
    generated_numbers = ""
    seed = float(time.time())
    random.seed(seed)
    numbers = random.sample(range(1, 51), 6)
    for i in numbers:
        generated_numbers += str(i) + ","
    return generated_numbers[:-1]

# print(generate_numbers())

ip = '127.0.0.1'
port = 12139
