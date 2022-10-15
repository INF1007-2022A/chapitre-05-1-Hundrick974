#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    number = (number*number)**(1/2)  
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    for letter in prefixes:
        liste.append(letter + suffixe)
    return liste


def prime_integer_summation() -> int:
    somme = 0
    compteur = 0
    nombre = 2
    while compteur < 100:
        for i in range(nombre-1, 0, -1):
            if nombre % i == 0:
                break
        if i == 1:
            somme += nombre
            compteur += 1
        nombre += 1
    return somme


def factorial(number: int) -> int:
    factoriel = 1
    while number != 1:
        factoriel *= number
        number -= 1
    return factoriel


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue

        print(i)


def verify_ages(groups: list[list[int]]) -> list[bool]:
    result = ""
    space = " "
    for groupe in groups:
        if len(groupe) <= 3 or len(groupe) > 10:
            result += str(False) + space
            continue
        if 25 in groupe:
            result += str(True) + space
            continue
        if min(groupe) < 18:
            result += str(False) + space
            continue
        if max(groupe) > 70 and 50 in groupe:
            result += str(False) + space
            continue
        result += str(True) + space
    return [result.split()]


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
