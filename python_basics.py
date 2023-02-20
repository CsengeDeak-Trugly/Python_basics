import random
import statistics
from statistics import mode


def alapok():
    a = input('Add meg a neved! ')
    print(a)

    b = 4
    b = str(b)
    print(type(b))

    c = input('Add meg a vezetéknevedet: ')
    d = input('Add meg a keresztnevedet: ')
    e = int(input('Hány éves vagy? '))
    szülév = 2022-e 
    print('Legyen szép napod', c, d, 'Szeretlek!', 'Én már tudom is, hogy mikor születtél: ', szülév, sep='' )

    # 3 ember, 3 magasság, kiszámolni a magasságok átlagát, printelje ki az átlagot int-ként
    ember1 = int(input('Add meg a magasságodat: '))
    ember2 = int(input('Add meg a magasságodat: '))
    ember3 = int(input('Add meg a magasságodat: '))
    átlag = (ember1 + ember2 + ember3)/3

    print(int(round(átlag, 0)))


def gondolt_szam(num):
    num = 4
    tipp = int(input('Melyik számra gondoltam 1 és 5 között? '))
    tipp = int(tipp)
    if num == tipp:
        print('Sikerült eltalálnod, szép volt! ')
    else:
        print('Nem sikerült. Próbáld meg újra! ')


# password-öt bekérni, if-else jó vagy nem jó a password
def password():
    cor_password = 'Abc123'
    password = input('Add meg a jelszót: ')
    if cor_password == password:
        print('Helyes jelszó! Üdvözöljük!')
    else:
        print('Helytelen jelszó!')


# változóba 2 szám, eredményt is megadni, megkérdezni, hogy mennyi lesz a számok különbsége, ellenőrizni, h jó-e a felhasználó eredménye
def kulonbseg():
    szam1 = 15
    szam2 = 27
    különbség = szam1-szam2
    bekért = int(input('Mennyi a '+ str(szam1)+ ' és a '+ str(szam2)+ ' különbsége? '))
    if bekért == különbség:
        print('Igen, jól számoltál!')
    else:
        print('Nem sikerült kiszámolnod.')


# if-else statements függvény neve, mindent meghívunk egy új függvénybe, ami if-elset tartalmaz
def if_else_statements():
    num = 5
    gondolt_szam(num)


# külön változókba, h milyen évszak van, esik-e az eső, fúj-e a szél, menjünk-e túrázni, vagy maradunk otthon, if-else-el ha több teljesül, akk megyünk, ha másképp teljesül akk nem megyünk...
def evszak():
    evszak = input('Milyen évszak van, írd be a kezdőbetűjét? Nyár= n, ősz = ő, tél = t, tavasz = a ')
    szel = input('Fúj a szél? Írj i betűt, ha igen, n betűt, ha nem: ')
    eso = input('Esik az eső? Írj i betűt, ha igen, n betűt, ha nem: ')
    if evszak == 'n' or (evszak == 'ő' or evszak == 'a') and eso == 'n' or evszak == 't' and szel == 'n' and eso == 'n' :
        print('Akkor megyünk túrázni!')
    else:
        print('Szar idő van, maradunk a seggünkön!')


# két egész számot bekérünk, if-else-el adjuk meg az eredményt, döntse el a program, h melyik a nagyobb szám? if: művelet a válasz= 1. szám a nagyobb, írjuk ki az eredményt
def melyik_nagyobb():
    szam1 = int(input('Add meg az első számot: '))
    szam2 = int(input('Add meg a második számot: '))
    if szam1 < szam2:
        eredmény = 'A második szám a nagyobb.'
    elif szam1 == szam2:
        eredmény = 'A két szám egyenlő.'
    else:
        eredmény = 'Az első szám a nagyobb.'
    print(eredmény)


# hanyadik lett az utolsó versenyén, ha benne volt az első háromba, akk result: szép volt, dobogós lettél, ha nem akk result: lúzer vagy
def place():
    posi = int((input('What rank did you get the last race? ')))
    if posi <=3:
        result = 'Nice job. You are in top 3.'
    else:
        result = 'You are a looser.'
    print(result)




# létezik-e a háromszög
def triangle():
    print('Does the triangle exist? ')
    side1 = int(input('Enter a number please: '))
    side2 = int(input('Enter a number please: '))
    side3 = int(input('Enter a number please: '))
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        result = "This triangle does exist."
    else:
        result = "This triangle doesn't exist."
    print(result)


#while loop
def while_loop():
    a = 1
    while a != 10:
        print(a)
        a += 1


# gondoltam egy számra, találd ki, van 3 lehetőséged, írjuk ki, hogy mennyire van az eredeti számtól
def guess_num():
    correct = 5
    figured = False
    print('Guess the number between 1-5!')
    try_num = 1

    while not figured and try_num < 4:
        guess = int(input('Enter a number between 1-5: '))
        try_num += 1

        if  guess == correct:
            print('You hit the number. Nice job! ')
            figured = True
        else:
            if try_num < 4:
                print('You missed the number. ', 'You are', abs(abs(guess) - abs(correct)) , 'far from the correct number.' 'Try again! ')

            else:
                print('You missed the number. ', 'You are', abs(abs(guess) - abs(correct)) , 'far from the correct number. ''Game over. ')


def third():
    null = 0
    null2 = 0

    # x^3 - 2x^2 + 3x - 8 = 0

    while null < 100 and null > -100:
        result = null**3 - 4*null**2 + 1*null + 6
      
        if result == 0:
            print(null)
        
        null -= 1

    while null2 < 100 and null2 > -100:
        result = null2**3 - 4*null2**2 + 1*null2 + 6
        
        if result == 0:
            print(null2)
           
        null2 += 1
   

def diophantos():
    x = 0

#(x/6 + x/12 + x/7 + 5 + 4) /2 = egész szám

    while x < 100:
        result = x*(1/6 +1/12 + 1/7 + 1/2) + 5 + 4

        if result == x:
            print(x)
        
        x += 1


# gondolt szám kitalálós, random számmal, 3 próbálkozás, 1-10ig, írjuk ki milyen távol van az eredménytől a beírt szám

def rand():
    lower_limit = 1
    upper_limit = 10

    number = random.randint(lower_limit,upper_limit)
    while_num = 1
    progress = True

    while progress and while_num < 4:
        my_num = int(input('Enter a number please between ' + str(lower_limit) + ' and ' + str(upper_limit) + ': '))

        if number == my_num:
            print('You hit the number. Nice job!')
            progress = False

        elif number != my_num and while_num <3:
            print('Wrong number, your number is', abs(abs(number) - abs(my_num)), 'away from the correct number. ',  'Try again! ')

        else:
            print('Wrong number. Game over.')
    
        while_num +=1


def while_in_while():
    row = 0
    while row < 25:
        column = 0

        while column != row + 1:
            print('O', end='')
            column += 1
        print('')
        row += 1


def while_in_while_0():
    row = 0
    while row < 25:
        column = 0

        while column != row:
            print(end=' ')
            column += 1
        print('O')
        row += 1


def while_in_while_Right_Left_10():
    repeat = 0
    while repeat < 10:
        row = 0
        while row < 25:
            column = 0

            while column != row:
                print(end=' ')
                column += 1  
            print('O')   
            row += 1 
        row2 = 24

        while row2 > 0:
            column2 = 0

            while column2 != row2 - 1:
                print(end=' ')
                column2 += 1
            print('O')  
            row2 -= 1   
        repeat += 1         


def list_():
    clothes = []
    dress = None

    while dress != '':
        dress = input('Write a dress: ')

        if dress:  #a dress vagy létezik vmilyen értékkel, vagy true
            clothes.append(dress)

    print(clothes)


