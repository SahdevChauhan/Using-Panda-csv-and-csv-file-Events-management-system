import pandas as pd
import csv


class Marriage:

    def __init__(self, Index_No="", Husband_name="", Wife_name="", marrige_budget="", marrige_of_address="",sound_system=" "):
        self.Index_No = Index_No
        self.Husband_name = Husband_name
        self.Wife_name = Wife_name
        self.marrige_budget = marrige_budget
        self.marrige_of_address = marrige_of_address
        self.sound_system = sound_system

        """
        s = open("marriage.txt", "a+")
        s.write("\nIndex_No :{0}\nHusband name: {1}\nWife_name : {2}\nMarrige_budget : {3}\n"
                "Address : {4}\nSound_System : {5}".
                format(self.Index_No, self.Husband_name, self.Wife_name, self.marrige_budget, self.marrige_of_address,
                       self.sound_system))
        s.close()
        """

class Angagement:
    def __init__(self, Index_No=" ", Husband_name=" ", Wife_name=" ", Angagement_Budget=" ", address_of_Angagement=" "):
        self.Index_No = Index_No
        self.Husband_name = Husband_name
        self.Wife_name = Wife_name
        self.Angagement_Budget = Angagement_Budget
        self.address_of_Angagement = address_of_Angagement

        """s = open("Angagement.txt", "a+")

        s.write("\nIndex_No :{0}\nHusband name: {1}\nWife_name : {2}\nAngegement_badget : {3}\n"
                "Address : {4}".
                format(self.Index_No, self.Husband_name, self.Wife_name, self.Angagement_Budget,
                       self.address_of_Angagement
                       ))
        s.close()
        """


class Party:
    def __init__(self, Index_No, NameOfOrganiser=" ", cotsume=" ", AddressOfParty=" ", ListOfGuest=" ", Budgets=" "):
        self.Index_No = Index_No
        self.NameOfOrganiser = NameOfOrganiser
        self.cotsume = cotsume
        self.AddressOfParty = AddressOfParty
        self.ListOfGuest = ListOfGuest
        self.Budgets = Budgets

        """party = open("partys.txt", "a+")
        party.write(
            "\nIndex_No :{0}\nNameOfOrganiser : {1}\ncotsumer : {2}\nAddress : {3}\nListOfGuest : {4}\nBudgets : {5} "
            .format(self.Index_No, self.NameOfOrganiser, self.cotsume, self.AddressOfParty, self.ListOfGuest,
                    self.Budgets))
        party.close()
        """



    """
    f = open("marriage.txt", "r")
    print(f.read())
    f.close()

    angagement = open("Angagement.txt", "r")
    print(angagement.read())
    angagement.close()


    parties = open("partys.txt", "r")
    print(parties.read())
    parties.close()
    """


