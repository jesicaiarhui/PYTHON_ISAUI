import tkinter as tk
from tkinter import font
import random
import threading
import time
from tkinter import messagebox

class JuegoTrivia:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("40 años ISAUI")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0, 0)
        self.ventana.iconbitmap("logo_isaui.ico")
        self.ventana.configure(bg="black")

        self.preguntas = []
        self.preguntas_seleccionadas = []
        self.pregunta_actual = 0
        self.respuestas_correctas = 0
        self.tiempo_inicial = 0
        self.tiempo_transcurrido = 0

        self.mostrar_interfaz_inicio()

    def mostrar_interfaz_inicio(self):
        
        self.mi_fuente = font.Font(family="Helvetica", size=50, weight="bold", slant="italic")

        self.etiqueta_bienvenida = tk.Label(self.ventana, text="¡Bienvenido a la Trivia ISAUI!", font=self.mi_fuente, bg="black", fg="white")
        self.etiqueta_bienvenida.pack(padx=20, pady=200)

        boton_play = tk.Button(self.ventana, text="Comenzar", font=("Arial", 20), command=self.iniciar_juego, bg="black", fg="white")
        boton_play.pack(pady=20)



        self.ventana.mainloop()

    def cambiar_color(self):
        if hasattr(self, "etiqueta_bienvenida"):
            color = self.colores.pop(0)
            self.colores.append(color)
            self.etiqueta_bienvenida.config(fg=color)
            self.ventana.after(1000, self.cambiar_color)

    def iniciar_juego(self):
        self.etiqueta_bienvenida.destroy()

        self.preguntas = obtener_preguntas()
        self.preguntas_seleccionadas = self.preguntas
        self.respuestas_correctas = 0

        self.pregunta_actual = 0
        self.tiempo_inicial = time.time()
        self.tiempo_transcurrido = 0

        self.pregunta_label = tk.Label(self.ventana, text="", wraplength=800, font=("Arial", 20), borderwidth=10, bg="black", fg="white")
        self.pregunta_label.pack(padx=20, pady=20)

        self.respuestas_frame = tk.Frame(self.ventana)
        self.respuestas_frame.pack(padx=20, pady=20)
        self.respuestas_frame.configure(bg="black")

        self.botones_respuestas = []
        for i in range(3):
            boton = tk.Button(self.respuestas_frame, text="", font=("Arial", 16), borderwidth=10, bg="medium spring green", fg="black")
            boton.pack(pady=10)
            boton.config(command=lambda btn=boton: self.verificar_respuesta(btn.cget("text")))
            self.botones_respuestas.append(boton)

        self.feedback_label = tk.Label(self.ventana, text="", font=("Arial", 16), fg="green", bg="black")
        self.feedback_label.pack(pady=20)

        self.tiempo_label = tk.Label(self.ventana, text="Tiempo: 0 segundos", font=("Arial", 16), bg="black", fg="white")
        self.tiempo_label.pack(pady=20)

        self.thread = threading.Thread(target=self.actualizar_tiempo)
        self.thread.daemon = True
        self.thread.start()

        self.actualizar_pregunta()

        cerrar_boton = tk.Button(self.ventana, text="Cerrar", font=("Arial", 16), command=self.cerrar_ventana, bg="black", fg="white")
        cerrar_boton.pack(side="right", padx=20, pady=20)

        self.boton_siguiente = tk.Button(self.ventana, text="Siguiente", font=("Arial", 16), state="disabled", command=self.siguiente_pregunta, bg="black", fg="white")
        self.boton_siguiente.pack(side="right", padx=20, pady=20)

    def cerrar_ventana(self):
        self.ventana.destroy()

    def actualizar_tiempo(self):
        while True:
            self.tiempo_transcurrido += 1
            tiempo_formateado = f"Tiempo: {self.tiempo_transcurrido} segundos"
            self.tiempo_label.config(text=tiempo_formateado)
            time.sleep(1)

    def verificar_respuesta(self, respuesta):
        if respuesta == self.preguntas_seleccionadas[self.pregunta_actual][1]:
            self.respuestas_correctas += 1
            self.feedback_label.config(text="¡Respuesta correcta!", fg="green")
        else:
            self.feedback_label.config(text="Respuesta incorrecta", fg="red")

        self.boton_siguiente.config(state="active")

        for boton in self.botones_respuestas:
            boton.config(state="disabled")

    def siguiente_pregunta(self):
        if self.pregunta_actual < len(self.preguntas_seleccionadas) - 1:
            self.pregunta_actual += 1
            self.actualizar_pregunta()
        else:
            mensaje = f"Juego terminado. Preguntas correctas: {self.respuestas_correctas}"
            messagebox.showinfo("Resultado", mensaje)
            self.finalizar_juego()

        self.boton_siguiente.config(state="disabled")

        for boton in self.botones_respuestas:
            boton.config(state="active")

    def generar_respuestas(self):
        pregunta, respuesta_correcta = self.preguntas_seleccionadas[self.pregunta_actual]
        respuestas = [respuesta_correcta]
        while len(respuestas) < 3:
            respuesta_incorrecta = random.choice(self.preguntas)[1]
            if respuesta_incorrecta not in respuestas:
                respuestas.append(respuesta_incorrecta)
        random.shuffle(respuestas)
        return respuestas

    def actualizar_pregunta(self):
        self.respuestas = self.generar_respuestas()
        pregunta, _ = self.preguntas_seleccionadas[self.pregunta_actual]
        self.pregunta_label.config(text=pregunta)
        for i, boton in enumerate(self.botones_respuestas):
            boton.config(text=self.respuestas[i], command=lambda respuesta=self.respuestas[i]: self.verificar_respuesta(respuesta))

    def finalizar_juego(self):
        tiempo_total = round(time.time() - self.tiempo_inicial, 2)
        # Puedes continuar aquí para guardar el puntaje y otros datos del jugador

def obtener_preguntas():
    pass

if __name__ == "__main__":
    juego = JuegoTrivia()

