import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import Image, ImageTk
from Logica.mago import Mago
from Logica.clerigo import Clerigo
from Logica.raza import Raza

ASSETS_DIR = Path(__file__).resolve().parent / "assets"

RESAMPLE = Image.Resampling.LANCZOS 

class FramePersonajes(ttk.Frame):
    def __init__(self, container, lista_personajes, callback_actualizar):
        super().__init__(container)
        self.lista_personajes = lista_personajes
        self.callback_actualizar = callback_actualizar
        self.sprite_refs = []

        self.sprites = {
            "Mago": self._cargar_sprite("mago.png"),
            "Clerigo": self._cargar_sprite("clerigo.png")
        }

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        creacion_frame = ttk.LabelFrame(self, text="Crear Personaje", padding="10", style="Role.TLabelframe")
        creacion_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.crear_widgets_creacion(creacion_frame)

        self.display_frame = ttk.LabelFrame(self, text="Personajes Creados", padding="10", style="Role.TLabelframe")
        self.display_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self._configurar_area_scroll()

    def _configurar_area_scroll(self):
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.rowconfigure(0, weight=1)

        self.display_canvas = tk.Canvas(
            self.display_frame,
            bg="#1c1c24",
            bd=0,
            highlightthickness=0
        )
        self.display_canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.display_frame, orient="vertical", command=self.display_canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(6, 0))

        self.display_canvas.configure(yscrollcommand=scrollbar.set)

        self.cards_container = ttk.Frame(self.display_canvas, style="Card.TFrame")
        self.cards_window = self.display_canvas.create_window((0, 0), window=self.cards_container, anchor="nw")

        self.cards_container.bind("<Configure>", self._ajustar_scroll_region)
        self.display_canvas.bind("<Configure>", self._ajustar_ancho_canvas)

    def _ajustar_scroll_region(self, event):
        self.display_canvas.configure(scrollregion=self.display_canvas.bbox("all"))

    def _ajustar_ancho_canvas(self, event):
        self.display_canvas.itemconfig(self.cards_window, width=event.width)

    def _cargar_sprite(self, nombre_archivo):
        ruta = ASSETS_DIR / nombre_archivo
        if ruta.exists():
            imagen = Image.open(ruta).convert("RGBA").resize((84, 126), RESAMPLE)
            return ImageTk.PhotoImage(imagen)
        return None

    def crear_widgets_creacion(self, container):
        container.columnconfigure(1, weight=1)

        ttk.Label(container, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.nombre_var, style="Role.TEntry").grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(container, text="Raza:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.raza_var = tk.StringVar()
        razas = [raza.name for raza in Raza if raza != Raza.NINGUNA]
        ttk.Combobox(container, textvariable=self.raza_var, values=razas, state="readonly", style="Dark.TCombobox").grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(container, text="Clase:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.clase_var = tk.StringVar()
        clases = ["Mago", "Clerigo"]
        ttk.Combobox(container, textvariable=self.clase_var, values=clases, state="readonly", style="Dark.TCombobox").grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        ttk.Button(container, text="Crear", command=self.crear_personaje, style="Accent.TButton").grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

    def crear_personaje(self):
        if len(self.lista_personajes) >= 4:
            messagebox.showwarning("Límite alcanzado", "No puedes crear más de 4 personajes.")
            return

        nombre = self.nombre_var.get()
        raza_str = self.raza_var.get()
        clase_str = self.clase_var.get()

        if not nombre or not raza_str or not clase_str:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        if any(p.nombre.lower() == nombre.lower() for p in self.lista_personajes):
            messagebox.showerror("Nombre repetido", "Ya existe un personaje con ese nombre.")
            return

        raza = Raza[raza_str]
        personaje = Mago(nombre=nombre, raza=raza) if clase_str == "Mago" else Clerigo(nombre=nombre, raza=raza)

        self.lista_personajes.append(personaje)
        self.actualizar_display_personajes()
        self.callback_actualizar()

    def actualizar_display_personajes(self):
        for widget in self.cards_container.winfo_children():
            widget.destroy()
        self.sprite_refs.clear()

        if not self.lista_personajes:
            ttk.Label(self.cards_container, text="Aún no hay héroes en el reino.", style="CardText.TLabel").pack(anchor="center", pady=10)
            return

        for personaje in self.lista_personajes:
            card = ttk.Frame(self.cards_container, style="Card.TFrame", padding=12)
            card.pack(fill="x", expand=True, padx=2, pady=4)

            sprite = self.sprites.get(personaje.__class__.__name__)
            if sprite:
                imagen_label = ttk.Label(card, style="CardImage.TLabel")
                imagen_label.config(image=sprite)
                imagen_label.pack(side="left", padx=(0, 6), pady=2)
                self.sprite_refs.append(sprite)

            content = ttk.Frame(card, style="Card.TFrame")
            content.pack(side="left", fill="both", expand=True)

            titulo = f"{personaje.nombre} · {personaje.__class__.__name__} · {personaje.raza.name}"
            ttk.Label(content, text=titulo, style="CardTitle.TLabel").pack(anchor="w")
            ttk.Separator(content, orient="horizontal").pack(fill="x", pady=(4, 8))

            info = (
                f"Vida: {personaje.vida_actual}/{personaje.vida_maxima}\n"
                f"Fuerza: {personaje.fuerza}\n"
                f"Inteligencia: {personaje.inteligencia}"
            )
            ttk.Label(content, text=info, style="CardText.TLabel", justify=tk.LEFT).pack(anchor="w")