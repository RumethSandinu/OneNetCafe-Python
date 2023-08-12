from simple_colors import *         #install simple-colors
import time
import random
from prettytable import PrettyTable         #install prettytable
print( green('W' , ['bold']) , end = '')            #This will print 'Welcome To One Net Cafe Application' like an animation.
time.sleep(0.1)
print( green('e' , ['bold']) , end = '')
time.sleep(0.1)
print( green('l' , ['bold']) , end = '')
time.sleep(0.1)
print( green('c' , ['bold']) , end = '')
time.sleep(0.1)
print( green('o' , ['bold']) , end = '')
time.sleep(0.1)
print( green('m' , ['bold']) , end = '')
time.sleep(0.1)
print( green('e' , ['bold']) , end = ' ')
time.sleep(0.1)
print( green('T' , ['bold']) , end = '')
time.sleep(0.1)
print( green('o' , ['bold']) , end = ' ')
time.sleep(0.1)
print( green('O' , ['bold']) , end = '')
time.sleep(0.1)
print( green('n' , ['bold']) , end = '')
time.sleep(0.1)
print( green('e' , ['bold']) , end = ' ')
time.sleep(0.1)
print( green('N' , ['bold']) , end = '')
time.sleep(0.1)
print( green('e' , ['bold']) , end = '')
time.sleep(0.1)
print( green('t' , ['bold']) , end = ' ')
time.sleep(0.1)
print( green('C' , ['bold']) , end = '')
time.sleep(0.1)
print( green('a' , ['bold']) , end = '')
time.sleep(0.1)
print( green('f' , ['bold']) , end = '')
time.sleep(0.1)
print( green('e' , ['bold']) , end = ' ')
time.sleep(0.1)
print( green('A' , ['bold']) , end = '')
time.sleep(0.1)
print( green('p' , ['bold']) , end = '')
time.sleep(0.1)
print( green('p' , ['bold']) , end = '')
time.sleep(0.1)
print( green('l' , ['bold']) , end = '')
time.sleep(0.1)
print( green('i' , ['bold']) , end = '')
time.sleep(0.1)
print( green('c' , ['bold']) , end = '')
time.sleep(0.1)
print( green('a' , ['bold']) , end = '')
time.sleep(0.1)
print( green('t' , ['bold']) , end = '')
time.sleep(0.1)
print( green('i' , ['bold']) , end = '')
time.sleep(0.1)
print( green('o' , ['bold']) , end = '')
time.sleep(0.1)
print( green('n' , ['bold']))
time.sleep(0.4)
print('\nConsole menu:')
print('    Type' , red('AID') , 'for adding item details.\n'
      '    Type' , red('DID') , 'for deleting item details.\n'
      '    Type' , red('UID') , 'for updating item details.\n'
      '    Type' , red('VID') , 'for viewing the items table.\n'
      '    Type' , red('SID') , 'for saving the item details to the text file anytime.\n'
      '    Type' , red('SDD') , 'for selecting four dealers randomly from a file.\n'
      '    Type' , red('VRL') , 'for displaying all the details of the randomly selected dealer.\n'
      '    Type' , red('LDI') , 'for display the items of the given dealer.\n'
      '    Type' , red('ESC') , 'to exit the program.')
