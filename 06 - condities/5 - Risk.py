#invoer
ad1 = int(input('dobbelsteen 1: '))
ad2 = int(input('dobbelsteen 2: '))
ad3 = int(input('dobbelsteen 3: '))
vd1 = int(input('dobbelsteen 4: '))
vd2 = int(input('dobbelsteen 5: '))
doden_van_a = 0
doden_van_v = 0


#sorteren variabelen
listobj = sorted([ad1, ad2, ad3], reverse=True)
ad1, ad2, ad3 = listobj
listobj2 = sorted([vd1, vd2], reverse=True)
vd1, vd2 = listobj2

#berekening
if ad1 > vd1 and ad2 > vd2:
    print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
elif ad1 <= vd1 and ad2 <= vd2:
    print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
else:
    print('aanvaller verliest 1 leger, verdediger verliest 1 leger')