slovarik = dict()


def f(n):
    if n in slovarik:
        return slovarik[n]
    if n <= 5:
        slovarik[n] = 1
    elif n > 5:
        slovarik[n] = n + f(n - 2)


for n in range(1, 2300 + 1):
    f(n)
res = f(2128) - f(2122)
print(res)

# 6378