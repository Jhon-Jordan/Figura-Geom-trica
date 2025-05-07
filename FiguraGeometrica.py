class Figura_Geomeometrica:
    def __init__(self,alto, ancho):
        self._alto = alto
        self._ancho = ancho
    def get_alto(self):
        return self._alto
    def set_alto(self):
        self._alto= alto
    def get_ancho(self):
        return self._ancho
    def set_ancho(self):
        self._ancho= ancho
    def __str__(self):
        return f'Alto: {self._alto}, Ancho: {self._ancho}'

