import socket
from config import receive_message, send_message, generate_numbers, ip, port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip, port))

    while True:
        mode = input('Wybierz tryb gry:\n(l) losowanie\n(w) wpisanie liczb: ')
        if mode == 'l' or mode == 'w':
            break
        else:
            print('Nieprawidłowy tryb gry. Wybierz (l) lub (w).')

    if mode == 'l':
        send_message(sock, generate_numbers())
    else:
        print('Podaj 6 liczb: \n')
        numbers = ''
        for _ in range(6):
            num = input()
            while True:
                if num in numbers:
                    num = input("Podaj inną liczbę: ")
                else:
                    break
            numbers += num + ","
        numbers = numbers[:-1]
        send_message(sock, numbers)

    result = receive_message(sock)
    print(result)
    if input("Pokazać historie[N/Y]").lower() == "y":
        print('Historia losowań:')
        print(receive_message(sock))
    sock.close()
    exit()
