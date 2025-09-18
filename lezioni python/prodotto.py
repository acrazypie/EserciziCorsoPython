"""
Crea una classe Prodotto che rappresenti un articolo in un negozio.
Il prodotto deve avere un nome e un prezzo.
Il prezzo non può essere negativo e deve essere gestito con la decoratore @property.
Il nome può essere impostato solo una volta durante la creazione.

Compiti:
Definisci la classe Prodotto.
Implementa il costruttore __init__ per nome e prezzo. Rendi __nome e __prezzo attributi privati.
Usa @property per nome in modo che sia di sola lettura.
Usa @property e @prezzo.setter per gestire l'attributo prezzo, assicurandoti che non possa essere impostato su un valore negativo.
Se si tenta di impostare un prezzo negativo, stampa un errore e mantieni il prezzo precedente.

Crea un'istanza di Prodotto, prova a impostare un prezzo valido e poi un prezzo non valido.
Prova anche a modificare il nome.
"""


class Prodotto:
    def __init__(
        self,
        nome: str,
        prezzo: float,
    ) -> None:
        self.__nome = nome
        self.__prezzo = prezzo

    @property
    def nome(self):
        return self.__nome

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, new_prezzo: float):
        if new_prezzo <= 0:
            print("Prezzo troppo basso o negativo!")
            return
        self.__prezzo = new_prezzo

    # Personalizza il print() di un oggetto
    def __str__(self) -> str:
        return f"Prodotto: {self.__nome} - {self.__prezzo}€"


prod1 = Prodotto("Carote", 2.34)
prod2 = Prodotto("Spaghetti", 2.72)

prod1.prezzo = 1.2
print(prod1)

prod2.prezzo = 0
print(prod2)

# prod1.nome = "Banane" -> ERRORE
