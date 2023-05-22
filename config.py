import random
import time
from errors import *
import linecache
def add_to_history(chosen, win):
    choosenstr = ''
    winstr = ''
    for i in chosen.split(","):
        choosenstr += str(i) + ","
    for j in win:
        winstr += str(j) + ","
    with open('history.txt', 'a') as f:
        f.write(f"Chosen by you: {choosenstr[:-1]}\n")
        f.write(f"Winning numbers: {winstr[:-1]}\n\n")


def receive_message(sock):
    data = b''
    while b'\r\n\r\n' not in data:
        data += sock.recv(1)
    return data.decode()

def send_message(sock, message):
    message += '\r\n\r\n'
    sock.sendall(message.encode())


# def generate_numbers():
#     generated_numbers = ""
#     seed = float(time.time())
#     random.seed(seed)
#     numbers = random.sample(range(1, 51), 6)
#     for i in numbers:
#         generated_numbers += str(i) + ","
#     return generated_numbers[:-1]

def pi_generator():
    r_pi = linecache.getline("./pi_numbers.txt", random.randrange(0, 1104058))
    return int(r_pi)
def generate_numbers():
    seed = int(time.time() * pi_generator())//pi_generator()
    a = pi_generator()
    c = 12345
    m = 2**31
    generated_numbers = ""
    for _ in range(6):
        seed = (a * seed + c) % m
        liczba = 1 + (seed % 50)
        generated_numbers += str(liczba) + ","
    return generated_numbers[:-1]




# with open (r'../../pi.txt', 'r') as filepi:
#     pi = filepi.read()
# pi += 'p'
#
# with open (r'./pi_numbers.txt', 'w') as sendpi:
#     i = 0
#     fourpi = ''
#     while True:
#         for j in pi:
#             if i > random.randrange(9,16):
#                 if j == 'p':
#                     break
#                 else:
#                     sendpi.writelines(fourpi+'\n')
#                     fourpi = ''
#                     i = 0
#             else:
#                 i += random.randrange(1, 3)
#                 fourpi += str(j)
#



def generate_request(numbers=None, play_mode=None, mode="g", message=None):
    request = ""
    if mode == "g":
        request += r"PLAY\r\n"
        if play_mode == "l":
            request += r"-r\r\n"
        elif play_mode == "w":
            request += r"-f\r\n"
        else:
            raise InvalidModeException
        if numbers == "":
            raise InvalidNumbersException
        elif len(numbers.split(",")) < 6:
            raise InvalidNumbersException
        else:
            request += f"-n{numbers}"
    if mode == "s":
        request += r"SEND\r\n"
        request += f"-m{message}"
    return request


# print(generate_numbers())
# print(generate_request(mode="g", numbers="1,2,3,4,5,6", play_mode="w"))

ip = '127.0.0.1'
port = 12139
