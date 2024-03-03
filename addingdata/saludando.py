import sys
sys.path.append("..")

from manim import *
from testing import test01

matriz = [['X', 'O', 'X'],
         ['O', 'X', 'X'],
         ['O', 'X', 'O']]

code = """def saludo(nombre):
    return f"Hola {nombre}"

print (saludo("pedro"))"""

class saludando(Scene):
    def construct(self):
        self.play(test01.SALUDO)

class tabla(Scene):
    def construct(self):
        tabla = test01.CreateTable(matriz, False)
        self.play(Create(tabla), run_time=test01.TIEMPO_LENTO)
        self.wait(2)
        self.play(Uncreate(tabla))
        self.wait(2)
        codigo = test01.RenderCode(code)
        self.play(Write(codigo))
        self.wait(1)
        self.play(Uncreate(codigo))
        variable = test01.CreateVariableEntera("Edad", 13)
        var_update = test01.updateVarValue(variable, 100)
        self.play(Write(variable))
        self.wait(2)
        self.play(var_update)
        self.wait(1)
        self.play(Uncreate(variable))
        lista = test01.CreateList([f'Elemento {i}' for i in range(0,40)])
        self.play(Create(lista))
        self.wait(1)
        self.play(Uncreate(lista))
        self.wait(2)
        ecuacion = test01.MakeEcuacion("2^2+5")
        watermark = test01.WATERMARK(0.2).to_edge(UP)
        self.play(Write(ecuacion), Create(watermark))
        self.wait(3)
        self.play(Uncreate(ecuacion), Uncreate(watermark))
        self.wait(1)
        titulo = test01.CreateTitle("Hola mundo")
        self.play(Write(titulo))
        self.wait(1)
        texto = test01.CreateText(f"<span foreground='{RED_E}'>Este</span> es un <b>mensaje</b> de <span foreground='{RED_A}'>prueba</span>")
        self.play(Write(texto))
        self.wait(1)
        self.play(*test01.BatchUncreateElements([titulo, texto]))
        self.wait(1)

class parrafo(Scene):
    def construct(self):
        parrafo = test01.CreateParagraph("Este es un texto largo diseñado para intentar programar un sistema capaz de ser controlable y evitar el overflow.")
        self.play(parrafo)
        self.wait(2)

class graficas(Scene):
    def construct(self):
        titulo = test01.CreateTitle("Funcion lineal")
        self.play(Write(titulo))
        grafico = test01.MakeFunction(x_rel=1, y_rel=1, x_axis=10, y_axis=10, step_x_axis=2, step_y_axis=2, flechas=False)
        self.play(*grafico, run_time=3)
        self.wait(2)