# lista: writers, lista: products, while, amivel hozzáadunk a writers listához, utána a while-on kívül egy for ciklus, ami belefut a writers listába (iteral), product változót a for cikluson belül
# és bekérünk a writerhez egy product-ot, hogy megadja az író egy művét a felhasználó, ezt a product változót gyűjtse bele a products listába
def writers_products():
    writers = []
    products = []
    writer = None
    product = None

    while writer != '':
        writer = input('Enter a writer: ')

        if writer:
            writers.append(writer)

    for writer2 in writers:
        product = input('Enter a ' + writer2 + ' product: ')
        products.append(product)

    #print(writers, '\n', products) sor végét így írunk

    for num in range(0, len(writers)): # len() hossza vminek 
        print(writers[num], 'wrote the', products[num]) 


# listába szavakat írni
def list2():
    list_2 = ['apple', 'pineapple', 'kiwi', 'orange', 'limon', 'lime' ]
    
    print(list_2[1]) # kiírjuk az 1-es indexű elemet (pineaple)
    list_2.append('peach') # hozzáad a listához
    print(list_2)
    list_2.pop() # kivesz belőle egy elemet, te adhatod meg, h melyiket, ha nincs semmi, akk az utolsót
    print(list_2)
    list_2.remove('kiwi') # meg kell adni, h melyiket elemet szedjük ki
    print(list_2) 
    print(list_2[-1]) # utolsó elem kiírása
    list_2.clear() #kitörli a lista elemeit
    print(list_2)
    print(list_2[0:5:2]) #slicing honnantól : meddig : hány lépés
    print(list_2)
    

def range_0():
    for sz in range(500, 1001, 2):
        print(sz, sz**2, sz**3, sz**4)


def while_0():
    sz= 500
    while sz <= 1000:
        print(sz, sz**2, sz**3, sz**4)
        sz= sz + 1


def range_1():
    for odd in range(51, 100, 2):
        print(odd)


def range_2():
    for odd2 in range(200, 99, -5):
        print(odd2)


def drawing():
    for i in range(2, 1001, 4):
        print(i)


# print: 3, 7, és még három számot
def drawing_2():
    for i in range(3, 21, 4):
        print(i)      


def drawing_3():
    for i in range(500, 399, -10):
        print(i)
    

# 0-70-ig a 7-tel osztahó számok        
def drawing_4():
    for i in range(7, 71, 7):
        print(i)
               
        
# egy sorba print(szám, szám négyzete, szám negyedik hatványa, 500-1000ig), minkét ciklussal
def example():
    for num in range(500, 1001):
        print(num, num**2, num**4)
        

def example_2():
    num = 500
    while num >= 500 and num <= 1000:
        print(num, num**2, num**4)
        num += 1


def rest():
    a = 5 / 2
    b = 5 // 2 # hány egésszer van meg benne
    c = 5 % 2  # mennyi a maradék
    print(a, b, c)
        
    
# 1,000,000 és 1,000,004 között a 7-tel osztható számok
def rest_2():
    for a in range(1000000, 1000004):
        if a % 7 == 0:
            print(a)


# 100.000Ft-om van, a bank ad évi 7% kamatot, mikor lesz 400.000Ft a pénzem?
def bank():
    money = 100000
    year = 0

    while money < 400000:
        money += money*7/100
        year += 1

    print(year)


# , listában szöveg, + alma, + narancs, minden elem szöveg mindein második karakterét kinyomtatni, for ciklus a listába megy bele még egy for ciklus a szavak elemeibe megy bele
def long():
    sentence = ['How long should it be?', 'apple', 'orange']
    counter = 0

    for words in sentence:
        print(words)    

        for characters in words:
            
            if counter % 2 == 0:
                print(characters)
            counter += 1

            
#listával az előző feladat
def long_list():
    sentence = ['How long should it be?', 'apple', 'orange']
    new_list = []

    for list_ in sentence:
        print(list_) 

        for list_char in list_:
            new_list.append(list_char)

    print(len(new_list))
    print(new_list)


def box():
    if True:
        print('Igaz')
    
    if False:
        print('Hamis')
    
    if not True:
        print('Nem igaz - azaz hamis')
    
    if not False:
        print('Nem hamis - azaz igaz')
    
    doboz = None
    if doboz: #a None logikai értéke: False
        print('1-Most van benne valami.')
    if not doboz: #a nem False az True!
        print('1-Most üres.')
    
    doboz = ''
    if doboz: #a "semmi" logikai értéke: False
        print('2-Most van benne valami.')
    if not doboz: #a nem False az True!
        print('2-Most üres.')
    
    doboz = 'ezt tettem bele'
    if doboz: #a "bármi" logikai értéke: True
        print('3-Most van benne valami.')
    if not doboz: #a nem True az False!
        print('3-Most üres.')

def loop():
    line = 0
    while line < 10:
        pillar = 0
        while pillar < 1:
            print('OOOOO', end='')
            pillar += 1
        print('')
        line += 1


def sor():
    hanyszor= 5
    for _ in range(hanyszor):
        print('O', end='')
    print('')

    meddig = 5
    for _ in range(meddig):
        print(_,_**2)


def loop2():
    # line = 0
    # while line < 1:
    #     print('+-----+')
    #     pillar = 0
    #     while pillar < 10:
    #         print('|:::::|', end='')
    #         print('')
    #         pillar += 1    
    #     line =+ 1
    # print('+-----+') 

    width = 7
    height = 12

    print('+', end='')
    for _ in range(width - 2):
        print('-', end='')
    print('+')

    for sor in range(height - 2):
        print('|', end='')
        for oszlop in range(width - 2):
            print(':', end='')
        print('|')    

    print('+', end='')
    for _ in range(width - 2):
        print('-', end='')
    print('+')



def loop__():
    sor = 12
    oszlop = 7

    print('+', end = '')
    for _ in range(oszlop - 2):
        print('-', end ='')
    print('+', end = '')
    print('')

    for a in range(sor - 2):
        print('|', end = '')
        for a in range(oszlop - 2):
            print(':', end = '')

        print('|', end = '')
        print('')

    print('+', end = '')
    for _ in range(oszlop - 2):
        print('-', end ='')
    print('+', end = '')
    


def triangle():
    emeletek = int(input('Enter a number please! '))
    for emelet in range(emeletek):

        for _ in range(emelet):
            print(' ', end='')

        for _ in range(2*(emeletek-emelet) - 1):
            print('O', end='')
        print('')


def triangle_2():
    lines = int(input('Enter a number! '))

    for line in range(lines):
        
        for _ in range(line):
            print(' ', end='')
        
        for _ in range((lines - line) * 2 - 1):
            print('O', end='')

        print('')

    line= 2
    for i in range(line):  # sorszámként adom be neki a line változót és 0-tól indul, vagyis 0. és 1. lesz benne
        print('Cseni')
        for _ in range(i):  # 0-nál nem csinál semmit, mert annyiszor írja ki a printet, amennyi a szám érétke
            print('aa')


def arrow():
    for _ in range(5):

        for line in range(7):

            for _ in range(7 - line - 1):
                print(' ', end='')          

            for _ in range(line + 1):
                print('O', end='')
            print('')

        for line2 in range(7 - 1):

            for _ in range(line2 + 1):
                print(' ', end='')          

            for _ in range(7 - line2 - 1):
                print('O', end='')
            print('')

        for line in range(7):         

            for _ in range(line + 1):
                print('O', end='')
            print('')

        for line2 in range(7 - 1):      

            for _ in range(7 - line2 - 1):
                print('O', end='')
            print('')


def block():
    width = 8
    column = 3
    height = 4
    line = 2

    for _ in range(line):
        for _ in range(height):

            for _ in range(column):

                for _ in range(width):
                    print('O', end='')
                print(' ', end='')

            print('')
        print('')
    print('')