print(blue('[I]') , 'Type console keyword:', end =' ' )
console = input()
while console.upper() != 'ESC' :
    while console.upper() == 'AID' :
        print(blue('[I]') , 'Enter Item Code' , end = ' ')
        ItemCode = input()
        tryvalue = False
        while tryvalue == False :
            try :
                int(ItemCode)
            except :
                print(red('[E] Item Code must be integer value'))
                print(blue('[I]'), 'Enter Item Code:', end = ' ')
                ItemCode = input()
                continue
            try :
                f = open('OneNetCafe.txt', 'r')
                lines = f.read().splitlines()
                OutList = []
                for value in lines :
                    OutList = eval(value.strip())
                    if int(ItemCode) == OutList[0] :
                        print(red('[E] ItemCode exists'))
                        print(blue('[I]') , 'Enter Item Code' , end = ' ')
                        ItemCode = input()
                        tryvalue = False
                        break
                    else :
                        tryvalue = True
            except :
                break
        def item_code() :
            return int(ItemCode)
        print(blue('[I]') , 'Enter Item Name' , end = ' ')
        ItemName = input()
        tryvalue = False
        while True :
            try :
                int(ItemName)
                print(red('[E] Item Name must be string value'))
                print(blue('[I]'), 'Enter Item Name', end=' ')
                ItemName = input()
            except :
                break
        def item_name() :
            return ItemName
        print(blue('[I]') , 'Enter Item Brand' , end = ' ')
        ItemBrand = input()
        tryvalue = False
        while True :
            try:
                int(ItemBrand)
                print(red('[E] Item Brand must be string value'))
                print(blue('[I]'), 'Enter Item Brand', end =' ')
                ItemBrand = input()
            except:
                break
        def item_brand() :
            return ItemBrand
        print(blue('[I]') , 'Enter Item Price:' , end = ' ')
        ItemPrice = input()
        while True:
            try:
                float(ItemPrice)
            except:
                print(red('[E] Item Price must be float value'))
                print(blue('[I]') , 'Enter Item Price:' , end = ' ')
                ItemPrice = input()
                continue
            decimal = float(ItemPrice)
            value = int(decimal)
            if ((decimal - value) >= 0.6) or (decimal < 0):
                print(red('[E] Item Price not in range'))
                print(blue('[I]') , 'Enter The Correct Item Price:' , end = ' ')
                ItemPrice = input()
                continue
            else:
                break
        def item_price() :
            return float(ItemPrice)
        print(blue('[I]') , 'Enter Item Quantity:' , end = ' ')
        ItemQuantity = input()
        while True :
            try :
                int(ItemQuantity)
            except :
                print(red('[E] Item Quantity must be integer value'))
                print(blue('[I]') , 'Enter Item Quantity:' , end = ' ')
                ItemQuantity = input()
                continue
            if int(ItemQuantity) < 0 :
                print(red('[E] Item Quantity not in range'))
                print(blue('[I]'), 'Enter Item Quantity:', end=' ')
                ItemQuantity = input()
                continue
            else :
                break
        def item_quantity() :
            return int(ItemQuantity)
        print(blue('[I]') , 'Enter Item Category:' , end = ' ')
        ItemCategory = input()
        while True :
            try :
                int(ItemCategory)
                print(red('[E] Item Category must be string value'))
                print(blue('[I]') , 'Enter Item Category:' , end = ' ')
                ItemCategory = input()
            except :
                break
        def item_category() :
            return ItemCategory
        print(blue('[I]') , 'Enter Purchase Year of the Item:' , end = ' ')
        YearOfPurchase = input()
        while True :
            try :
                int(YearOfPurchase)
            except :
                print(red('[E] Purchase Year must be integer'))
                print(blue('[I]'), 'Enter Purchase Year of the Item:', end=' ')
                YearOfPurchase = input()
                continue
            if int(YearOfPurchase) < 2022 :
                print(red('[E] Purchase Year not in range'))
                print(blue('[I]'), 'Enter Purchase Year of the Item:', end=' ')
                YearOfPurchase = input()
                continue
            else :
                break
        def year_of_purchase() :
            return YearOfPurchase
        print(blue('[I]') , 'Enter Purchase Month of the Item:' , end = ' ')
        MonthOfPurchase = input()
        while True:
            try :
                int(MonthOfPurchase)
            except :
                print(red('[E] Purchase Month must be integer value'))
                print(blue('[I]'), 'Enter Purchase Month of the Item:', end=' ')
                MonthOfPurchase = input()
                continue
            if int(MonthOfPurchase) < 1 or int(MonthOfPurchase) > 12 :
                print(red('[E] Purchase Month not in range.'))
                print(blue('[I]'), 'Enter Purchase Month of the Item:', end=' ')
                MonthOfPurchase = input()
                continue
            else:
                break
        def month_of_purchase() :
            return MonthOfPurchase
        print(blue('[I]') , 'Enter Purchase Day of the Item:' , end = ' ')
        DayOfPurchase = input()
        while True :
            try :
                int(DayOfPurchase)
            except :
                print(red('[E] Purchase Day must be integer value'))
                print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                DayOfPurchase = input()
                continue
            if (int(MonthOfPurchase) == 1) or (int(MonthOfPurchase) == 3) or (int(MonthOfPurchase) == 5) or (int(MonthOfPurchase)) == 7 or (int(MonthOfPurchase)) == 8 or (int(MonthOfPurchase) == 10) or (int(MonthOfPurchase) == 12) :
                if (int(DayOfPurchase) < 1) or (int(DayOfPurchase) > 31):
                    print(red('[E] Purchase Day not in range.'))
                    print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                    DayOfPurchase = input()
                    continue
                else :
                    break
            elif (int(MonthOfPurchase) == 4) or (int(MonthOfPurchase) == 6) or (int(MonthOfPurchase) == 9) or (int(MonthOfPurchase) == 11) :
                if (int(DayOfPurchase)) < 1 or (int(DayOfPurchase) > 30) :
                    print(red('[E] Purchase Day not in range.'))
                    print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                    DayOfPurchase = input()
                    continue
                else:
                    break
            elif int(MonthOfPurchase) == 2:
                if int(YearOfPurchase) % 4 == 0:
                    if (int(DayOfPurchase)) < 1 or (int(DayOfPurchase) > 29) :
                        print(red('[E] Purchase Day not in range.'))
                        print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                        DayOfPurchase = input()
                        continue
                    else :
                        break
                else :
                    if (int(DayOfPurchase) < 1) or (int(DayOfPurchase) > 28) :
                        print(red('[E] Purchase Day not in range.'))
                        print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                        DayOfPurchase = input()
                        continue
                    else :
                        break
        def day_of_purchase() :
            return DayOfPurchase
        def item_purchase_date() :
            ItemPurchaseDate =  str(day_of_purchase()) + '/' + str(month_of_purchase()) + '/' + str(year_of_purchase())
            return ItemPurchaseDate
        ItemList = []
        ItemList.insert(0,item_code())
        ItemList.insert(1,item_name())
        ItemList.insert(2,item_brand())
        ItemList.insert(3,item_price())
        ItemList.insert(4,item_quantity())
        ItemList.insert(5,item_category())
        ItemList.insert(6,item_purchase_date())
        print(blue('[I]') , 'Type console keyword [' , red('SID') , 'to save]:' , end = ' ')
        console = input()
        if console.upper() == 'SID' :
            f = open('OneNetCafe.txt' , 'a')
            f.write(str(ItemList))
            f.write('\n')
            f.close()
            print(blue('[O]') , 'Item record has been succesfully saved.')
            print(blue('[I]') , 'Type console keyword:' , end = ' ')
            console = input()
        else:
            continue
    while console.upper() == 'DID' :
        f = open('OneNetCafe.txt' , 'r+')
        lines = f.read().splitlines()
        tryvalue = False
        print(blue('[I]') , 'Enter the Item Code you want to delete:' , end = ' ')
        SearchCode = input()
        OutList = []
        while tryvalue == False :
            try :
                int(SearchCode)
                tryvalue = True
            except :
                print(red('[E] Item Code must be integer value'))
                print(blue('[I]') , 'Enter the Item Code you want to delete:' , end = ' ')
                SearchCode = input()
                continue
            Check = False
            while Check == False:
                for value in lines :
                    CheckList = eval(value.strip())
                    if int(SearchCode) == CheckList[0] :
                        Check = True
                    else:
                        OutList.append(value)
                break
            if Check == False :
                print(red('[E] ItemCode does not exist'))
                print(blue('[I]') , 'Enter the Item Code you want to delete:' , end = ' ')
                SearchCode = input()
                tryvalue = False
            else :
                break
        f.close()
        print(blue('[I]') , 'Type console keyword [' , red('SID') , 'to confirm deletation]:' , end = ' ')
        console = input()
        while console.upper() == 'SID':
            f = open('OneNetCafe.txt', 'a')
            f.truncate(0)
            f.seek(0)
            for value in OutList :
                f.write(str(value))
                f.write('\n')
            f.close()
            print(blue('[O]') , 'Item record succesfully deleted.')
            print(blue('[I]') , 'Type console keyword:' , end = ' ')
            console = input()
        else :
            continue
    while console.upper() == 'UID' :
        print(blue('[I]') , 'Enter the Item Code you want Update:' , end = ' ')
        SearchCode = input()
        tryvalue = False
        while tryvalue == False:
            try :
                int(SearchCode)
                tryvalue = True
            except :
                print(red('[E] Item Code must be integer value'))
                print(blue('[I]') , 'Enter the Item Code you want Update:' , end = ' ')
                SearchCode = input()
                continue
            KeyList = []
            key = False
            Search = False
            f = open('OneNetCafe.txt', 'r')
            while key == False :
                lines = f.read().splitlines()
                for data in lines :
                    KeyList = eval(data.strip())
                    if int(SearchCode) == KeyList[0] :
                        key = True
                        Search = True
                        break
                    else:
                        Search = False
                break
            if Search == False :
                print(red('[E] ItemCode does not exist.'))
                print(blue('[I]') , 'Enter the Item Code you want Update:' , end = ' ')
                SearchCode = input()
                f.close()
                tryvalue = False
                continue
            else :
                break
        f = open('OneNetCafe.txt', 'r')
        OutList = []
        LastList = []
        lines = f.read().splitlines()
        for value in lines:
            OutList = eval(value.strip())
            if int(SearchCode) == OutList[0]:
                def item_code():
                    return int(SearchCode)
                print(blue('[I]'), 'Enter Item Name', end=' ')
                ItemName = input()
                tryvalue = False
                while True:
                    try:
                        int(ItemName)
                        print(red('[E] Item Name must be string value'))
                        print(blue('[I]'), 'Enter Item Name', end=' ')
                        ItemName = input()
                    except:
                        break
                def item_name():
                    return ItemName
                print(blue('[I]'), 'Enter Item Brand', end=' ')
                ItemBrand = input()
                tryvalue = False
                while True:
                    try:
                        int(ItemBrand)
                        print(red('[E] Item Brand must be string value'))
                        print(blue('[I]'), 'Enter Item Brand', end=' ')
                        ItemBrand = input()
                    except:
                        break
                def item_brand():
                    return ItemBrand
                print(blue('[I]'), 'Enter Item Price:', end=' ')
                ItemPrice = input()
                while True:
                    try:
                        float(ItemPrice)
                    except:
                        print(red('[E] Item Price must be float value'))
                        print(blue('[I]'), 'Enter Item Price:', end=' ')
                        ItemPrice = input()
                        continue
                    decimal = float(ItemPrice)
                    value = int(decimal)
                    if ((decimal - value) >= 0.6) or (decimal < 0):
                        print(red('[E] Item Price not in range'))
                        print(blue('[I]'), 'Enter The Correct Item Price:', end=' ')
                        ItemPrice = input()
                        continue
                    else:
                        break
                def item_price():
                    return float(ItemPrice)
                print(blue('[I]'), 'Enter Item Quantity:', end=' ')
                ItemQuantity = input()
                while True:
                    try:
                        int(ItemQuantity)
                    except:
                        print(red('[E] Item Quantity must be integer value'))
                        print(blue('[I]'), 'Enter Item Quantity:', end=' ')
                        ItemQuantity = input()
                        continue
                    if int(ItemQuantity) < 0:
                        print(red('[E] Item Quantity not in range'))
                        print(blue('[I]'), 'Enter Item Quantity:', end=' ')
                        ItemQuantity = input()
                        continue
                    else:
                        break
                def item_quantity():
                    return int(ItemQuantity)
                print(blue('[I]'), 'Enter Item Category:', end=' ')
                ItemCategory = input()
                while True:
                    try:
                        int(ItemCategory)
                        print(red('[E] Item Category must be string value'))
                        print(blue('[I]'), 'Enter Item Category:', end=' ')
                        ItemCategory = input()
                    except:
                        break
                def item_category():
                    return ItemCategory
                print(blue('[I]'), 'Enter Purchase Year of the Item:', end=' ')
                YearOfPurchase = input()
                while True:
                    try:
                        int(YearOfPurchase)
                    except:
                        print(red('[E] Purchase Year must be integer'))
                        print(blue('[I]'), 'Enter Purchase Year of the Item:', end=' ')
                        YearOfPurchase = input()
                        continue
                    if int(YearOfPurchase) < 2022:
                        print(red('[E] Purchase Year not in range'))
                        print(blue('[I]'), 'Enter Purchase Year of the Item:', end=' ')
                        YearOfPurchase = input()
                        continue
                    else:
                        break
                def year_of_purchase():
                    return YearOfPurchase
                print(blue('[I]'), 'Enter Purchase Month of the Item:', end=' ')
                MonthOfPurchase = input()
                while True:
                    try:
                        int(MonthOfPurchase)
                    except:
                        print(red('[E] Purchase Month must be integer value'))
                        print(blue('[I]'), 'Enter Purchase Month of the Item:', end=' ')
                        MonthOfPurchase = input()
                        continue
                    if int(MonthOfPurchase) < 1 or int(MonthOfPurchase) > 12:
                        print(red('[E] Purchase Month not in range.'))
                        print(blue('[I]'), 'Enter Purchase Month of the Item:', end=' ')
                        MonthOfPurchase = input()
                        continue
                    else:
                        break
                def month_of_purchase():
                    return MonthOfPurchase
                print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                DayOfPurchase = input()
                while True:
                    try:
                        int(DayOfPurchase)
                    except:
                        print(red('[E] Purchase Day must be integer value'))
                        print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                        DayOfPurchase = input()
                        continue
                    if (int(MonthOfPurchase) == 1) or (int(MonthOfPurchase) == 3) or (int(MonthOfPurchase) == 5) or (
                    int(MonthOfPurchase)) == 7 or (int(MonthOfPurchase)) == 8 or (int(MonthOfPurchase) == 10) or (
                            int(MonthOfPurchase) == 12):
                        if (int(DayOfPurchase) < 1) or (int(DayOfPurchase) > 31):
                            print(red('[E] Purchase Day not in range.'))
                            print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                            DayOfPurchase = input()
                            continue
                        else:
                            break
                    elif (int(MonthOfPurchase) == 4) or (int(MonthOfPurchase) == 6) or (int(MonthOfPurchase) == 9) or (
                            int(MonthOfPurchase) == 11):
                        if (int(DayOfPurchase)) < 1 or (int(DayOfPurchase) > 30):
                            print(red('[E] Purchase Day not in range.'))
                            print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                            DayOfPurchase = input()
                            continue
                        else:
                            break
                    elif int(MonthOfPurchase) == 2:
                        if int(YearOfPurchase) % 4 == 0:
                            if (int(DayOfPurchase)) < 1 or (int(DayOfPurchase) > 29):
                                print(red('[E] Purchase Day not in range.'))
                                print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                                DayOfPurchase = input()
                                continue
                            else:
                                break
                        else:
                            if (int(DayOfPurchase) < 1) or (int(DayOfPurchase) > 28):
                                print(red('[E] Purchase Day not in range.'))
                                print(blue('[I]'), 'Enter Purchase Day of the Item:', end=' ')
                                DayOfPurchase = input()
                                continue
                            else:
                                break
                def day_of_purchase():
                    return DayOfPurchase
                def item_purchase_date():
                    ItemPurchaseDate = str(day_of_purchase()) + '/' + str(month_of_purchase()) + '/' + str(
                        year_of_purchase())
                    return ItemPurchaseDate
                value = []
                value.insert(0, item_code())
                value.insert(1, item_name())
                value.insert(2, item_brand())
                value.insert(3, item_price())
                value.insert(4, item_quantity())
                value.insert(5, item_category())
                value.insert(6, item_purchase_date())
                LastList.append(value)
            else:
                LastList.append(value)
        print(blue('[I]') , 'Type console keyword [' , red('SID') , 'to save]:' , end = ' ')
        console = input()
        if console.upper() == 'SID':
            f = open('OneNetCafe.txt', 'a')
            f.truncate(0)
            f.seek(0)
            f = open('OneNetCafe.txt', 'a')
            for value in LastList :
                f.write(str(value))
                f.write('\n')
            f.close()
            print(blue('[O]') , 'Item record successfully updated.')
            print(blue('[I]') , 'Type console keyword:' , end = ' ')
            console = input()
        else :
            continue
    while console.upper() == 'VID' :
        f = open('OneNetCafe.txt', 'r')
        lines = f.read().splitlines()
        ItemCount = 0
        OutList = []
        SortList = []
        DescendingList =[]
        LastList = []
        for value in lines :
            OutList.append(eval(value.strip()))
        for list in OutList :
            SortList.append(int(list[0]))
            ItemCount += list[4]
        SelectList = SortList
        for valA in range(len(SortList)) :
            max = 0
            for valB in SelectList:
                if max < valB:
                    max = valB
                else:
                    pass
            DescendingList.append(max)
            SelectList.remove(max)
        for dec in DescendingList :
            for itemcode in OutList :
                if dec == int(itemcode[0]) :
                    LastList.append(itemcode)
                else :
                    pass
        t = PrettyTable(['Item Code' , 'Item Name' , 'Item Brand' , 'Item Price' , 'Item Quantity' , 'Item Category' , 'Item Puchased Date'])
        for value in LastList:
            t.add_row([value[0] , value[1] , value[2] , value[3] , value[4] , value[5] , value[6]])
        print(blue('[O]'))
        print(t)
        print(blue('[O]') , 'Claculating Item Total please wait', end='')
        time.sleep((0.5))
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print(blue('[O]') , 'Current Item Total is', cyan(ItemCount))
        print(blue('[I]') , 'Type console keyword:' , end = ' ')
        console = input()
    while console.upper() == 'SDD' :
        f = open('Dealers.txt', 'r')
        lines = f.read().splitlines()
        LastList = []
        OutList = []
        DealerList = []
        ValueNumber = 0
        RandomNumber1 = random.randint(1, 6)
        RandomNumber2 = random.randint(1, 6)
        if RandomNumber2 == RandomNumber1:
            while RandomNumber2 == RandomNumber1:
                RandomNumber2 = random.randint(1, 6)
        RandomNumber3 = random.randint(1, 6)
        if (RandomNumber3 == RandomNumber1) or (RandomNumber3 == RandomNumber2):
            while (RandomNumber3 == RandomNumber1) or (RandomNumber3 == RandomNumber2):
                RandomNumber3 = random.randint(1, 6)
        RandomNumber4 = random.randint(1, 6)
        if (RandomNumber4 == RandomNumber1) or (RandomNumber4 == RandomNumber2) or (RandomNumber4 == RandomNumber3):
            while (RandomNumber4 == RandomNumber1) or (RandomNumber4 == RandomNumber2) or (
                    RandomNumber4 == RandomNumber3):
                RandomNumber4 = random.randint(1, 6)
        print(blue('[O]'), 'Randomly selecting dealers please wait', end='')
        time.sleep((0.5))
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print(blue('[O]') , '4 Dealers selected randomly.They are:')
        for value in lines:
            OutList = eval(value.strip())
            OutList.insert(0,ValueNumber)
            ValueNumber += 1
            if RandomNumber1 == ValueNumber :
                OutList.pop(0)
                DealerList.append(OutList[0])
                LastList.append(OutList)
            elif RandomNumber2 == ValueNumber :
                OutList.pop(0)
                DealerList.append(OutList[0])
                LastList.append(OutList)
            elif RandomNumber3 == ValueNumber :
                OutList.pop(0)
                DealerList.append(OutList[0])
                LastList.append(OutList)
            elif RandomNumber4 == ValueNumber :
                OutList.pop(0)
                DealerList.append(OutList[0])
                LastList.append(OutList)
            else:
                pass
        print(DealerList)
        print(blue('[I]') , 'Type console keyword [' , red('VRL') , 'to display all the details]:' , end = ' ')
        console = input()
        if console.upper() != 'VRL' :
            break
        elif console.upper() == 'LDI' :
            break
        while console.upper() == 'VRL' :
            print(blue('[O]'))
            SelectList = []
            for location in LastList :
                SelectList.append(location[2])
            SelectList.sort()
            for value in SelectList :
                for location in LastList :
                    if value == location[2] :
                        print(location)
                        break
                    else:
                        pass
            print(blue('[I]') , 'Type console keyword [' , red('LDI') , 'to display the items of the given dealer]:' , end = ' ')
            console = input()
        while console.upper() == 'LDI':
            print(blue('[I]') , 'Enter the Dealer Name:' , end = ' ')
            DealerName = input()
            while True :
                try :
                    int(DealerName)
                    print(red('[E] Dealer name musyt be string value'))
                    print(blue('[I]'), 'Enter the Dealer Name:', end=' ')
                    DealerName = input()
                    continue
                except :
                    break
            f = open('DealerItems.txt', 'r')
            lines = f.read().splitlines()
            DealerItemList = []
            for itemlist in lines :
                DealerItemList.append(eval(itemlist.strip()))
            f.close()
            key = False
            for item in DealerItemList :
                if item[0].lower() == DealerName.lower() :
                    del item[0]
                    print(blue('[O]') , end = ' ')
                    print('Item Name :' , item[0], ',' , 'Item Brand :' , item[1], ',' , 'Item Price :' , item[2] ,',','Item Quantity :' ,item[3])
                    key = True
                else :
                    pass
            if key == False :
                print(red('[E] Dealer Name not Found'))
                continue
            print(blue('[I]') , 'Type console keyword: [' , red('LDI') , 'to display the items of the given dealer]:' , end = ' ')
            console = input()
    while  console.upper() == 'SID' :
        print(red('[E] You have to Add,Delete or Update item to save\n') ,
              '\tType' , red('AID')  , 'to add item.\n'
              '\tType' , red('DID') , 'to delete item.\n'
              '\tType'  , red('UID') , 'to update item.')
        print(blue('[I]') , 'Type console keyword:' , end = ' ')
        console = input()
    while console.upper() == 'ESC' :
        break
    while console.upper() == 'VRL' or console.upper() == 'LDI' :
        print(red('[E] First you have to select four dealers randomly\n') ,
              '\tTo select four dealers randomly type' , red('SDD') + '.')
        print(blue('[I]') , 'Type console keyword:' , end = ' ')
        console = input()
    while console.upper() != 'AID' and console.upper() != 'DID' and console.upper() != 'UID' and console.upper() != 'VID' and console.upper() != 'SDD'  and console.upper() != 'ESC' and console.upper() != 'VRL' and console.upper() != 'LDI':
        print(red('[E] Invalid console keyword'))
        print(blue('[I]') , 'Type console keyword:' , end = ' ')
        console = input()
print( green('G' , ['bold']) , end = '')            #This will print 'Good Bye!!!' like an animation.
time.sleep(0.1)
print( green('o' , ['bold']) , end = '')
time.sleep(0.1)
print( green('o' , ['bold']) , end = '')
time.sleep(0.1)
print( green('d' , ['bold']) , end = ' ')
time.sleep(0.1)
print( green('B' , ['bold']) , end = '')
time.sleep(0.1)
print( green('y' , ['bold']) , end = '')
time.sleep(0.1)
print( green('e' , ['bold']) , end = '')
time.sleep(0.1)
print( green('!' , ['bold']) , end = '')
time.sleep(0.1)
print( green('!' , ['bold']) , end = '')
time.sleep(0.1)
print( green('!' , ['bold']) , end = '')
time.sleep(0.4)








