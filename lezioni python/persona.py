class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta

    @property
    def eta(self):
        return self.__eta

    @property
    def nome(self):
        return self.__nome

    def __controlloEta(self, etaNew):
        if etaNew < 1:
            print("eta non consentita")
            return False
        return True

    @eta.setter  # Il setter per 'eta'
    def eta(self, nuova_eta):
        self.__eta = nuova_eta


persona1 = Persona("Paolo", 500)

print(persona1.eta)

persona1.eta = 200
