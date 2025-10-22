import tkinter as tk
from tkinter import ttk

class FrameLog(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        log_frame = ttk.LabelFrame(self, text="Log de Eventos", padding="10", style="Role.TLabelframe")
        log_frame.grid(row=0, column=0, sticky="nsew")
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)

        self.log_text = tk.Text(
            log_frame,
            state="disabled",
            wrap="word",
            bg="#11111a",
            fg="#d7d5cf",
            font=("Courier New", 10),
            insertbackground="#d7d5cf",
            relief=tk.FLAT,
            borderwidth=0
        )
        self.log_text.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.log_text['yscrollcommand'] = scrollbar.set

    def agregar_mensaje(self, mensaje):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"> {mensaje}\n\n")
        self.log_text.config(state="disabled")
        self.log_text.see(tk.END)