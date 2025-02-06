import tkinter as tk
from tkinter import messagebox
import socket

def send_command(ip, port, command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(command.encode())
            response = s.recv(1024).decode()
            return response
    except Exception as e:
        messagebox.showerror("Hiba", f"Hiba történt a kapcsolat során: {e}")
        return None

def parse_response(response):
    if response:
        ch1_state = "Bekapcsolva" if response[0] == "1" else "Kikapcsolva"
        ch2_state = "Bekapcsolva" if response[1] == "1" else "Kikapcsolva"
        return ch1_state, ch2_state
    return "Ismeretlen", "Ismeretlen"

def update_status():
    response = send_command(IP, PORT, "00")  # Állapotlekérdezés parancs
    if response:
        ch1_state, ch2_state = parse_response(response)
        label_ch1.config(text=f"Ch1: {ch1_state}")
        label_ch2.config(text=f"Ch2: {ch2_state}")

def command_action(command):
    response = send_command(IP, PORT, command)
    if response:
        update_status()

IP = "192.168.1.100"
PORT = 6722

root = tk.Tk()
root.title("IoT Eszközvezérlő")
root.geometry("300x250")

label_ch1 = tk.Label(root, text="Ch1: Ismeretlen", font=("Arial", 12))
label_ch1.pack(pady=5)
label_ch2 = tk.Label(root, text="Ch2: Ismeretlen", font=("Arial", 12))
label_ch2.pack(pady=5)

tk.Button(root, text="Ch1 Bekapcsolás", command=lambda: command_action("11")).pack(pady=5)
tk.Button(root, text="Ch1 Kikapcsolás", command=lambda: command_action("21")).pack(pady=5)
tk.Button(root, text="Ch2 Bekapcsolás", command=lambda: command_action("12")).pack(pady=5)
tk.Button(root, text="Ch2 Kikapcsolás", command=lambda: command_action("22")).pack(pady=5)
tk.Button(root, text="Frissítés", command=update_status).pack(pady=5)
tk.Button(root, text="Kilépés", command=root.quit).pack(pady=5)

update_status()
root.mainloop()
