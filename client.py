import socket
from config import receive_message, send_message, generate_numbers, generate_request, ip, port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((ip, port))

    receive_hello = receive_message(server)
    receive_hello = receive_hello.split(r"\r\n")[-1][2:]
    print(receive_hello)

    send_hello = generate_request(mode="s", message=f"[CLIENT] HI SERVER {ip}")
    send_message(server, send_hello)

    while True:
        mode = input('Wybierz tryb gry:\n(l) losowanie\n(w) wpisanie liczb: ')
        if mode == 'l' or mode == 'w':
            break
        else:
            print('Nieprawidłowy tryb gry. Wybierz (l) lub (w).')

    if mode == 'l':
        send_numbers = generate_numbers()
    else:
        print('Podaj 6 liczb: \n')
        numbers = []
        numbers_str = ''
        for _ in range(6):
            num = int(input())
            while True:
                if num > 50 or num in numbers:
                    num = int(input("Podaj inną liczbę: "))
                else:
                    break
            numbers.append(num)
            numbers_str += str(num) + ","
        numbers_str = numbers_str[:-1]
        send_numbers = numbers_str

    request = generate_request(numbers=send_numbers, play_mode=mode)
    send_message(sock=server, message=request)

    result = receive_message(server)
    print(result)

    if input("Pokazać historie[N/Y]").lower() == "y":
        print('Historia losowań:')
        print(receive_message(server))
    server.close()
    exit()
