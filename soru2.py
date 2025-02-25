def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == '-':
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == '*':
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == '/':
        if sayi2 == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
        else:
            print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Geçersiz işlem türü!")


hesap_makinesi(5, 3, '+')  
hesap_makinesi(10, 2, '/') 
hesap_makinesi(4, 0, '/')   
hesap_makinesi(6, 2, '%')   
