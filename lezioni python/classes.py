class Libro:
    def __init__(
        self, titolo: str, autore: str, genere: str, copie_vendute: int
    ) -> None:
        self.titolo = titolo
        self.autore = autore
        self.genere = genere
        self.copie_vendute = copie_vendute

    def descrizione(self):
        return f"{self.titolo} scritto da {self.autore}, un libro {self.genere} che ha venduto {self.copie_vendute} copie."

    def aumento_copie_vendute(self, aumento: int):
        self.copie_vendute += aumento


lib1 = Libro("Il Sognatore", "Lainy Taylor", "fantasy", 300)
print(lib1.descrizione())

lib1.aumento_copie_vendute(50)
print(lib1.descrizione())
