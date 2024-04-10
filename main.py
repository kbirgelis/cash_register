#
# Kases aparāts
#
#ir  0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#ir     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
#ir  0.5pt dzēst preci pēc kārtas numura
#ir  0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
#ir 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#ir    0.5pt izdrukāt piemēroto atlaidi (ja ir)
#ir    0.5pt izdrukāt kopējo summu

# ir1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# ir 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# ir 1pt koda palaišanas brīdī nerādās kļūdas
# ir 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# būs 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import json

jaysons = []
produkta_nosaukums = []
jauna_prece = []
produkta_cena = []
produktu_summa = []
produktu_summa_atlaide = []
jaysons_2 = []
produktu_sum = []
Summa = []
ietaupijums = []
samaksa = []
nauda = []
with open('jayjay.json', 'r') as openfile:

    jaysons = json.load(openfile)

    jaysons_2 = jaysons

while True: #Kamēr kods ir patiess, tiek atkārtotas sekojošās komandas
    print("\nKases aparāts!")
    print("-+-+-+-+-+-+-+-+-+-+-+")
    print("Izvēlies savu nākošo soli zemāk:")
    print("1. Pievienot jaunu preci")
    print("2. Dzēst preci pēc kārtas nummura")
    print("3. Iztukšot preču sarakstu")
    print("4. Piemērot atlaidi visam pirkumam")
    print("5. Izdrukāt gatavu čeku")
    print("")
    print("6. Iziet no kases aparāta sistēmas")
    print("")
    choice = input("Ievadis savu izvēli: ")

    if choice == "1": #Ja tiek izvēlēta preces pievienošana tad tiek aktivizēts sekojošais kods
        produkta_nosaukums = input("Ievadi preces nosaukumu: ")
        produkta_cena = input("Super! Ievadi produkta cenu: ")

        if type(produkta_cena) != int:  #Ja produkta cenas vietā ierakstīts burts, tad tiek izprintēta ziņa
                print("Produkta cena tika ievadīta nepareizi!")
        if produkta_cena < '0': #Ja produkta cena ir negatīva, tad tiek izprintēta ziņa
                print("Produkta cena tika ievadīta nepareizi!")
        if produkta_cena > '9999': #Ja produkta cena ir virs 9999, tad tiek izprintēta ziņa
                print("Produtka cena tika ievadīta nepareizi!")

        jauna_prece = {'nosaukums': produkta_nosaukums, 'cena': produkta_cena}
        produktu_sum.append(int(produkta_cena))
        jaysons_2.append(jauna_prece) #!!!!!!!!!!!

    elif choice == "2": #Ja choice ir 2, tad tiek dota iespēja dzēst preci pēc tās kārtas nummura.
        id_2 = int(input("Ievadi preces kārtas nummuru, kuru vēlies dzēst: "))
        jaysons_2.pop(id_2)
        print("Prece tika veiksmīgi dzēsta!")
    
    elif choice == "3": #Ja tiek ierakstīts 3, tad preču saraksts tiek iztukšots ar sekojošā koda palīdzību.
        print("* PREČU SARAKSTU NAV IESPĒJAMS ATJAUNOT, JA TAS TIEK DZĒSTS! *")
        confirmation_delete = input("Vai tu tiešām vēlies dzēst visu preču sarakstu?(Ja/Ne): ")

        if confirmation_delete == 'Ja': #Ja lietotājs uzraksta 'Ja', tad tiek aktivizēts sekojošais kods
              jaysons_2.clear
        if confirmation_delete == 'Ne': #Ja lietotājs uzraksta 'Ne', tad tiek aktivizēts sekojosais kods
              print("Preču saraksta dzēšana tika atcelta!")
        
    elif choice == "4":

        total = sum(produktu_sum)

        preces_atlaide = int(input("Ieraksti procentuālu skaitu piemērotajai atlaidei: "))

        atlaide_temp = int(100 - preces_atlaide)

        produktu_summa_atlaide = (total / 100) * atlaide_temp

        ietaupijums = total - produktu_summa_atlaide

        print("summa" + str(total))
        print("summa ar atlaidi" + str(produktu_summa_atlaide))

    elif choice == "5": #Ja tiek izvēlēta piektā opcija tad tiek Izdrukāts gatavs čeks
         print("Kristera kases aparāts!")
         print("=======================")
         print("10.04.2024")
         print("")
         print(jaysons)
         total = sum(produktu_sum)
         print("")
         print("Jūsu kopsumma (pirms atlaides): " + str(total))
         print("Jūsu kopsumma: " + str(produktu_summa_atlaide))
         print("")
         print("=======================")

         samaksa = input("Ievadiet summu, kuru jūs vēlaties samaksāt par pirkumu!: ")
         if samaksa < produktu_summa_atlaide:
              print("Nepietiek naudas!")
         if samaksa >= produktu_summa_atlaide:
              nauda = samaksa - produktu_summa_atlaide
              print("Jūsu atlikums ir " + nauda)

    elif choice == "6": #Ja tiek izvēlēta sestā opcija, tad fails tiek saglabāt uz JSON
         with open("jayjay.json", "w") as jayson_file:
              json.dump(jaysons, jayson_file)
              print("Tiek veikta kases sistēmas aizvēršana...")
         break




        

