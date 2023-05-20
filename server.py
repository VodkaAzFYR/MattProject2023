import socket
from config import ip, port, receive_message, send_message, generate_numbers, add_to_history, generate_request

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(5)

        client, addr = s.accept()
        print(f"CONNECTED WITH {addr[0]}")

        hello_mess = generate_request(mode="s", message=f"[SERVER] HELLO CLIENT {addr[0]}")
        send_message(client, hello_mess)

        receive_hello = receive_message(client)
        receive_hello = receive_hello.split(r"\r\n")[-1][2:]
        print(receive_hello)

    #PLAY\r\n-f-n1,2,3,4,5,6

        input_user = receive_message(client)
        curr_number = [int(x) for x in generate_numbers().split(',')]
        split_input_user = input_user.split(r"\r\n")
        guess = split_input_user[-1].split("\r\n\r\n")[0]
        guess = guess[2:]

        good_guesses = 0
        for i in guess:
            if i in curr_number:
                good_guesses += 1
        if good_guesses > 0:
            message = f'[SERVER] You won!, you guessed: {good_guesses}'
            response = generate_request(mode="s", message=message)
            send_message(client, response)
            add_to_history(guess, curr_number)
            with open(r'./history.txt', 'r') as file:
                history = (file.read())
                " ".join(history)
            send_message(client, history)

        else:
            message = f'[SERVER] You lost!'
            response = generate_request(mode="s", message=message)
            send_message(client, response)

            add_to_history(guess, curr_number)
            with open(r'./history.txt', 'r') as file:
                history = (file.read())
            send_message(client, history)

    s.close()

