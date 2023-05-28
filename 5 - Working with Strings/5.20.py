def transform(S, N):
    if len(S) > N:
        transformedS = S[-N:]
    elif len(S) < N:
        dots = "." * (N - len(S))
        transformedS = dots + S
    else:
        transformedS = S
    return transformedS

S = input("Введите строку S: ")
N = int(input("Введите число N: "))

result = transform(S, N)
print("Результат преобразования строки:", result)
