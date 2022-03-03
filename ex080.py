list = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {list}')