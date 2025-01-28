import socket

def send_command(ip, port, command):
    try:
        # TCP kapcsolat létrehozása
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            
            # Parancs küldése az SR-201 eszköznek
            s.sendall(command.encode())
            
            # Válasz fogadása
            response = s.recv(1024).decode()
            return response
    except Exception as e:
        print(f"Hiba történt a kapcsolat során: {e}")
        return None

def parse_response(response):
    if response:
        ch1_state = "Bekapcsolva" if response[0] == "1" else "Kikapcsolva"
        ch2_state = "Bekapcsolva" if response[1] == "1" else "Kikapcsolva"
        return ch1_state, ch2_state
    return None, None

def main():
    ip = "192.168.1.100"
    port = 6722

    while True:
        print("\nVálaszd ki a műveletet:")
        print("1: Ch1 bekapcsolása")
        print("2: Ch1 kikapcsolása")
        print("3: Ch2 bekapcsolása")
        print("4: Ch2 kikapcsolása")
        print("5: Kilépés")

        choice = input("Add meg a választott művelet számát: ")

        if choice == "1":
            command = "11"
        elif choice == "2":
            command = "21"
        elif choice == "3":
            command = "12"
        elif choice == "4":
            command = "22"
        elif choice == "5":
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás. Próbáld újra!")
            continue

        # Parancs küldése és válasz feldolgozása
        response = send_command(ip, port, command)
        if response:
            ch1_state, ch2_state = parse_response(response)
            print(f"Válasz az eszköztől: {response}")
            print(f"Ch1 állapot: {ch1_state}, Ch2 állapot: {ch2_state}")
        else:
            print("Nem sikerült választ kapni az eszköztől.")

if __name__ == "__main__":
    main()
