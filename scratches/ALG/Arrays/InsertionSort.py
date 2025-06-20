#Complessità
#

def insertionSort(A):
    # Scorri da 1 fino alla fine dell'array
    for i in range(1, len(A)):  # Inizia da 1 perché l'elemento 0 è già considerato ordinato
        card = A[i]  # L'elemento corrente da inserire
        j = i - 1  # L'indice dell'elemento a sinistra di card

        # Sposta gli elementi che sono più grandi di card verso destra
        while j >= 0 and A[j] > card:
            A[j + 1] = A[j]  # Sposta l'elemento a destra
            j = j - 1  # Vai all'elemento precedente

        # Inserisci card nella posizione corretta
        A[j + 1] = card



array = [1, 5, 2, 5, 6]

insertionSort(array)

print(array)