def list_():
    cars = ['Dacia', 'Opel', 'Toyota', 'BMW', 'Mercedes', 'Audi', 'Skoda', 'Toyota', \
     'Saab', 'Mazda', 'Fiat', 'Aston Martin', 'Voldo', 'Lotus', 'Jeep']

    my_new_cars = []

    new_car = None

    while new_car != '':
        new_car = input('Enter a car brand: ')
        if new_car != '':
            my_new_cars.append(new_car)
            print(my_new_cars)
    print(my_new_cars)

    cars.extend(my_new_cars)

    print(cars)

    sell_cars = input('Enter the sell car: ')
    cars.remove(sell_cars)

    print('My cars after selling: ', cars)

    print(sell_cars, 'more left',  cars.count(sell_cars))


def list_monarchy():
    kingdoms = []
    grand_duchies = []
    duchies = []
    monarchies = []
    kingdom = None
    grand_duchy = None
    duchy = None
    plus = ['Vatican']
    
    while kingdom != '':
        kingdom = input('Enter a kingdom: ' )
        if kingdom != '':
            kingdoms.append(kingdom)
            print(kingdoms)

    while grand_duchy != '':
        grand_duchy= input('Enter a grand duchy: ' )
        if grand_duchy != '':
            grand_duchies.append(grand_duchy)
            print(grand_duchies)

    while duchy != '':
        duchy= input('Enter a duchy: ' )
        if duchy != '':
            duchies.append(duchy)
            print(duchies)

    print('Kingdoms: ', kingdoms)
    print('Grand duchies: ' ,grand_duchies)
    print('Duchies: ', duchies)

    monarchies.append(kingdoms + grand_duchies + duchies + plus)
    #monarchies.append('Vatican')
    print('Monarchies : ', monarchies)


def throws():
    numbers = []

    for _ in range(10000000):
        number = random.randint(1,6)
        numbers.append(number)
    
    print('Number 1: ', numbers.count(1), 'Number 2: ', numbers.count(2), 'Number 3: ',  numbers.count(3), 'Number 4: ',  numbers.count(4), 'Number 5: ',  numbers.count(5), 'Number 6: ', numbers.count(6))


def foglalkozasok():
    foglalkozások = ['postás', 'rendőr', 'villanyszerelő', 'a szomszéd', 'gázos', 'díjbeszedő', \
                    'handlé', 'szódás', 'képkereskedő', 'a házmester', 'a fia', 'kéményseprő']

    #slicing - szeletelés
    print(foglalkozások[1:3])
    #striding - egyelés, lépkedés
    print(foglalkozások[1:6:2])
    print(foglalkozások[::2])   # ha nem írok be semmit, akkor az elsőtől indul, és a teljes hosszán végig megy a listának
    print(foglalkozások[::-1])  # így megy végig visszafelé
    print(foglalkozások[-3:-10:-1])  # visszafelé megy végig megadott szakaszon


def foglalkozasok_gyak():
    foglalkozások = ['postás', 'rendőr', 'villanyszerelő', 'a szomszéd', 'gázos', 'díjbeszedő', \
                    'handlé', 'szódás', 'képkereskedő', 'a házmester', 'a fia', 'kéményseprő']
    
    # print(foglalkozások[2])
    # print(foglalkozások[8])
    # print(foglalkozások[6])

    # print(foglalkozások[-3])
    # print(foglalkozások[-7])
    # print(foglalkozások[-12])

    # print(foglalkozások[5:8])
    # print(foglalkozások[7:11])
    # print(foglalkozások[3:10])

    # print(foglalkozások[-3:-5:-1])
    # print(foglalkozások[-3:-10:-1])
    # print(foglalkozások[-2:-8:-1])

    # print(foglalkozások[-2:-7:-2])
    # print(foglalkozások[-3:-10:-3])
    # print(foglalkozások[2::4])
    # print(foglalkozások[-6:-11:-2])
    # print(foglalkozások[2::2])

    # print(foglalkozások[2::4])
    # print(foglalkozások[::3])
    # print(foglalkozások[::-1])
    # print(foglalkozások[-4:-11:-3])
    # print(foglalkozások[:10:3])
    # print(foglalkozások[::-3])


def string():
    string_1 = 'Mici'
    string_2 = 'mackó'

    list_1 = ['Hello' , 'Lord', 'John']
    list_2 = ['nice', 'the', 'your', 'horse' 'and', 'a', 'your', 'dress']

    # # indexelhető
    # print(string_1[2], list_1[2])

    # #szeletelhető
    # print(string_1[1:], list_1[1:])

    # # egyelhető
    # print(string_2[::2], list_2[::2])

    # print(string_1[::-1], list_1[::-1])

    # list_2.append('also')
    # print(list_2)

    # list_2.extend(list_1)
    # print(list_2)

    # print(string_1 + string_2)
    # print(list_1 + list_2)
    
    # list_2.insert(3, 'yep')
    # print(list_2)

    # list_2.remove('your')
    # print(list_2)

    # print(list_2.pop())

    my_list = 'kenyeret ettem meggyel'

    # for string in my_list:
       
    #     print(string.count('e'))
    #     print(string[::3])

    # for sentence in my_list:
    #     print(sentence[::-1])

    for char in my_list:
        print(char, ' ', end = '')

    # for char_2 in my_list:
    #     print(char_2, end='')
   

