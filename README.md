# Personalizacja i Systemy Rekomendacyjne

Zadania realizowane w ramach kursu Personalizacja i Systemy Rekomendacyjne na Politechnice Wrocławskiej
## Zadanie 1
Podstawowe metody tworzenia systemów rekomendacyjnych

Przedstawiono 3 podejścia:
- **Collaborative Filtering** - podaejście bazujące na iterakcjach pomiędzy użytkownikami a obiektami. Interakcją może być ocena lub sam fakt jej zajścia. Wykorzystana została bibloteka surprise i zbadany model KNN oraz modele faktoryzacji macieerzy SVD i NFD
- **Content-based filtering** - podejście bazujące na informacji o produkcie nie biorąc pod uwagę opinie i interakcji z innymi użytkownikami. Znajdują zastosowanie w sytuacji, gdy znamy dane o przedmiocie, a nie użytkowniku. Jako reprezentacje przedmiotów wykorzystano algorytm TF-IDF bazując na rodzaju filmów.
- **KNN**

## Zadanie 2
Zaawansowane metody tworzenia systemów rekomendacyjnych

Przedstawiono 3 podejścia:
- **Reguły asocjacyjne** - podejście bazuje na zliczaniu częstotliwości grup filmów, które są lubiane przez każdego z użytkowników. Na podstawie tego tworzone są potencjalne reguły asocjacyjne, które następnie są weryfikowane na zbiorze treningowym. Otrzymane reguły składają się z przesłanek i konkluzji.
- **Modele głębokie** - przebadane metody udostępnione w ramach bibioteki Spotlight zarówno metody faktoryzacji przy urzyciu ukrytej reprezentacji sieci neuronowej jak i głębokie metody sekwencyjne
- **Sekwencyjne systemy rekomendacyjne** - grupa rozwiązań uwzględniająca sekwencyjność danych. Przedstawiono podejście z wykorzystaniem sieci konwolucyjnych opisane jako Convolutional Sequence Embedding Recommendation Mode (Caser).
 Metoda ta polega na reprezentacji przedmiotów za pomocą wektorów osadzeń. Następnie dla uporządkowanych chronologicznie danych tworzona jest macierz, która jest przetwarzana przez sieć konwolucyjną w celu uchwycenia preferencji użytkownika i uwzględnieniu sekwencyjności danych.
 
## Dataset
Badania przeprowadzono na zbiorach **[MovieLens](http://files.grouplens.org/datasets/movielens/)**
