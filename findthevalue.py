# p n and m are intergers
# p^n + 3600 = m^2


def main():
    n = 1
    m = 1
    p = 1
    for n in range(1, 600):
        for m in range(1, 600):
            for p in range(1, 600):
                if p**n + 3600 == m**2:
                    print(p, n, m)
                    return
                else:
                    print(f"not found we are at {p} {n} {m}")


if __name__ == "__main__":
    main()