def division():  # osztási műveletek
    print(9/2)
    print(9//2)  # div, 9 div 2 nem egyenlő a division-nel
    print(9%2)  # mod, modulo
    
def fizzbuzz(): 

    for numbers in range(1, 101):
        if numbers % 5 == 0 and numbers % 3 == 0:
            print('fizzbuzz')
            #continue
        elif numbers % 5 == 0:
            print('fizz')
            #continue
        elif numbers % 3 == 0:
            print('buzz')
            #continue
        else:
            print(numbers)
       

        #print(numbers)


def odd_even():
    odd = []
    even = []

    for _ in range(1, 101):
        number = random.randint(1, 6)

        if number % 2 == 0:
            even.append(number)
            #print(even)
        else:
            odd.append(number)
            #print(odd)
    if even < odd:
        print('Rolled odd number several times. Number of odd number: ', len(odd), 'Rolled numbers: ', odd, ',', even)
    elif odd < even:
        print('Rolled even number several times. Number of even numbers: ', len(even), 'Rolled numbers: ', even, ',', odd)
    else:
        print('Rolled even number and even number the same times', 'Rolled numbers: ', even, ',', odd)


    odd_1 = 0
    even_2 = 0
    
    for _ in range(1, 101):
        number = random.randint(1 ,6)
        if number % 2 == 0:
            even_2 += 1
        else:
            odd_1 += 1      

    if even_2 < odd_1:
        print('Rolled odd number several times. Number of odd number: ', odd_1)
    elif odd_1 < even_2:
        print('Rolled even number several times. Number of even numbers: ', even_2)
    else:
        print('Rolled even number and even number the same times')


def odd_even_100():
    throw = 0
    number = 1

    while number % 2 != 0:
        number = random.randint(1, 100)
        throw += 1
        print('The rolled number is ', number, 'How many times it was thrown', throw)

    print('How many times it was even number', throw)

def gauss():
    number_list = [1, 5, 4, 5, 6, 2, 4, 6, 8]

    summa = 0

    for number in range(1, 101):  # számok összege 1-100ig
        summa += number
    print(summa)

    summa = 0

    for number in number_list:  # számlista számit adja össze
        summa += number
        #print(summa)
    print(summa)
    print(sum(number_list))    # összeadás nem kell már a ciklus
    
    summa = 0
    items = 0

    for number in range(1, 101):  # számok átlaga 1-100-ig
        summa += number
        items += 1
    print(summa / items)

    for number in number_list:  # számlista számainak átlaga ilyenkor nem kell már ciklus
        summa += number
        items += 1
    print(sum(number_list)/len(number_list))

    product = 1

    for number in range(1, 101):  # számok szorzata 1-100-ig 
        product *= number
    print(product)

    letters = ['I', 't', 's', 'a', 'l', 'l']
    text = ''

    for letter in letters:
        text += letter 
    print(text)
    print(''.join(letters))   # egyesíti a listát nem kell hozzá a for ciklus


def lists():
    li = [1, 55, 7, 16, 64164, 65, 97, 6, 65]
    al = ['ads', 'dd', 'adsplgk', 'a asdlkasd asdsad']

    print(len(li))   # lista elemszámát adja meg a len
    print(len(al))


def programing_theses():
    # list1 = [...]
    # starting_value = 0 

    # for item in list1:
    #     starting_value += item


    # list2 = [...]
    # start_value = 1

    # for item_2 in list2:
    #     start_value *= item_2

    list3 = [5, 7, 16, 64, 0]
    start_val = 0   # elemszám
    summa = 0       # összeg

    for items in list3:
        summa += items
        start_val += 1
    print(summa / start_val)

def list_methods():
    courses = ['History', 'Math', 'Physics', 'CompSci']
    courses_2 = ['Education', 'Literature']
    nums = [1, 5, 6, 7, 5, 3]
    
    print(courses)

    # courses.append('Art')  # hozzáad a végéhez elemet
  
    # courses.insert(0, courses_2)  # hozzáad a megadott helyre elemet

    # courses.insert(-1, 'Dance')  # meg kell adni egy helyet, h hova illessze az elemet

    # courses.extend(courses_2)  # egyesít két listát

    # courses.remove('Math')  # kiveszi a megadott elemet 

    # popped = courses.pop()  # elveszi az utolsó elemet, külön változóba teszi, h lehessen vele dolgozni
    # courses.pop()           # elveszi az utolsó elemet

    # courses.reverse()   # megfordítja az elemek sorrendjét

    # courses.sort()    # sorba rendezi az elemeket
    # courses.sort(reverse = True)   # fordított sorrendbe teszi az elemeket

    # nums.sort()
    # nums.sort(reverse = True)

    # print(nums)

    # sorted(courses)  # visszaadja az eredeti sorrendjét a listának
    # sorted_courses = sorted(courses)  # sorrendbe rendezi a listát

    # print(courses) 
    # print(sorted_courses)

    # print(min(nums))    # legkisebb értékét adja vissza a listának
    # print(max(nums))    # legnagyobb értékét adja vissza
    # print(sum(nums))    # összeadja az elemeket

    # print(courses.index('Math'))

    # print('Art' in courses)   # igaz vagy hamis értéket ad vissza, attól függően, h benne van-e a listában, vagy nem
    # print('Math' in courses)

    # for index, course in enumerate(courses):  # visszaadja az indexét az elemnek és az elem nevét
    #     print(index, course)

    # for index, course in enumerate(courses, start=1):   # megadhatjuk, hogy honnan indítsa az indexelést
    #     print(index, course)

    course_str = ', '.join(courses) # karakterláncot ad vissza megadott egyesítési elemekkel 
    course_str_2 = ' - '.join(courses)
    new_list = course_str.split(' - ')  # visszaadja az eredeti listát

    print(course_str)
    print(course_str_2)
    print(new_list)


def tuples_methods():

    # Mutable
    # list_1 = ['History', 'Math', 'Physics', 'CompSci']
    # list_2 = list_1

    # print(list_1)
    # print(list_2)

    # list_1[0] = 'Art'

    # print(list_1)
    # print(list_2)


    # Immutable
    tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
    tuple_2 = tuple_1

    print(tuple_1)
    print(tuple_2)

    # tuple_1[0] = 'Art'    # nem lehe megcsinálni, mert ez állandó, nem lehet megváltoztatni, nem lehet append, remove, reserve... műveleteket csinálni vele

    # print(tuple_1) 
    # print(tuple_2)


def sets_methods():

    # Sets
    cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
    art_courses = {'History', 'Math', 'Art', 'Design'}

    # print(cs_courses)
    # print('Math' in cs_courses)

    print(cs_courses.intersection(art_courses))     # megadja a közös elemeket a halmazokból
    print(cs_courses.difference(art_courses))       # megadja a halmazok különbségét
    print(cs_courses.union(art_courses))            # uniójukat adja meg


def empty():

    # Empty Lists
    empty_list = []
    empty_list = list()

    # Empty Tuples
    empty_tuple = ()
    empty_tuple = tuple()

    # Empty Sets
    empty_set = {} # This isn't right! It's a dict
    empty_set = set()


    
def list_():    # kigyűjti listába a i, j, k elemeket hármas egységekben, amik együttesen kisebbek, mint az n értéke
    x = 1
    y = 2
    z = 2
    n = 5

    # l= list()
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if (i+j+k != n):
    #                 l.append([i,j,k])
    # print(l)

    lis = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k) != n]
    print(lis) 
    # a lis változóba kigyűjtjük a ilyen formátumba: [i,j,k] az elemeket, ahol az i-t úgy kapjuk meg, hogy bejárjuk az x értékeit, 0-tól x+1-ig, j elemeinél ugyígy a y-t járjuk be , k elemeinél ugyanígy a z-t járjuk be
    # majd ha függvény miatt csak azokat írjuk ki, ahol i+j+k nem egyenlő az n értékkel
    
def names():
    name = 'kldas'
    score = 1.64

    names_grades = list()
    
    for nam in range(name):
        for sco in range(score):
            names_grades.append([nam, sco])
    print(names_grades)

def arr():
    arr = [15, 49, 65, 65, 65, 65]
    new_list = []
    
    for i in arr:
        new_list.append(i)
        
    print(new_list)

    my_set = set(new_list)
    list_2 = list(my_set)
    
    list_2.remove(max(list_2))

    print(max(list_2))


def list_64():
    numbers = [1, 5, 7, 19, 92, 64, 105, 103]

    if 64 in numbers:
        print('Yes')
    else:
        print('No')

    for num in numbers:
        if num % 2 == 0:
            print('In the list exist even number')
            break
    else:
        print('Not exist even number')

def lotto():
    lotto = [41, 49, 53, 50, 59]
    lotto_2 = [91, 64, 16, 53, 74]
    
    for num in lotto:
        if num < 40 or num > 60:
            print('Yes')
            break
    else:
        print('The all number is between 40-60.')

    for num in lotto_2:
        if num < 40 or num > 60:
            print('Yes')
            break
    else:
        print('The all number is between 40-60.')


def up():
    lis_1 = [34, 35, 37, 39, 40, 42, 44, 45]
    lis_2 = [31, 32, 34, 33, 35, 35, 40, 41]
    x = 1
    x_2 = 1

    for index in range(1, len(lis_1)):
        if lis_1[index] <= lis_1[index - 1]:
            print('The rise is NOT continuous.')
            break
    else:
        print('The rise is  continuous.')

    for index2 in range(1, len(lis_2)):
        if lis_2[index2] <= lis_2[index2 - 1]:
            print('The rise is NOT continuous.')
            break
    else:
        print('The rise is continuous.')


def host():
    guests = []

    for guest in range(30):
        gue = random.randint(10, 30)
        guests.append(gue)

    if 30 in guests:
        print('We need expansion in this restaurant! ')
    else:
        print('The restaurant is OK!')

    for index in range(2, len(guests)):
        if guests[index] <= 12 and guests[index - 1] <= 12 and guests[index - 2] <= 12:
            print('We need some promotions.')
            break

    else:
        print("The promotion is OK!")


def exist():
    fruits = ['apple', 'kiwi', 'pineapple', 'pear', 'grape', 'orange', 'lemon', 'lime']

    fru = input('Wich fruit are you looking for? ')

    # for _ in fruits:
    #     if fru in fruits:
    #         print(fru, 'is in the list. ')
    #         break

    # else:
    #     print(fru, 'is NOT in the list. ')


    for i in range(len(fruits)):
        if fruits[i] == fru:
            print(fru, 'is the number', i+1, 'place in the list. ')
            break

    else:
        print(fru, 'is NOT in the list. ')


