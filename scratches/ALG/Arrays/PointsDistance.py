import math
import random

class Punto:
    def __init__(self, x, y):
        """Inizializza un punto con le coordinate (x, y)."""
        self.x = x
        self.y = y

    def calcolaDistanza(self, altro_punto):
        """Calcola la distanza euclidea tra il punto corrente e un altro punto."""
        # Calcoliamo la differenza delle coordinate
        dx = self.x - altro_punto.x
        dy = self.y - altro_punto.y

        # Applichiamo la formula della distanza euclidea
        distanza = math.sqrt(dx ** 2 + dy ** 2)
        return distanza

def pointsDistance(points):
    # Inizializziamo la distanza minima con un valore molto alto
    minimum = float('inf')

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            # Calcoliamo la distanza tra i due punti
            distance = points[i].calcolaDistanza(points[j])

            # Aggiorniamo la distanza minima
            if distance < minimum:
                minimum = distance

    return minimum


dimensione = random.randint(1, 10)

arrayPuntiRandom = [Punto(random.randint(1, 100), random.randint(1, 100)) for _ in range(dimensione)]


for punto in arrayPuntiRandom:
    print(f"Punto({punto.x}, {punto.y})")

minimo = pointsDistance(arrayPuntiRandom)
print(f"Distanza Minima: {minimo}")
