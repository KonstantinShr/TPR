import math


def W(D):
    return max(0, 1.74 * math.exp(0.31 * D) - 2.4)


def A(P):
    if P <= 5:
        return 0
    if 5 < P <= 10:
        return 0.26 * math.exp(0.38 * P) - 1.75
    return P


def B(D):
    return 6.17 * math.log(D + 1.4) - 2.16


def C(P):
    return max(0, 0.08 * math.exp(0.33 * P) - 0.15)


def gen(n, arr, res):
    if n == 0:
        res.append(arr.copy())
        return None
    for i in range(7):
        arr.append(i)
        gen(n - 1, arr, res)
        arr.pop()


def calc_profit(arr):
    P = 0
    profit = 0
    for D in arr:
        W_cur = W(D)
        B_cur = B(D)
        C_cur = C(P)
        P = A(P + W_cur)
        profit += B_cur - C_cur
    if P <= 10:
        return profit
    return 0


def main():
    res = []
    gen(5, [], res)
    best_profit = 0
    ans = []
    for arr in res:
        cur_profit = calc_profit(arr)
        if cur_profit > best_profit:
            best_profit = cur_profit
            ans = arr
    print(ans)
    print(best_profit)


if __name__ == '__main__':
    main()