def num():
    num_list = [1, 54, 35, 67, 12]

    for i in num_list:
        if i % 2 == 0:
            print(i, 'is the first even number in the list. ')
            break

    for l in range(len(num_list)):
        if l % 7 == 0:
            print('is the number', l + 1, 'place in the list.')
            break

    for j in range(len(num_list)):
        if num_list[j] == 12:
            print('12 is number', j + 1, 'place in the list and this has', j, 'index.')
            break


def lnko():

    a = 68
    b = 54
    b_numbers = []
    a_numbers = []

    for x in range(53):
        if b % (x+1) == 0 and x != 0:
            b_numbers.append(x)
    
    for y in range(67):
        if a % (y + 1) == 0 and y != 0:
            a_numbers.append(y)
    
    # print(a_numbers, b_numbers)

    a_num = set(a_numbers)
    b_num = set(b_numbers)

    print(list(a_num.intersection(b_num))[-1])

def lnko_2():
    a = 68
    b = 54
    
    for i in range(54, 0, -1):
        if a % i == 0 and b % i == 0:
            print('thisd', i)
            break

def lkkt():
    a = 14
    b = 18

    for i in range(a*b+1):
        if (i+1) % a == 0 and (i+1) % b == 0:
            print(i+1)
            break

def montain():
    montain_ = [450, 782, 1344, 1783, 1889, 2520, 2343, 1381, 1213]
    print(montain_.index(max(montain_))+1)
    

def n_eight():
    for x in range(100000, 200000):
        if (x+1) % 80 == 0:
            print(x+1)
            break

    for num in range(100000, 2000000):
        if str(num)[4] == '8':
            print(num)
            break

def fruits():
    fruits = ["apple", "pear", "orange", "pineapple", "grape", "kiwi"]
    fruit = input('Wich fruit are you looking for? ')

    for i in range(len(fruits)):
        if fruit == fruits[i]:
            print('Find it!', fruits.index(fruit), "is its index")
            break
    else:
        print("Not find!")


def num1():
    numbers = [5, 3, 3, 4, 5, 6, 4, 5, 3, 1]

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            print("Ezen a helyen van ismétlés:", numbers.index(numbers[i]))
            break
    else:
        print('Nothing')


def names():
    man_names = ['Sanyi', 'Manyi', 'Jani', 'Pali', 'Olga', 'Pali', 'Pista']
    
    for name in man_names:
        if man_names.count(name) > 1:
            print(name)
            break
    else:
        print("Nothing")


def nnum():
    num_list = [3, 6, 4, 9, 8, 11, 12, 20]

    for i in range(1, len(num_list)):
        if abs(num_list[i] - num_list[i-1]) == 1:
            print("Yes", num_list[i], num_list[i-1])    
        else:
            ("Nothing")


def abc(): 
    letters = ["a", "v", "b", "k", "a", "f", "o", "l", "m", "o", "a"]

    after_k = 0

    for letter in letters:
        if letter > 'k':
            print(letter)
            after_k += 1

    print(after_k)
    print(letters.count('a'))


def throw_2():
    throw = []

    for _ in range(100000):
        throw.append(random.randint(1,6))
    
    print(throw.count(6))


def bigger_than_10():
    lis = [3, 6, 12, 3, 14, 5, 18]
    list2 = []

    for lis_2 in lis:
        if 10 < lis_2:
            list2.append(lis_2)

    print(len(list2))


def between():
    lis = []
    less_30 = []
    greater_60 = []

    for num in range(1, 101):
        lis.append(num)

    for i in lis:
        if i < 30:
            less_30.append(i)
        elif i > 60:
            greater_60.append(i)

    print("There are fewer than 30: ", len(less_30), "There are greater than 60: ", len(greater_60))


def red():
    lis = ["piros", "zöld", "kék", "kék", "piros", "zöld", "sárga", "kék", "piros"]

    print("Wnnyi piros van: ", lis.count("piros"), "Ennyi kék van: ", lis.count("kék"))


def throw_2():
    lis = []

    for _ in range(100000):
        num = random.randint(1,6)
        lis.append(num)

    print(lis.count(1))


def even():
    numbers = []
    even_nums = []

    for _ in range(100):
        num = random.randint(0,100)
        numbers.append(num)

    print(numbers)

    for i in range(len(numbers) - 1):
        if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0:
            even_nums.append(numbers[i])
    
    print(even_nums)
    print(len(even_nums))
    

def fe():
    lis = ["fele", "fölfele", "ferde", "felette", "zabkeksz", "fefefe", "fajsnde"]
    fe = 0

    for i in range(len(lis)):
        if lis[i][0] == 'f' and lis[i][-1] == 'e':
            fe += 1
        
    print(fe)


def max_min():
    numbers = [1, 4, 7, 13, 3, 5, 18, 12, 9, 11, 5, 17, 25, 38, 47]
    names = ["Barbara", "Franciszek", "Barbara", "Mikolaj", "Ambrozy", "Marek", "Daniel", "Lucyna", "Grzegorz", "Jozef", \
        "Antoni", "Franciszek", "Gabriela", "Natan", "Tomasz", "Izydor", "Adam", "Ewa", "Jan", "Melchior", "Baltazar", "Janusz", "Melchior", "Sylwester"]
    maximum = 0

    for num in numbers:
        if num > maximum and num % 2 == 0:  # ez akkor kell, ha bonyolultabb a maximum kiválasztása
            maximum = num
    print(maximum)

    print(max(numbers)) # ez mindig kiadja a legnagyobb értéket

    print(max(names))
    print(min(names))

def names_():
    names = ["Barbara", "Franciszek", "Barbara", "Mikolaj", "Ambrozy", "Marek", "Daniel", "Lucyna", "Grzegorz", "Jozef", \
        "Antoni", "Franciszek", "Gabriela", "Natan", "Tomasz", "Izydor", "Adam", "Ewa", "Jan", "Melchior", "Baltazar", "Janusz", "Melchior", "Sylwester"]
    maximum = 0
    max_name = []

    for name in names:
        if len(name) > maximum:
            maximum = len(name)
    
    for name in names:
        if len(name) == maximum:
            max_name.append(name)
        
    print(max_name)

    
def num_max():
    num_lis = [-2, 8, 7, -12, -22, 19, -5, 4]
    min_pos_lis = []

    # print(min(num_lis))

    # for i in num_lis:
    #     if i > 0:
    #         min_pos_lis.append(i)
    # print(min(min_pos_lis))
  
    # maximum = min(num_lis)

    # for number in num_lis:
    #     if abs(number) > abs(maximum):
    #         maximum = number
    # print(maximum)

    mini = (num_lis[0] + num_lis[1])
    pair_lis = []
    

    for i in range(1, len(num_lis)):
        
        if (num_lis[i] + num_lis[i-1]) > mini:
            mini = (num_lis[i] + num_lis[i-1])
            pair_lis.append(num_lis[i-1])
            pair_lis.append(num_lis[i])

    print(pair_lis)
    
def cube():

    def most_common(List):
        return(mode(List))

    List = []
    for _ in range (10000):
        num = random.randint(1,6)
        List.append(num)

    if List.count(1) > List.count(2) and List.count(1) > List.count(3) and List.count(1) > List.count(4) and List.count(1) > List.count(5) and List.count(1) > List.count(6):
        print("The most rolled number: 1 ")
    elif List.count(2) > List.count(1) and List.count(2) > List.count(3) and List.count(2) > List.count(4) and List.count(2) > List.count(5) and List.count(2) > List.count(6):
        print("The most rolled number: 2 ")
    elif List.count(3) > List.count(1) and List.count(3) > List.count(2) and List.count(3) > List.count(4) and List.count(3) > List.count(5) and List.count(3) > List.count(6):
        print("The most rolled number: 3 ")
    elif List.count(4) > List.count(1) and List.count(4) > List.count(3) and List.count(4) > List.count(2) and List.count(4) > List.count(5) and List.count(4) > List.count(6):
        print("The most rolled number: 4 ")
    elif List.count(5) > List.count(1) and List.count(5) > List.count(3) and List.count(5) > List.count(4) and List.count(5) > List.count(2) and List.count(5) > List.count(6):
        print("The most rolled number: 5 ")
    else:
        print("The most rolled number: 6 ")

    print(most_common(List))


