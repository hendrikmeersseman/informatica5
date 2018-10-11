#invoer
hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee): ')
man_duwen = input('Man van brug duwen (ja/nee): ')

if hendel_trekken == 'ja' and man_duwen == 'ja':
    print(2)
elif hendel_trekken == 'ja' and man_duwen == 'nee':
    print(1)
elif hendel_trekken == 'nee' and man_duwen == 'ja':
    print(1)
else:
    print(5)
#elif (hendel_trekken == 'nee' and man_duwen == 'ja') or (hendel_trekken == 'ja' end man_duwen == 'nee')
#elif hendel trekken != man_duwen
#moeilijkste verschuiven naar els
#beter: elif hendel_trekken == 'nee' and man_duwen == 'nee':
#   print =5
#veriabelen gebruiken