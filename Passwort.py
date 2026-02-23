import tkinter as tk
from tkinter import messagebox

def show_main_page(root, master_password):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Hauptseite")
    root.configure(bg="#fbbf24")

    tk.Label(root, text=" Willkommen!", bg="#fbbf24", font=("Arial", 20, "bold")).pack(pady=20)
    tk.Label(root, text="Fügen Sie Ihre Passwörter hinzu.", bg="#fbbf24", font=("Arial", 14)).pack(pady=3)

    
    form = tk.Frame(root, bg="#fbbf24")
    form.pack(pady=20)

    tk.Label(form, text="App Name:", bg="#fbbf24", font=("Arial", 13)).grid(row=0, column=0, padx=10, pady=8, sticky="w")
    app_entry = tk.Entry(form, font=("Arial", 13), width=25)
    app_entry.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(form, text="Passwort:", bg="#fbbf24", font=("Arial", 13)).grid(row=1, column=0, padx=10, pady=8, sticky="w")
    pw_entry = tk.Entry(form, font=("Arial", 13), width=25, show="•")
    pw_entry.grid(row=1, column=1, padx=10, pady=8)

    status = tk.Label(root, text="", bg="#fbbf24", font=("Arial", 11))
    status.pack()

    
    tk.Label(root, text="Gespeicherte Einträge:", bg="#fbbf24", font=("Arial", 13, "bold")).pack(pady=(16, 4))

    list_frame = tk.Frame(root, bg="#fbbf24")
    list_frame.pack(fill="both", expand=True, padx=20)

    entries = []

    def refresh_list():
        for widget in list_frame.winfo_children():
            widget.destroy()

        if not entries:
            tk.Label(list_frame, text="Noch keine Einträge.", bg="#fbbf24",
                     font=("Arial", 11), fg="gray").pack(anchor="w")
            return

        for i, (app, pw) in enumerate(entries):
            row = tk.Frame(list_frame, bg="#f59e0b", pady=6, padx=10)
            row.pack(fill="x", pady=3)

            tk.Label(row, text=f" {app}", bg="#f59e0b",
                     font=("Arial", 12, "bold")).pack(side="left")

            pw_var = tk.StringVar(value="••••••")
            visible = [False]
            pw_lbl = tk.Label(row, textvariable=pw_var, bg="#f59e0b", font=("Arial", 12))
            pw_lbl.pack(side="left", padx=10)

            def toggle(v=pw_var, p=pw, s=visible):
                s[0] = not s[0]
                v.set(p if s[0] else "••••••")

            def delete(idx=i):
                entries.pop(idx)
                refresh_list()

            tk.Button(row, text="👁", relief="flat", bg="#f59e0b",
                      font=("Arial", 12), cursor="hand2", command=toggle).pack(side="right")
            tk.Button(row, text="🗑", relief="flat", bg="#f59e0b", fg="red",
                      font=("Arial", 12), cursor="hand2", command=delete).pack(side="right", padx=4)

    def save_entry():
        app = app_entry.get().strip()
        pw  = pw_entry.get().strip()
        if not app or not pw:
            status.config(text="⚠ Bitte beide Felder ausfüllen.", fg="red")
            return
        entries.append((app, pw))
        app_entry.delete(0, "end")
        pw_entry.delete(0, "end")
        status.config(text=f"✔ '{app}' gespeichert!", fg="green")
        refresh_list()

    tk.Button(root, text="+ Speichern", font=("Arial", 13, "bold"),
              bg="white", relief="flat", padx=12, pady=6,
              cursor="hand2", command=save_entry).pack(pady=10)

    refresh_list()


def show_password_page(root):
    root.title("Passwort speichern")
    root.geometry("500x400")
    root.configure(bg="#fbbf24")

    pw1_var = tk.StringVar()
    pw2_var = tk.StringVar()

    tk.Label(root, text="Bitte Passwort erstellen", bg="#fbbf24",
             font=("Arial", 16)).pack(padx=10, pady=20)

    entry1 = tk.Entry(root, textvariable=pw1_var, width=40, font=("Arial", 16), show="•")
    entry1.pack(padx=10, pady=10, ipady=5)

    tk.Label(root, text="Passwort bestätigen", bg="#fbbf24",
             font=("Arial", 16)).pack(padx=10, pady=10)

    entry2 = tk.Entry(root, textvariable=pw2_var, width=40, font=("Arial", 16), show="•")
    entry2.pack(padx=20, pady=10, ipady=6)

    def check_password():
        if pw1_var.get() == pw2_var.get() and pw1_var.get() != "":
            show_main_page(root, pw1_var.get())
        else:
            messagebox.showerror("Fehler", "Passwörter sind nicht gleich")

    tk.Button(root, text="Speichern", font=("Arial", 14),
              command=check_password).pack(pady=20)


root = tk.Tk()
show_password_page(root)
root.mainloop()

