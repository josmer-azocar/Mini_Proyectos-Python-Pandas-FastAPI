import tkinter as tk
from tkinter import ttk, messagebox
from Logica.hechizo import Hechizo
from Logica.mago import Mago
from Logica.clerigo import Clerigo
from Logica.Manejador_de_Exceptions import PuntosDeVidaException


class FrameAcciones(ttk.Frame):
    def __init__(self, container, lista_personajes, lista_hechizos, callback_log):
        super().__init__(container)
        self.lista_personajes = lista_personajes
        self.lista_hechizos = lista_hechizos
        self.callback_log = callback_log

        self.columnconfigure(0, weight=1)

        sel_frame = ttk.LabelFrame(self, text="Selección de Personajes", padding=10, style="Role.TLabelframe")
        sel_frame.grid(row=0, column=0, sticky="ew", padx=6, pady=(0, 10))
        sel_frame.columnconfigure(0, weight=0, minsize=150)
        sel_frame.columnconfigure(1, weight=1)
        self.crear_widgets_seleccion(sel_frame)

        acc_frame = ttk.LabelFrame(self, text="Acciones", padding=10, style="Role.TLabelframe")
        acc_frame.grid(row=1, column=0, sticky="ew", padx=6, pady=(0, 10))
        acc_frame.columnconfigure(0, weight=1, uniform="acciones")
        acc_frame.columnconfigure(1, weight=1, uniform="acciones")
        self.crear_widgets_acciones(acc_frame)

        hech_frame = ttk.LabelFrame(self, text="Gestión de Hechizos", padding=10, style="Role.TLabelframe")
        hech_frame.grid(row=2, column=0, sticky="ew", padx=6, pady=(0, 6))
        hech_frame.columnconfigure(0, weight=0, minsize=150)
        hech_frame.columnconfigure(1, weight=1)
        self.crear_widgets_hechizos(hech_frame)

    def crear_widgets_seleccion(self, container):
        ttk.Label(container, text="Personaje Actor:").grid(row=0, column=0, sticky="w", padx=(0, 6), pady=5)
        self.actor_var = tk.StringVar()
        self.actor_combo = ttk.Combobox(container, textvariable=self.actor_var, state="readonly", style="Dark.TCombobox")
        self.actor_combo.grid(row=0, column=1, sticky="ew", pady=5)

        ttk.Label(container, text="Personaje Objetivo:").grid(row=1, column=0, sticky="w", padx=(0, 6), pady=5)
        self.objetivo_var = tk.StringVar()
        self.objetivo_combo = ttk.Combobox(container, textvariable=self.objetivo_var, state="readonly", style="Dark.TCombobox")
        self.objetivo_combo.grid(row=1, column=1, sticky="ew", pady=5)

    def crear_widgets_acciones(self, container):
        ttk.Button(
            container,
            text="Rezar (Clérigo)",
            command=self.rezar,
            style="Accent.TButton"
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6), pady=5, ipady=4)

        ttk.Button(
            container,
            text="Curar (Clérigo)",
            command=self.curar,
            style="Accent.TButton"
        ).grid(row=0, column=1, sticky="ew", padx=(6, 0), pady=5, ipady=4)

    def crear_widgets_hechizos(self, container):
        ttk.Label(container, text="Nombre Hechizo:").grid(row=0, column=0, sticky="w", padx=(0, 6), pady=4)
        self.hechizo_nombre_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.hechizo_nombre_var, style="Role.TEntry").grid(row=0, column=1, sticky="ew", pady=4)

        ttk.Label(container, text="Efecto (daño):").grid(row=1, column=0, sticky="w", padx=(0, 6), pady=4)
        self.hechizo_efecto_var = tk.IntVar(value=10)
        ttk.Entry(container, textvariable=self.hechizo_efecto_var, style="Role.TEntry").grid(row=1, column=1, sticky="ew", pady=4)

        ttk.Button(container, text="Crear Hechizo", command=self.crear_hechizo, style="Accent.TButton").grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 10), ipady=4)

        ttk.Label(container, text="Hechizo a usar:").grid(row=3, column=0, sticky="w", padx=(0, 6), pady=4)
        self.hechizo_sel_var = tk.StringVar()
        self.hechizo_combo = ttk.Combobox(container, textvariable=self.hechizo_sel_var, state="readonly", style="Dark.TCombobox")
        self.hechizo_combo.grid(row=3, column=1, sticky="ew", pady=4)

        btn_frame = ttk.Frame(container, style="Main.TFrame")
        btn_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        btn_frame.columnconfigure(0, weight=1, uniform="acciones_hechizos")
        btn_frame.columnconfigure(1, weight=1, uniform="acciones_hechizos")

        ttk.Button(btn_frame, text="Aprender Hechizo", command=self.aprender_hechizo, style="Accent.TButton").grid(row=0, column=0, sticky="ew", padx=(0, 6), ipady=4)
        ttk.Button(btn_frame, text="Lanzar Hechizo", command=self.lanzar_hechizo, style="Accent.TButton").grid(row=0, column=1, sticky="ew", padx=(6, 0), ipady=4)

    def get_selected_personaje(self, combo_var):
        nombre_sel = combo_var.get()
        if not nombre_sel:
            return None
        for p in self.lista_personajes:
            if p.nombre == nombre_sel:
                return p
        return None

    def rezar(self):
        actor = self.get_selected_personaje(self.actor_var)
        if isinstance(actor, Clerigo):
            mensaje = actor.rezar()
            self.callback_log(mensaje)
        else:
            messagebox.showerror("Error de Acción", "Solo los Clérigos pueden rezar.")

    def curar(self):
        actor = self.get_selected_personaje(self.actor_var)
        objetivo = self.get_selected_personaje(self.objetivo_var)
        if not actor or not objetivo:
            messagebox.showerror("Error de Selección", "Debes seleccionar un actor y un objetivo.")
            return
        if isinstance(actor, Clerigo):
            try:
                vida_anterior = objetivo.vida_actual
                mensaje = actor.curar(objetivo)
                if objetivo.vida_actual > vida_anterior:
                    self.callback_log(mensaje)
                else:
                    self.callback_log(mensaje)
            except PuntosDeVidaException as e:
                self.callback_log(f"No se pudo curar: {e.mensaje}")
        else:
            messagebox.showerror("Error de Acción", "Solo los Clérigos pueden curar.")

    def crear_hechizo(self):
        nombre = self.hechizo_nombre_var.get()
        try:
            efecto = self.hechizo_efecto_var.get()
        except (tk.TclError, ValueError):
            messagebox.showerror("Error de Valor", "El efecto del hechizo debe ser un número entero.")
            return

        if not nombre:
            messagebox.showerror("Error", "El hechizo debe tener un nombre.")
            return
        
        nuevo_hechizo = Hechizo(nombre, efecto)
        self.lista_hechizos.append(nuevo_hechizo)
        self.actualizar_listas()
        self.callback_log(f"Hechizo '{nombre}' creado con {efecto} de efecto.")

    def aprender_hechizo(self):
        actor = self.get_selected_personaje(self.actor_var)
        nombre_hechizo = self.hechizo_sel_var.get()

        if not isinstance(actor, Mago):
            messagebox.showerror("Error de Acción", "Solo los Magos pueden aprender hechizos.")
            return
        if not nombre_hechizo:
            messagebox.showerror("Error de Selección", "Debes seleccionar un hechizo para aprender.")
            return
        
        hechizo_obj = next((h for h in self.lista_hechizos if h._nombre == nombre_hechizo), None)
        if hechizo_obj:
            mensaje = actor.aprenderHechizo(hechizo_obj)
            self.callback_log(mensaje)

    def lanzar_hechizo(self):
        actor = self.get_selected_personaje(self.actor_var)
        objetivo = self.get_selected_personaje(self.objetivo_var)
        nombre_hechizo = self.hechizo_sel_var.get()

        if not isinstance(actor, Mago):
            messagebox.showerror("Error de Acción", "Solo los Magos pueden lanzar hechizos.")
            return
        if not objetivo:
            messagebox.showerror("Error de Selección", "Debes seleccionar un objetivo.")
            return
        if not nombre_hechizo:
            messagebox.showerror("Error de Selección", "Debes seleccionar un hechizo para lanzar.")
            return
        
        mensaje = actor.lanzarHechizo(objetivo, nombre_hechizo)
        self.callback_log(mensaje)

    def actualizar_listas(self):
        nombres_personajes = [p.nombre for p in self.lista_personajes]
        self.actor_combo['values'] = nombres_personajes
        self.objetivo_combo['values'] = nombres_personajes
        
        nombres_hechizos = [h._nombre for h in self.lista_hechizos]
        self.hechizo_combo['values'] = nombres_hechizos