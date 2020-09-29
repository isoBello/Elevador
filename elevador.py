# -*- coding: utf-8 -*-
if __name__ == "__main__":
    testes = int(input())
    while testes:
        andares, capacidade, grupo = map(int, input().split(" "))
        visitar = list(map(int, input().split(" ")))
        visitar.sort(reverse=True)
        energia = 0
        for i in range(0, len(visitar), capacidade):
            energia += (visitar[i] * 2)

        print(energia)
        testes -= 1
