import tkinter as tk
from tkinter import ttk
from frame_personajes import FramePersonajes
from frame_acciones import FrameAcciones
from frame_log import FrameLog

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        palette = {
            "bg": "#14141a",
            "panel_bg": "#1c1c24",
            "header_bg": "#1e1e28",
            "accent": "#c9aa71",
            "accent_hover": "#d7bc82",
            "button_bg": "#2a2a36",
            "text_primary": "#f4f3ef",
            "text_secondary": "#b8b6b0"
        }

        self.title("Juego de Rol - Creador de Personajes")
        self.geometry("1280x720")
        self.configure(bg=palette["bg"])
        self.minsize(1024, 576)

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background=palette["panel_bg"])
        style.configure("Main.TFrame", background=palette["panel_bg"])
        style.configure("Header.TFrame", background=palette["header_bg"])
        style.configure("Role.TLabelframe", background=palette["panel_bg"], foreground=palette["accent"], padding=10)
        style.configure("Role.TLabelframe.Label", background=palette["header_bg"], foreground=palette["accent"], font=("Cinzel", 11, "bold"))
        style.configure("Card.TFrame", background="#22222f", borderwidth=0)
        style.configure("CardTitle.TLabel", background="#22222f", foreground=palette["accent"], font=("Cinzel", 12, "bold"))
        style.configure("CardText.TLabel", background="#22222f", foreground=palette["text_secondary"], font=("Verdana", 10))
        style.configure("CardImage.TLabel", background="#22222f")
        style.configure("Title.TLabel", background=palette["header_bg"], foreground=palette["accent"], font=("Cinzel", 18, "bold"))
        style.configure("Subtitle.TLabel", background=palette["header_bg"], foreground=palette["text_secondary"], font=("Verdana", 10))
        style.configure("TLabel", background=palette["panel_bg"], foreground=palette["text_primary"], font=("Verdana", 10))
        style.configure("Accent.TButton", background=palette["button_bg"], foreground=palette["accent"], font=("Verdana", 10, "bold"))
        style.configure("Accent.TButton", background=palette["button_bg"], foreground=palette["accent"], font=("Verdana", 10, "bold"), padding=(14, 10))
        style.configure("Role.TEntry", fieldbackground="#242431", foreground=palette["text_primary"], insertcolor=palette["text_primary"])
        style.configure("Dark.TCombobox", fieldbackground="#242431", background="#242431", foreground=palette["text_primary"])
        style.map("Dark.TCombobox", fieldbackground=[("readonly", "#242431")], foreground=[("readonly", palette["text_primary"])])

        self.personajes_creados = []
        self.hechizos_creados = []

        main_frame = ttk.Frame(self, padding="15", style="Main.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)

        header_frame = ttk.Frame(main_frame, style="Header.TFrame", padding=(15, 12))
        header_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        ttk.Label(header_frame, text="Crónicas del Reino", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header_frame, text="Forja héroes, domina hechizos y restaura la esperanza del reino.", style="Subtitle.TLabel").pack(anchor="w", pady=(2, 0))

        separator = ttk.Separator(main_frame, orient="horizontal")
        separator.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(6, 12))
        main_frame.columnconfigure(0, weight=2, minsize=420)
        main_frame.columnconfigure(1, weight=2, minsize=420)
        main_frame.columnconfigure(2, weight=1, minsize=360)
        main_frame.rowconfigure(2, weight=1)

        frame_personajes = FramePersonajes(main_frame, self.personajes_creados, self.actualizar_frames)
        frame_personajes.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.frame_acciones = FrameAcciones(main_frame, self.personajes_creados, self.hechizos_creados, self.actualizar_log)
        self.frame_acciones.grid(row=2, column=1, padx=(10, 30), pady=10, sticky="nsew")

        self.frame_log = FrameLog(main_frame)
        self.frame_log.grid(row=2, column=2, padx=(0, 10), pady=10, sticky="nsew")

    def actualizar_log(self, mensaje):
        self.frame_log.agregar_mensaje(mensaje)
        self.actualizar_frames()

    def actualizar_frames(self):
        self.frame_acciones.actualizar_listas()
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Frame):
                for sub_widget in widget.winfo_children():
                    if isinstance(sub_widget, FramePersonajes):
                        sub_widget.actualizar_display_personajes()