def function():
    def keret(abc):                         
        print("#" * (len(abc) + 4))
        print("#", abc, "#")
        print("#" * (len(abc) + 4))

    def keret_2(abc, nice):
        first = nice * (len(abc) + 4)
        second = nice + " " +  abc + " " + nice
        result = first + "\n" + second + "\n" + first
        return result

    print(keret_2("Hey!", "#"))
    print(keret_2("Dear!", "+"))
    print(keret_2("Welcome!", ">"))
    print(keret_2("Good bye!", "*"))

    def square(num):
        result = num ** 2 + 2
        return result
    
    print(square(2))

    for number in range(10):
        print(square(number))


def fug():
    def num(number):                    # isinstance(abc, str) --> megnézi, h string-e a megadott érték
        return number + 1

    for i in range(1, 200):
        print(i, num(i))

    print(num(num(7)))

    def sum1(*abc):                    # akármennyi argumentet adhatunk így meg a függvények
        return sum(abc)

    print(sum1(10,20,30,40,50,60,70,80,90,100))

def sequence():
    def average(num_list):
        return (sum(num_list)) / len(num_list)

    num_list = [1, 5, 4, 3, 7, 8, 8, 9, 5, 4, 5]
    print(average(num_list))


def head():
    def heads_or_tails(string):
        if coin == 1:
            return "head"
        else:
            return "tail"

    for i in range(10):
        coin = random.randint(1,2)
        print(coin)
        print(heads_or_tails(string))

    
def even_odd():
    def even(number):
        if num % 2 == 0:
            return True
        else:
            return False
    
    for _ in range(10):
        num = random.randint(0,100)
        print(num)
        print(even(num))

def text_file():
    lis = ["First line. \n", "Second line. \n", "Third line. \n", "4444444 \n"]
    print(lis)
    lis_2 = []

    for line in lis:
        new_line = line.strip()
        lis_2.append(new_line)

    print(lis_2)


def text():
    
    # my_absolute_path = r'D:\python\text.txt'

    # with open(my_absolute_path, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()

    #     print(lines)


    # file = open("text.txt")
    # for i in file:
    #     print(i.strip(), ' ', end= '')

    # file.close()


    # files = open('text.txt')
    # lis = []

    # for line in files:
    #     lis.append(line.strip())
    # files.close()

    # file_2 = open('outtext.txt', 'w')
    # for word in line:
    #     print(word, end='', file = file_2)

    # print('', file = file_2)
    # file_2.close()

    
    # lis = []
    # egy = open('text.txt')

    # for line in egy:
    #     lis.append(line.strip())
    # egy.close()

    # lepke = open('outtext.txt', 'w')
    # print(' '.join(lis), file = lepke)
    # lepke.close()


    x = open('text.txt')
    new = []

    for line in x:
        new.append(line.strip())
    x.close()

    y = open('new_text.txt', 'w')
    for word in new:
        print(word, file = y)
    y.close()


def dim():
    lis = []

    x = open('dim.txt')

    for line in x:
        strip_line = line.strip()
        line_list = strip_line.split()
        print(line_list)
        lis.append(line_list)

    x.close()
    print(lis)

    lis_2 = []

    y = open('dim2.txt')

    while True:
        line_lis = []
        line = y.readline()
        if line:
            line_lis.append(line.strip())   # beírjuk a nevet a line_lis-be
            line = y.readline()
            if line:
                line_lis += line.strip().split()    # beírjuk a 2. sort a line_lis-be (jatékos pozícióját, eredményeit)
            else:
                break
        else:
            break
        print(line_lis)
        lis_2.append(line_lis)

    y.close()
    print(lis_2)

def football():
    lis = []
    x = open('dim.txt')

    for line in x:
        print(line.strip().split()[0], ', ', sep='', end='')
    print('')

    # for line in x:
    #     strip_line = line.strip()
    #     line_list = strip_line.split()
    #     lis.append(line_list)
    # x.close()

    # for name in lis:
    #     print(name[0], ', ', sep='', end='')


    # names = []
    # for name in lis:
    #     names.append(name[0])

    # print(', '.join(names))


def csatar():
    x = open('dim.txt')
    lis = []
    csat = 0

    for line in x:
        strip_line = line.strip().split()
        lis.append(strip_line)
    x.close()

    for pozi in lis:
        if pozi[1] == 'csatar':
            csat += 1

    print(lis)
    print(csat)

   
def pozi():
    def position(lista, pozi):
        # pozi = input('Give me a position: ')
        num = 0

        for word in lis:
            if word[1] == pozi:
                num += 1
        return num    

    lis = []
    doc = open('dim.txt')

    for line in doc:
        lis.append(line.strip().split())

    doc.close()
    print(lis)
    print('This is the number of csatar:', position(lis, 'csatar'))
    print('This is the number of hatved:', position(lis, 'hatved'))
    print('This is the number of kozeppalyas:', position(lis, 'kozeppalyas'))

    for pozi in ['csatar', 'hatved', 'kozeppalyas']:
        print('This is the number of', pozi, ':', position(lis, pozi))


def average():
    file = open('dim.txt')
    lis = []

    for line in file:
        lis.append(line.strip())

    print(lis)
    file.close()

    goals = []
    for num in lis:
        print(num[-2:])
        goals.append(int(num[-2:]))

    print(sum(goals)/len(goals))

def average_2():
    file = open('dim.txt')
    lis = []

    for line in file:
        lis.append(line.strip().split())

    print(lis)
    file.close()

    goals = 0
    for num in lis:
        goals += int(num[-1])

    print(goals/len(lis))
        

def least():
    file = open('dim.txt')
    lis = []

    for line in file:
        lis.append(line.strip().split())
       
    print(lis)
    file.close()

    leas = 100
    for man in lis:
        if int(man[3]) < leas:
            leas = int(man[3])

    for who in lis:
        if int(who[3]) == leas:
            print(who[0], who[1])


def over_10():
    file = open('dim.txt')
    lis = []

    for line in file:
        lis.append(line.strip().split())

    file.close()
    goal = 0

    for num in lis:
        if int(num[3]) > 10:
            goal = int(num[3])

    for who in lis:
        if int(who[3]) == goal:
            print(who[0], who[1])


def average_posi():
    file = open('dim.txt')
    lis = []

    for line in file:
        lis.append(line.strip().split())

    file.close()
    positions = []

    for pozi in lis:
        positions.append(pozi[1])

    x= set(positions)
    pos = list(x)

    names = []
    names_2 = []
    names_3 = []
    for name in lis:
        if str(name[1]) == pos[0]:
            names.append(name)
            # print(names)
        elif str(name[1]) == pos[1]:
            names_2.append(name)
            # print(names_2)           
        elif str(name[1]) == pos[2]:
            names_3.append(name)
            # print(names_3)
    
    print(names, names_2, names_3)


    goals = 0
    goals_2 = 0
    goals_3 = 0
    for goal in names:
         goals += int(goal[-1])

    for goa in names_2:
         goals_2 += int(goa[-1])

    for go in names_3:
         goals_3 += int(go[-1])


    print('This is the average of hatved:', goals/len(names), 'This is the average of kozeppalyas:', round(goals_2/len(names_2), 2), 'This is the average of csatar:', round(goals_3/len(names_3), 2),)

def list_football():
    file = open('football.txt')
    football = []

    for line in file:
        football.append(line.strip().split())

    file.close()
    
    for lin in football:
        for li in lin:
            print(li, '', end='')
        print('')

    file_2 = open('football.txt')

    for lis in file_2:
        print(lis, end='')

    file_2.close()

