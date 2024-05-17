N = int(input())

for i in range(1, N + 1):
    str_i = str(i)
    clap = str_i.count('3') + str_i.count('6') + str_i.count('9')
    
    if clap == 0:
        print(str_i, end = ' ')
    else:
    	print("-" * clap, end = ' ')