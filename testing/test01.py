import manim

TIEMPO_LENTO = 3
TIEMPO_MEDIO = 2
TIEMPO_RAPIDO = 1

def WATERMARK(opacity=1.0, text="TechAtlasDev", **kwargs):
    """
    Función para crear una marca de agua con texto.
    
    Parámetros:
        text (str): El texto de la marca de agua.
        opacity (float): La opacidad del texto, un valor entre 0 y 1.
        **kwargs: Otros argumentos opcionales para personalizar el estilo del texto.
        
    Retorna:
        Text: El objeto de texto que representa la marca de agua.
    """
    watermark = manim.Text(text, **kwargs)
    watermark.set_opacity(opacity)
    return watermark

def CreateText(text, opacidad=1):
    Text = manim.MarkupText(text, fill_opacity=opacidad)
    return Text

def CreateTitle(titulo, underline=True):
    tituloG = manim.Title(titulo, include_underline=underline)
    return tituloG

def CreateTable(matriz, borde=True):
    tabla = manim.MathTable(
        matriz,
        include_outer_lines=borde)
    return tabla

def RenderCode(code, language="python", background="window"):
    code = manim.Code(code=code, tab_width=4, background=background,
                            language=language, font="Monospace")
    return code

def CreateVariableDecimal(name, value, decimales=2):
    variable = manim.Variable(value, manim.Text(name), num_decimal_places=decimales)
    return variable

def CreateVariableEntera(name, value):
    variable = manim.Variable(value, manim.Text(name), var_type=manim.Integer)
    return variable

def updateVarValue(variable, new_value):
    """Retorna un objeto listo para ser enviado a grabar"""
    return variable.tracker.animate.set_value(new_value)

def CreateList(listData):
    lista = manim.BulletedList(*listData, height=2, width=2)
    return lista

def MakeEcuacion(ecuacion, color=manim.WHITE):
    ecuacion = manim.MathTex(ecuacion, color=color)
    return ecuacion

def BatchUncreateElements(elements:list):
    return [manim.Uncreate(i) for i in elements]

def BatchWriteElements(elements:list):
    return [manim.Write(i) for i in elements]

def BatchCreateElements(elements:list):
    return [manim.Create(i) for i in elements]

def MakeFunction(x_rel=2, y_rel=1, x_axis=10, y_axis=10, step_x_axis=2, step_y_axis=2, flechas=False):
    ejes = manim.Axes(
        x_range=[0, x_axis, step_x_axis],
        y_range=[0, y_axis, step_y_axis],
        tips=flechas,
        x_length=7*x_rel,
        y_length=7*y_rel,
        axis_config={"include_numbers":True}
    ).scale(0.7)
    grafico = ejes.plot(lambda x: x, [0, 8])
    return [manim.Create(grafico), manim.Create(ejes)]

def CreateParagraph(text, longitud=6):
    l = [" ".join(text.split()[i:i+longitud]) for i in range(0, len(text.split()), longitud)]
    return manim.Write(manim.Paragraph(*l, width=10))