def copy():
    def plus_5(num):
        return num + 5

    def firstname(name):
        return name.split()[0]

    nums = [1, -2, -3, 4, -5, 6, 7]
    names = ['John Smith', 'Katie Burrock', 'Liana Potter']
    other = []
    names_other = []

    for num in nums:
        other.append(plus_5(num))

    for name in names:
        names_other.append(firstname(name))
    
    five_more = list(map(plus_5, nums))
    first_names = list(map(firstname, names))

    print(nums)
    print(five_more)
    print(names)
    print(first_names)
    # print(other)
    # print(firstname('John Smith'))
    # print(names_other)


def temperature():
    temps = []
    temps_copy = []

    def hot(temp):
        if temp > 20:
            return '!'
        else:
            return temp
    
    for _ in range(30):
        temps.append(random.randint(15, 25))

    for temp in temps:
        temps_copy.append(hot(temp))

    print(temps)
    # print(temps_copy)

    temps_copy_2 = []

    for i in range(len (temps)):
        if temps[i] == 0:
            temps_copy_2.append(0)
        elif temps[i] > temps[i-1]:
            temps_copy_2.append('+')
        elif temps[i] == temps[i-1]:
            temps_copy_2.append('=')
        else:
            temps_copy_2.append('-')

    print(temps_copy_2)


def assesment():
    lis = [['literature', 3.2], ['math', 3.8], ['english', 4.6], ['computer science', 1.4]]
    lis_2 = []

    def result(lis):
        if lis >= 4.5:
            return 'A'
        elif lis >= 3.5:
            return 'B'
        elif lis >= 2.5:
            return 'C'
        elif lis >= 1.5:
            return 'D'
        else:
            return 'E'

    for i in lis:
        line = []
        line.append(i[0])
        line.append(result(i[1]))
        lis_2.append(line)

    for lines in lis_2:
        print(': '.join(lines))

def char():
    words = 'expressions'
    lis = ['apple', 'pear', 'banana']

    def plus_v(word):
        vowel = ['a', 'e', 'i', 'o', 'u']

        word_v = ''
        for char in word:
            if char in vowel:
                word_v += char + 'v' + char
            else:
                word_v += char
        return word_v
    
    print(plus_v(words))
    

def certi():
    file = open('school.txt')

    def assessment(num):
        if num >= 4.5:
            return 'A'
        elif num >= 3.5:
            return 'B'
        elif num >= 2.5:
            return 'C'
        elif num >= 1.5:
            return 'D'
        else: 
            return 'E'

    def from_diary(str):
        certi = []
        for registry in str:
            line = []
            line.append(registry[0])
            line.append(assessment(registry[1]))
            certi.append(line)
        return certi

    def out(abc):
        for lin in abc:
            print(': '.join(lin))

    def average(num_lis):
        return sum(num_lis)/len(num_lis)

    def part_of_file(line):
            part = []
            lis = line.split(': ')
            part.append(lis[0])
            nums = lis[1].strip().split(', ')
            nums_from_string = list(map(int, nums))
            part.append(average(nums_from_string))
            return part
    diary = []

    for lines in file:
            lines = lines.strip()
            diary.append(part_of_file(lines))

    assessment = from_diary(diary)
    out(assessment)
    file.close()
            

def example():
    file = open('school.txt')
    lis = []

    def result(a):
        if a >= 4.5:
            return 'A'
        elif a >= 3.5:
            return 'B'
        elif a >= 2.5:
            return 'C'
        elif a >= 1.5:
            return 'D'
        else:
            return 'E'

    def average(b_list):
        return sum(b_list)/len(b_list)

    def certification(c_line):
        certi = []
        for i in c_line:
            line = []
            line.append(i[0])
            line.append(result(i[1]))
            certi.append(line)
        return certi

    def out(d):
        for i in d:
            print(': '.join(i))

    def part_of_file(e):
        part = []
        line = e.split(': ')
        part.append(line[0])
        nums = line[1].strip().split(', ')
        int_num = list(map(int, nums))
        part.append(average(int_num))
        return part
    diary = []

    for i in file:
        i = i.strip()
        diary.append(part_of_file(i))

    result = certification(diary)
    out(result)
    file.close()


def selection():
    def even(num):
        if num % 2 == 0:
            return True
        else:
            return False

    lis = [1, 103, 56, 49, 37, 18]

    even_nums = []

    for num in lis:
        if even(num):
            even_nums.append(num)

    print(lis)
    print(even_nums)


def a_1949():
    file = open('1949.txt')
    line_list = []

    for line in file:
        line = line.strip().split()
        line_list.append(line)

    file.close()
    def date_month(date):
        month = date.split()[0]
        if month == 'mĂˇrcius' or month == 'Ăˇprilis':
            return 'spring'
        else:
            return 'other'
    
    study_list = []

    for study in line_list:
        if study[0] == '1849.' and date_month(study[1]) == 'spring':
            study_list.append(study)

    for line in study_list:
        print(line[0], ' ', line[1], ': ', line[2], sep = '')


def sort():
    nums = [1, 100, 300, 156, 21, 212, 45, 34, 78, 107]
    over_100 = []
    under_100 = []

    for num in nums:
        if num > 100:
            over_100.append(num)
        elif num < 100:
            under_100.append(num)

    print(nums)
    print(over_100)
    print(under_100)
    # print(under_100)


def sort_sorted_list():
    lis = [5, 3, 9, 1, 7]

    print(lis)
    lis.sort()          # megváltoztatja a lista sorrendjét
    print(lis)          
    print(sorted(lis, reverse = True))      # helyben rendez

def sort_list():
    lis = [5, -3, 9, -1, 7]

    print(lis)
    print(sorted(lis, key = abs, reverse = True))       # kulcsfüggvény használata 

def sort_names():
    lis = ['Dorogi Zsiga', 'Batyu Ferenc', 'Aba Samu', 'Czipo Lajos']

    def lastnames(name):
        return name.split()[1][0]

    print(lis)
    print(sorted(lis, reverse = True))
    print(sorted(lis, key = lastnames))


def nums_100():
    num_lis = []
    for _ in range(100):
        num = random.randint(1,1000)
        num_lis.append(num)

    num_lis.sort()
    print(num_lis)


def sets():
    lis = ['apple', 'banana', 'pear', 'pear']
    new_set = set(lis)                          # halmaznál a bejárás sorrendje nem fix, mindig változik

    set_1 = set()       # üres halmaz
    lis_1 = list()      # üres lista

    for i in new_set:
        print(i)
    
    set_2 = set()

    for i in lis:
        set_2.add(i)
        print(i, set_2)

    set_2.remove('pear')
    print(set_2)
    
    lis_2 = sorted(list(set(lis)))          # listából halmaz, majd abból újra lista rendezve
    print(lis_2)

    set1 = {1, 2, 3, 4, 4, 5, 4}
    set2 = {5, 5, 6, 7, 10, 10, 8, 9}

    sets = set1 & set2          # metszet
    unio = set1 | set2          # unió
    diff = set1 - set2          # különbség
    sim_diff = set1 ^ set2      # szimmetrikus differenciál, minden benne lesz csak a KÖZÖS ELEM NEM

    print(set1, set2, sets, unio, diff, sim_diff)

def union():
    juli = ['apple', 'tomato', 'onion']
    kati = ['apple', 'pear', 'salad']
    isti = ['tomato', 'paprika', 'onion', 'potato']

    sel = set(juli) | set(kati) | set(isti)
    print(sel)

def for_loop():
    lis = ['Rocket', '424', 'Thomas', 'Flying Scotsman']

    for sz, element in enumerate(lis):
        print(sz + 1, ': ', element, sep = '')
        # print(element)

