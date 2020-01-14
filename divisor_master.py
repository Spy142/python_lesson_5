def prost_int(N):
    if N<=0: print('Введите целое число от 1 до 1000')
    if N==1:return False
    for i in range(2,(N // N**0.5),1):
        if N % i == 0:
            return False
        return True

print(prost_int(23))