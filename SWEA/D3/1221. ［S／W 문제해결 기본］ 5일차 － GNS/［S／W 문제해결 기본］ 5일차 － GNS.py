num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
       'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

t = int(input())

for tc in range(1, t + 1):
    t_num = list(input().split())
    word = list(input().split())
    sorted_word = []

    for i in word:
        sorted_word.append((num[i], i))

    sorted_word.sort()

    print(f"#{tc}", end=' ')
    for i in range(int(t_num[1])):
        print(sorted_word[i][1], end=' ')
    print()