def lists():
    lis = [5, 3, 7, 12, 4]
    lis_2 = [item * 2 for item in lis]
    lis_3 = [item * 3 for item in lis if item >= 4]
    string_lis = ['apple', 'pear', 'onion', 'salad', 'tomato']
    string_lis_2 = [item.upper() for item in string_lis if 'a' in item]

    print(lis, lis_2, lis_3)
    print(string_lis, string_lis_2)

    lis_ = [[1,2], [3,4], [4,5,6]]

    sum_lis = [item for inner_lis in lis_ for item in inner_lis]
    set_for = {item for inner_lis in lis_ for item in inner_lis}

    print(sum(sum_lis))
    print(sum(set_for))


def dic():
    human = {'name': 'Glan', 'birth year': 1999, 'location': 'Newyork', 'profession': 'farmer', 'number of eyes': 2}        # szótár: kulcs és egy hozzá tatozó érték
    human['dog'] = 'Foxy'   # szótárnak nincs sorrendje, nincs vhanyadik eleme
    del human['dog']        # törlés
    
    print(human)

    for data in human:      # a kulcsot adja vissza 
        print(data)

    for data in human.keys():       # a kulcsokat adja vissza, így látványos
        print(data)
    
    for data in human.values():     # az értékeket adja vissza
        print(data)

    for key, result, in human.items():      # mindent kiír, a kulcsot is és az értéket is
        print(key, ': ', result)

    print(human.get('name'))
    print(human.get('cat', "He doesn't have cat"))      # megnézi, h van-e a szótárban, ha nincs, akkor kiírja, hogy None,vagy a megadott szöveget 
    print(human.pop('name'))            # visszaadja az értéket, és kitörli a szótárból


def animals():
    animals = []

    while True:
        animal = {}
        name = input("What is the animal's name? ")
        if not name:
            break
        animal['name'] = name
        animal['type'] = input("What is tha animal's type? ")
        animal['age'] = 2023 - int(input("What is the animal's age? "))
        animals.append(animal)
        print(animals)

    file_ = open('animals.txt', 'w')
    for animal in animals:
        for property in ['name', 'age', 'type']:
            print(animal[property], end='', file = file_ )
            if property != 'type':
                print(';', end='', file = file_ )
        print('', file = file_ )

    file_.close()

def numer():
    humans = [{'name': 'Harry', 'score': 37.21}, {'name': 'Berry', 'score': 37.21}, \
         {'name': 'Tina', 'score': 37.2}, {'name': 'Akriti', 'score': 41.0}, {'name': 'Harsh', 'score': 39.0}]

    for i in range(1, len(humans)):
        if humans[i-1]['score'] < humans[i]['score']:
            num = humans[i-1]['score']
            
        print(humans[i-1]['score'])
        print(num)

def test():
    def secret_chamber(translations, test_cases):
        mapping = {}
        for t in translations:
            if t[0] in mapping:
                mapping[t[0]].append(t[1])
            else:
                mapping[t[0]] = [t[1]]

        for i in range(len(mapping)):
            for letter in mapping:
                for mapped_letter in mapping[letter]:
                    if mapped_letter in mapping:
                        mapping[letter] += mapping[mapped_letter]

        for test_case in test_cases:
            source, target = test_case
            if source == target:
                print("yes")
            else:
                mapping_exists = True
                for i in range(len(target)):
                    if target[i] not in mapping.get(source[i], []):
                        mapping_exists = False
                        break
                if mapping_exists:
                    print("yes")
                else:
                    print("no")

    translations = []
    test_cases = []

    n, m = map(int, input().split())
    for i in range(n):
        a, b = input().split()
        translations.append((a, b))
    for i in range(m):
        a, b = input().split()
        test_cases.append((a, b))

    secret_chamber(translations, test_cases)

def class1():
    class Human:
        name = ''
        age = None
        sex = ''

        def set_age(self, value):
            self.age = value

        def set_name(self, value):
            self.name = value

        def set_sex(self, value):
            self.sex = value

    John = Human()
    John.set_age(21)
    John.set_name('John')
    John.set_sex('man')

    print(John.name)
    print(John.age)
    print(John.sex)

    Mary = Human()
    Mary.set_name('Mary')
    Mary.set_age(48)
    Mary.set_sex('woman')
 
    print(Mary.name)
    print(Mary.age)
    print(Mary.sex)


def init():
    class Human:
        def __init__(self, name, age, sex, nationality, religion = 'hindi'):
            self.name = name
            self.age = age
            self.sex = sex
            self.nationality = nationality
            self.religion = religion
            self.hello()

        def hello(self):
            print('Hello ' + self.name)

    Katy = Human('Katy', 32, 'woman', 'american', 'catholic')
    Harry = Human('Harry', 47, 'man', 'english')
    print(Katy.name, Katy.age, Katy.sex, Katy.nationality, Katy.religion)
    print(Harry.name, Harry.age, Harry.sex, Harry.religion)

    print(type(Katy))

    class Employe(Human):
        def __init__(self, name, age, sex, nationality, religion, experienses, trustfullness, education):
            super().__init__(name, age, sex, nationality, religion)
            self.experienses = experienses
            self.trustfullness = trustfullness
            self.education = education


    Any = Employe('Any', 45, 'woman', 'spanish', 'catholic', 8, 8, 'trainer' )
    Kelly = Employe('Kelly', 36, 'woman', 'american', 'catholic', 7, 7.5, 'shoper')

    print(Any.name)
    print(Any.education)
    Kelly.education = 'doctor'
    print(Kelly.name)
    print(Kelly.education)
    print(Kelly.religion)


def strin_format():
    text = 'Your name {} and you are {} years old.'.format('Mary', 35)      # régi módszer
    print(text)

    name = 'Kelly'
    age = 45
    text_2 = f'Your name {name} and you are {age} years old.'       # új módszer 
    print(text_2)

    names_dict = {'Betty': 28, "Candy": 45, "Tony": 41, "Peter": 27, "Cho": 67}

    for name, age in names_dict.items():
        print(f'Your name {name} and you are {age + 5} years old.')


def operators():
    # += -= *= /= //= %= **= 
    num = 10
    print(num)
    num += 5
    print(num)
    num -= 5
    print(num)
    num *= 2
    print(num)
    num /= 2
    print(num)
    num //= 3
    print(num)
    num %= 5
    print(num)
    num **= 2
    print(num)
    # < > <= >= != ==    True vagy False értéket ad vissza mindig
    num1 = 10
    num2 = 4
    print(num1 < num2)      # False értéket kapuk, mert nem kisebb a 10 a 4-nél
    print(num1 > num2)
    print(5 <= 5)           # True
    print(7 >= 6)
    print(14 != 5)          # nem egyenlő
    print(45 == num1)         # egyenlő-e
    # and or not        True and True = True, True and False = False, False and False = False       True or True = True, True or False = True, False or False = False       True and not False = True
    num3 = 2
    num4 = 4
    print(num3 < num4 and num3 == 2)            # True
    print(num3 < num4 and num3 == 3)            # False
    print(num3 < num4 or num3 == 3 or 5 > 6)    # True
    print(num3 < num4 and not num3 == 3)        # True


def keywords():
    for i in range(10):
        if i == 5:
            break           # megszakítja a ciklust, kiugrik belőle azon a ponton, ahol a break szó van
        print(i)     

    num = 0
    while True:
        if num == 5:
            break
        num += 1
        print(num)
        
    # while True:
    #     pass            # ha nem tudom, hogy mit szeretnék a törzsbe írni, akk írom a pass-t és akk le tud furni a program, nem ad hibát, de nem csinál semmit a ciklus

    for i in range(10):
        if i == 5:
            continue
        print('a', i)

    while True:
        num += 1
        if num % 2 == 0:
            continue
        print(num)
        if num > 20:
            break


def password2():
    password = "CBA321"
    user_input = input("Enter your password: ")
    test = 0

    while user_input != password:
        test += 1
        if test == 3:
            print("System error.")
            break
        print("Wrong password!")
        user_input = input("Enter your password: ")

    if user_input == password:
        print("Correct password. Welcome!")

def main():
    fug()


# magic method: __name__
if __name__ == "__main__":
    main()


