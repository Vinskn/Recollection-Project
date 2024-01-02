def download_file(url):
    import requests
    import tkinter as tk
    from tkinter import filedialog

    try:
        response = requests.get(url)
        
        root = tk.Tk()
        root.withdraw()

        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        with open(path, 'wb') as file:
            file.write(response.content)

        print(f"File berhasil diunduh ke {path}")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat mengunduh file: {e}")
