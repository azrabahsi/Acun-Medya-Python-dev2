def asal_mi(sayi):
    if sayi < 2:
        print(f'{sayi} bir asal sayı değildir.')
    elif sayi == 2:
        print(f'{sayi} bir asal sayıdır.')
    else:
        for i in range(2, sayi):
            if (sayi % i == 0):
                print(f'{sayi} bir asal sayı değildir.')
                break
            else:
                print(f'{sayi} bir asal sayıdır.')
                break
asal_mi(7)
asal_mi(10)    