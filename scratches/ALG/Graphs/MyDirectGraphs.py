"""
    struttura dati di grafo direzionato

    per esercizio applico bfs al controllo dei cicli
"""

class MyDirectGraphs:
    def __init__(self):
        self.grafo = {}
        self.num_vertici = 0
        self.num_link = 0

    def aggiungiVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
            self.num_vertici += 1
    def aggiungiDirectLink(self, vertice1, vertice2):
        self.aggiungiVertice(vertice1)
        self.aggiungiVertice(vertice2)

        if vertice2 not in self.grafo[vertice1]:
            self.grafo[vertice1].append(vertice2)
            self.num_link += 1

    def getPrimo(self):
        return self.grafo[0]

    def getViciniUscenti(self, vertice):
        return self.grafo[vertice]


    # con bfs
    def controllaCicli(self):
        primo = self.getPrimo()
        trovati = list()

        trovati.append(primo)
        for i in range(self.num_vertici):
            for element in trovati:
                for node in self.getViciniUscenti(element):
                    if node in trovati:
                        return True
                    trovati.append(node)
        return False



    def printGrafo(self):
        for nodo in self.grafo:
            print(f"f: {nodo} --> {self.grafo[nodo]}")


g = MyDirectGraphs()
g.aggiungiDirectLink(1, 2)
g.aggiungiDirectLink(1, 3)
g.aggiungiDirectLink(1, 4)  # Crea un ciclo

print("Ha cicli?", g.controllaCicli())
g.printGrafo()