while True:
    print("1.Marrige_management\n2.Angagement_management\n3.Partys\n4.Display\n5.Exit")
    login = int(input("Enter your choice : "))
    while True:

        if login == 1:
            print("\n1.Add_record\n2.Search_record\n3.Food_Item\n4.Exit")
            choice = int(input("ENTER YOUR CHOICE : "))

            if choice == 1:
                Index = int(input("Enter Serial Number :"))
                Husband_name = input("Enter your Husband`s name : ")
                Wife_name = input("Wife Name: ")
                Budget = int(input("Enter budget : "))
                Address = input("Enter address : ")
                sound_system = input("Enter name of sound system : ")

                mrg1 = Marriage(str(Index), Husband_name, Wife_name, str(Budget), Address, sound_system)

                my_dict = pd.DataFrame({
                    'Index_No': [str(Index)],
                    'Husband_Name': [Husband_name],
                    'Wife_Name': [Wife_name],
                    'Marriage_Budget': [str(Budget)],
                    'Address': [Address],
                    'Sound_System': [sound_system]
                })

                my_dict.to_csv('MARRIAGE_DATA.csv', index=False, mode='a', header=True)

                # with open('MARRIAGE_DATA.csv', 'a') as f:
                #   my_dict.to_csv(f, mode='a', header=f.tell() == 0)
                # if file does not exist write header

            if choice == 2:
                print("\n1.Search By Index\n2.Search By Name")
                search_choice = int(input("Enter your choice :"))
                if search_choice ==1:

                    with open("MARRIAGE_DATA.csv" ) as csv_file:
                        SearchByIndex = csv.reader(csv_file)
                        Index_No = input("Please enter serial number : ")

                        for row in SearchByIndex:
                            if row[0] == Index_No:
                                print(row)

                    with open("MARRIAGE_FOOD.csv") as csv_file:
                        SearchByIndex = csv.reader(csv_file)
                        Index_No = input("Please enter serial number : ")

                        for row in SearchByIndex:
                            if row[0] == Index_No:
                                print(row)


                if search_choice == 2:
                    with open("MARRIAGE_DATA.csv") as csv_files:
                        SearchByName = csv.reader(csv_files)
                        Husband_Name = input("Please enter name of Boy whose detail you want to check : ")

                        for row in SearchByName:
                            if row[1] == Husband_Name:
                                print(row)


                """
                SE = input("please enter to search : ")
                search_file = open("marriage.txt", "r")
                checks_file = search_file.readlines()
                search_file.close()

                for LINES in checks_file:

                    try:
                        if LINES.split()[2] == SE:
                            print(" Found ")
                        else:
                            continue
                    except IndexError:
                        pass
                        """

            if choice == 3:
                print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
                CHOICE = int(input("Enter your choice : "))
                Serial_no_of_marriage_data = int(input("Enter Serial Number : "))
                if CHOICE == 1:
                    Gujratifood = input("Enter gujrati item :")
                    Index_No = int(input("Enter serial number :"))
                    #A = open("marriage.txt", "a")
                    #A.write("\nGujrati Food : " + Gujratifood)
                    df1 = pd.DataFrame({'Index_No ': [Index_No],
                        'Gujrati_Item ': [Gujratifood]})
                    df1.to_csv('MARRIAGE_FOOD.csv', index=False, mode='a')
                    #A.close()

                elif CHOICE == 2:
                    Panjabifood = input("Enter panjabi item :")
                    Index_No = int(input("Enter serial number :"))
                    #B = open("marriage.txt", "a")
                    #B.write("\nPanjabi Food : " + Panjabifood)

                    df2 = pd.DataFrame(
                        {'Index_No ': [Index_No],
                            'Panjabi_Food ': [Panjabifood]})
                    df2.to_csv('MARRIAGE_FOOD.csv', index=False, mode='a')
                    #B.close()

                elif CHOICE == 3:
                    Chinesefood = input("Enter Chinese item :")
                    Index_No = int(input("Enter serial number :"))
                    #C = open("marriage.txt", "a")
                    #C.write("\nChinese Food : " + Chinesefood)

                    df3 = pd.DataFrame({'Index_No ': [Index_No],
                        'Chinese_Food': [Chinesefood]})
                    df3.to_csv('MARRIAGE_FOOD.csv', index=False, mode='a')
                    #C.close()

                elif CHOICE == 4:
                    Japanesefood = input("Enter Japanese item :")
                    Index_No = int(input("Enter serial number :"))
                    #D = open("marriage.txt", "a")
                    #D.write("\nJapanese Food : " + Japanesefood)
                    df4 = pd.DataFrame({'Index_No ': [Index_No],
                        'Japanese_Food ': [Japanesefood]})
                    df4.to_csv('MARRIAGE_FOOD.csv', index=False, mode='a')
                    #D.close()


            if choice == 4:
                exit()

        if login == 2:
            print("\n1.Add_record\n2.Search_record\n3.Food_Item\n4.Exit")
            Ang = int(input("ENTER YOUR CHOICE : "))

            if Ang == 1:
                Index = int(input("Enter Serial Number :"))
                Husband = input("Enter your Husband`s name : ")
                wife = input("Enter your Wife`s name : ")
                Angage_Budgets = int(input("Enter budget : "))
                Address = input("Enter address : ")
                Angage = Angagement(str(Index), Husband, wife, str(Angage_Budgets), Address)

                df = pd.DataFrame({
                    'Index_No ': [str(Index)],
                    'Husband name': [Husband],
                    'Wife_name': [wife],
                    'Angegement_badget': [str(Angage_Budgets)],
                    'Address': [Address]
                })
                df.to_csv('ANGAGEMENT_DATA.csv', index=False, mode='a', header=True)

            if Ang == 2:
                print("\n1.Search By Index\n2.Search By Name")
                search_choice = int(input("Enter your choice :"))
                if search_choice == 1:
                    with open("ANGAGEMENT_DATA.csv") as csv_file:
                        SearchByIndex = csv.reader(csv_file)
                        Index_No = input("Please enter serial number : ")

                        for row in SearchByIndex:
                            if row[0] == Index_No:
                                print(row)
                    with open("ANGAGEMENT_FOOD.csv") as csv_file:
                        SearchByIndex = csv.reader(csv_file)
                        Index_No = input("Please enter serial number : ")

                        for row in SearchByIndex:
                            if row[0] == Index_No:
                                print(row)

                if search_choice == 2:
                    with open("ANGAGEMENT_DATA.csv") as csv_file:
                        SearchByName = csv.reader(csv_file)
                        Husband_Name = input("Please enter name of Boy whose detail you want to check : ")

                        for row in SearchByName:
                            if row[1] == Husband_Name:
                                print(row)


                """
                SEARCH = input("please enter to search : ")
                SEARCH_FILE = open("Angagement.txt", "r")
                check_file = SEARCH_FILE.readlines()
                SEARCH_FILE.close()

                for line in check_file:
                    try:
                        if line.split()[2] == SEARCH:
                            print(" Found ")
                        else:
                            continue
                    except IndexError:
                        pass
                        

                SEARCH = input("please enter to search : ")
                search_file = open("Angagement.txt", "r")
                check_file = search_file.readlines()
                search_file.close()

                for data in check_file:
                    search_word = re.findall(" ", data)
                    print("found")
                    break

"""

            if Ang == 3:
                while True:

                    print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
                    check = int(input("Enter your choice : "))

                    Serial_no_of_Angagement_data = int(input("Enter Serial Number : "))
                    if check == 1:
                        GujratiFood = input("Enter gujrati item :")
                        Index_No = int(input("Enter serial number :"))
                        #A = open("Angagement.txt", "a")
                        #A.write("\nGujrati Food : " + GujratiFood)
                        DATAFRAME2 = pd.DataFrame({'Index_No ': [Index_No],
                            'Gujrati_Item ': [GujratiFood]})
                        DATAFRAME2.to_csv('ANGAGEMENT_FOOD.csv', index=False, mode='a')
                        #A.close()

                    elif check == 2:
                        PanjabiFood = input("Enter panjabi item :")
                        Index_No = int(input("Enter serial number :"))
                        #B = open("Angagement.txt", "a")
                        #B.write("\nPanjabi Food : " + PanjabiFood)
                        df6 = pd.DataFrame({'Index_No ': [Index_No],
                            'Panjabi Food': [PanjabiFood]})
                        df6.to_csv('ANGAGEMENT_FOOD.csv', index=False, mode='a')
                        #B.close()

                    elif check == 3:
                        ChineseFood = input("Enter Chinese item :")
                        Index_No = int(input("Enter serial number :"))
                        #C = open("Angagement.txt", "a")
                        #C.write("\nChinese Food : " + ChineseFood)
                        df7 = pd.DataFrame({'Index_No ': [Index_No],
                            'Chinese Food ': [ChineseFood]})
                        df7.to_csv('ANGAGEMENT_FOOD.csv', index=False, mode='a')
                        #C.close()

                    elif check == 4:
                        JapaneseFood = input("Enter Japanese item :")
                        Index_No = int(input("Enter serial number :"))
                        #D = open("Angagement.txt", "a")
                        #D.write("\nJapanese Food : " + JapaneseFood)
                        df8 = pd.DataFrame({'Index_No ': [Index_No],
                            'Japanese Food \t': [JapaneseFood]})
                        df8.to_csv('ANGAGEMENT_FOOD.csv', index=False, mode='a')
                        #D.close()

            if Ang == 4:
                exit()

        if login == 3:
            print("\n1.Culture party\n2.College party\n3.Birthday party\n4.Exit")
            party_choice = int(input("Enter Your choice : "))

            if party_choice == 1:
                print("\n1.Add data\n2.Food service")
                party_data = int(input("Enter your choice :"))
                if party_data ==1:

                    Index = int(input("Enter Serial Number :"))
                    name_Of_Organiser = input("Enter name Of the Organiser : ")
                    Costume = input("Enter types of Costume : ")
                    Address = input("Enter the address of the party : ")
                    List_Of_Guest = int(input("Enter number of guest in party :"))
                    Party_Budget = int(input("Enter party budget : "))
                    par1 = Party(Index, name_Of_Organiser, Costume, Address, str(List_Of_Guest), str(Party_Budget))

                    df = pd.DataFrame({
                        'Index_No\t ': [str(Index)],
                        'Organiser \t': [name_Of_Organiser],
                        'Costume\t': [Costume],
                        'Address\t': [Address],
                        'List_Of_Guest\t ': [str(List_Of_Guest)],
                        'Budget\t': [Party_Budget]
                    })
                    df.to_csv('CULTURAL_PARTYS.csv', index=False, mode='a')

                if party_data == 2:
                    print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
                    food = int(input("Enter your choice : "))
                    Serial_no_of_Partyes_data = int(input("Enter your choice: "))
                    if food == 1:
                        Gujrati_Food = input("Enter gujrati item :")
                        # guj = open("partys.txt", "a")
                        # guj.write("\nGujrati Food : " + Gujrati_Food)
                        Index_No = int(input("Enter serial number :"))
                        # D = open("Angagement.txt", "a")
                        # D.write("\nJapanese Food : " + JapaneseFood)

                        Birth = pd.DataFrame({'Index_No ': [Index_No],
                                            'Gujrati_Food ': [Gujrati_Food]})
                        Birth.to_csv('Cultural_food.csv', index=False, mode='a')

                        # guj.close()

                    elif food == 2:
                        Panjabi_Food = input("Enter panjabi item :")
                        # pan = open("partys.txt", "a")
                        # pan.write("\nPanjabi Food : " + Panjabi_Food)
                        Index_No = int(input("Enter serial number :"))

                        Birth = pd.DataFrame({'Index_No ': [Index_No],
                                            'Panjabi_Food ': [Panjabi_Food]})
                        Birth.to_csv('Cultural_food.csv', index=False, mode='a')


                        # pan.close()

                    elif food == 3:
                        Chinese_Food = input("Enter Chinese item :")
                        # Chin = open("partys.txt", "a")
                        # Chin.write("\nChinese Food : " + Chinese_Food)

                        Index_No = int(input("Enter serial number :"))
                        Birth = pd.DataFrame({'Index_No': [Index_No],
                                            'Panjabi_Food ': [Chinese_Food]})
                        Birth.to_csv('Cultural_food.csv', index=False, mode='a')
                        # Chin.close()

                    elif food == 4:
                        Japanese_Food = input("Enter Japanese item :")
                        # japa = open("partys.txt", "a")
                        # japa.write("\nJapanese Food : " + Japanese_Food)
                        Index_No = int(input("Enter serial number :"))

                        Birth = pd.DataFrame({'Index_No': [Index_No],
                            'Japanese_Food ': [Japanese_Food]})
                        Birth.to_csv('Cultural_food.csv', index=False, mode='a')
                        # japa.close()



            if party_choice == 2:
                print("\n1.Add data\n2.Food service")
                party_data = int(input("Enter your choice :"))
                if party_data == 1:
                    Index = int(input("Enter Serial Number :"))
                    Name_of_Organiser = input("Enter name Of the Organiser : ")
                    CostumeOfStudent = input("Enter types of Costume : ")
                    AddressOfParty = input("Enter the address of the party : ")
                    List_Of_Student = int(input("Enter number of guest in party :"))
                    Party_budget = int(input("Enter party budget : "))
                    par2 = Party(Index, Name_of_Organiser, CostumeOfStudent, AddressOfParty, str(List_Of_Student),
                                 str(Party_budget))
                    df = pd.DataFrame({
                        'Index_No\t ': [str(Index)],
                        'Organiser \t': [Name_of_Organiser],
                        'Costume\t': [CostumeOfStudent],
                        'Address\t': [AddressOfParty],
                        'List_Of_Guest\t ': [str(List_Of_Student)],
                        'Budget\t': [Party_budget]
                    })
                    df.to_csv('COLLEGE_PARTYS.csv', index=False, mode='a')

                if party_data == 2:
                    print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food\n5.Exit")
                    food = int(input("Enter your choice : "))
                   #Serial_no_of_Partyes_data = int(input("Enter serial number: "))
                    if food == 1:
                        Index_No = int(input("Enter serial number :"))
                        Gujrati_Food = input("Enter gujrati item :")
                        # guj = open("partys.txt", "a")
                        # guj.write("\nGujrati Food : " + Gujrati_Food)

                        # D = open("Angagement.txt", "a")
                        # D.write("\nJapanese Food : " + JapaneseFood)

                        Birth = pd.DataFrame({'Index_No ': [Index_No],
                                              'Gujrati_Food ': [Gujrati_Food]})
                        Birth.to_csv('College_food.csv', index=False, mode='a')

                        # guj.close()

                    elif food == 2:
                        Panjabi_Food = input("Enter panjabi item :")
                        # pan = open("partys.txt", "a")
                        # pan.write("\nPanjabi Food : " + Panjabi_Food)
                        Index_No = int(input("Enter serial number :"))

                        Birth = pd.DataFrame({'Index_No ': [Index_No],
                                              'Panjabi_Food ': [Panjabi_Food]})
                        Birth.to_csv('College_food.csv', index=False, mode='a')

                        # pan.close()

                    elif food == 3:
                        Chinese_Food = input("Enter Chinese item :")
                        # Chin = open("partys.txt", "a")
                        # Chin.write("\nChinese Food : " + Chinese_Food)

                        Index_No = int(input("Enter serial number :"))
                        Birth = pd.DataFrame({'Index_No': [Index_No],
                                              'Panjabi_Food ': [Chinese_Food]})
                        Birth.to_csv('College_food.csv', index=False, mode='a')
                        # Chin.close()

                    elif food == 4:
                        Japanese_Food = input("Enter Japanese item :")
                        # japa = open("partys.txt", "a")
                        # japa.write("\nJapanese Food : " + Japanese_Food)
                        Index_No = int(input("Enter serial number :"))

                        Birth = pd.DataFrame({'Index_No': [Index_No],
                                              'Japanese_Food ': [Japanese_Food]})
                        Birth.to_csv('College_food.csv', index=False, mode='a')
                        # japa.close()



            if party_choice == 3:
                print("\n1.Add data\n2.Food service")
                party_data = int(input("Enter your choice :"))
                if party_data == 1:
                    Index = int(input("Enter Serial Number :"))
                    Name_Of_organiser = input("Enter name Of the Organiser : ")
                    Costumes = input("Enter types of Costume : ")
                    Addrese = input("Enter the address of the party : ")
                    ListGuests = input("Enter number of guest in party :")
                    Party_Budgets = int(input("Enter party budget : "))
                    par3 = Party(Index, Name_Of_organiser, Costumes, Addrese, ListGuests, str(Party_Budgets))

                    df = pd.DataFrame({
                        'Index_No': [str(Index)],
                        'Organiser ': [Name_Of_organiser],
                        'Costume': [Costumes],
                        'Address': [Addrese],
                        'List_Of_Guest ': [str(ListGuests)],
                        'Budget': [Party_Budgets]
                    })
                    df.to_csv('BIRTHDAY_PARTYS.csv', index=False, mode='a')

                if party_data == 2:
                    print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
                    food = int(input("Enter your choice : "))
                    #Serial_no_of_Partyes_data = int(input("Enter your choice: "))
                    if food == 1:
                        Index_No = int(input("Enter serial number :"))
                        Gujrati_Food = input("Enter gujrati item :")
                        # guj = open("partys.txt", "a")
                        # guj.write("\nGujrati Food : " + Gujrati_Food)

                        # D = open("Angagement.txt", "a")
                        # D.write("\nJapanese Food : " + JapaneseFood)

                        Birth = pd.DataFrame({'Index_No ': [Index_No],
                                              'Gujrati_Food ': [Gujrati_Food]})
                        Birth.to_csv('Birth_food.csv', index=False, mode='a')

                        # guj.close()

                    elif food == 2:
                        Index_No = int(input("Enter serial number :"))
                        Panjabi_Food = input("Enter panjabi item :")
                        # pan = open("partys.txt", "a")
                        # pan.write("\nPanjabi Food : " + Panjabi_Food)

                        Birth = pd.DataFrame({'Index_No ': [Index_No],
                                              'Panjabi_Food ': [Panjabi_Food]})
                        Birth.to_csv('Birth_food.csv', index=False, mode='a')

                        # pan.close()

                    elif food == 3:
                        Index_No = int(input("Enter serial number :"))
                        Chinese_Food = input("Enter Chinese item :")
                        # Chin = open("partys.txt", "a")
                        # Chin.write("\nChinese Food : " + Chinese_Food)


                        Birth = pd.DataFrame({'Index_No': [Index_No],
                                              'Panjabi_Food ': [Chinese_Food]})
                        Birth.to_csv('Birth_food.csv', index=False, mode='a')
                        # Chin.close()

                    elif food == 4:
                        Index_No = int(input("Enter serial number :"))
                        Japanese_Food = input("Enter Japanese item :")
                        # japa = open("partys.txt", "a")
                        # japa.write("\nJapanese Food : " + Japanese_Food)
                        Birth = pd.DataFrame({'Index_No': [Index_No],
                                              'Japanese_Food ': [Japanese_Food]})
                        Birth.to_csv('Birth_food.csv', index=False, mode='a')
                        # japa.close()

                if party_choice ==4:
                    exit()

        if login == 4:
            print("\n1.Marriage data\n2.Angagement data\n3.Exit")
            file_data = int(input("Enter your choice :"))
            if file_data == 1:
                with open('MARRIAGE_DATA.csv', 'r')as Marriage_File:
                    data = csv.reader(Marriage_File)
                    for row in data:
                        print(row)

            if file_data ==2:
                with open('ANGAGEMENT_DATA.csv', 'r')as Angagement_File:
                    data = csv.reader(Angagement_File)
                    for row in data:
                        print(row)

            if file_data ==3:
                exit()


        if login ==5:
            exit()
