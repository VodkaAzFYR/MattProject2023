import socket
from config import ip, port, receive_message, send_message, generate_numbers, add_to_history

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(5)

        client, addr = s.accept()
        print(f"CONNECTED WITH {addr[0]}")

        send_message(client, 'Connected with server!')

        input_user = receive_message(client)
        curr_number = [int(x) for x in generate_numbers().split(',')]
        guess = [int(x) for x in input_user.split(',')]
        print(curr_number)
        print(guess)
        good_guesses = 0
        for i in guess:
            if i in curr_number:
                good_guesses += 1
        if good_guesses > 0:
            response = f'You won!, you guessed: {good_guesses}'
            send_message(client, response)
            add_to_history(guess, curr_number)
            with open(r'./history.txt', 'r') as file:
                history = (file.read())
                " ".join(history)
            send_message(client, history)

        else:
            response = 'You lost! again losser'
            send_message(client, response)
            add_to_history(guess, curr_number)
            with open(r'./history.txt', 'r') as file:
                history = (file.read())
            send_message(client, history)

    s.close()
    vvhvhjvhjvhj