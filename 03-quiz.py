import json


points = 0      #liczyc punkty

def show_question(questions):                # tworzymy funkcje show question
    #tutaj przekazujemy nasze pytania 
    global points
    print()
    print(questions["pytanie"])          # i będziemy teraz wyswietlac pytania i odpowiedzi
    print("a:",questions["a"])           #questions["a"] poniewaz tak mamy zapisane w quiz.json
    print("b:",questions["b"])  
    print("c:",questions["c"])
    print("d:",questions["d"])  
    print()            
    
    answer = input("Którą odpowiedz wybierasz ?")          #pytamy uzytkownik ktora odpowiedz jest prawidłowa
    #do zmiennej answer przypiszemy to co poda uzytkownik 
    #na terminalu pojawia sie pytania i odpowiedzi i na koniec (input)

    if answer == questions["prawidłowa odpowiedz"].lower():
    #if answer == questions["prawidłowa odpowiedz"]:
    #zeby liczyly sie punkty musimy porownac to co podał uzytkownik z polem Prałidwoła odpowiedz w pliku quiz.json
        
        points += 1     #jezei prawidlowa odpowedz dodajemy jeden punkt   #points zmienna globalna bo na poczatku 
        #jest napisane points = 0   / global points (teraz mozemy modyfikowac tą zmienną )

        print("To prawidłowa odpowiedz brawo elo naula.Masz juz: ",points,"punktów")
    else:                                                   #jezeli
        print("Niestyty zla odpowiedz wypierdalaj,prawidłowa odowiedz to",questions["prawidłowa odpowiedz"])

        
with open ('quiz.json') as json_file :      #otworzyc nasz plik z pytaniami #json_file zrobilismy zmienna
    questions = json.load(json_file)                                    #dane w formacie json
     
    for i in range(0,len(questions)): #korzystamy  pętli for (od o do len questions) przechodzimy przez 
    #wszystkie pytania 
    #   print(questions[i]["pytanie"]) #pobiermy pierwszy element z listy pytan i odpowiedzi w pliku wezel
    #wyświetlą sie wszystkie pytania
     
    #tworzymy jednak osobną funkcje 
        show_question(questions[i])
    #rezygnujemy z pytania bo chcemy do show_questin przekazac pytania i odpowiedzi i info poprawnej odp.


print()                         #kiedy nasz program bedzie się konczyl wyswietlimy informacje 
print("Tokoniec gry zdobyta liczba punktów to :" + str(points) + ".")        #zamiast , dajemy + polaczyc te elementy
#Dodajemy funkcje str(points) dla tego ze python niewie czy + to polaczyc elementy czy cos dodac
  


#1.po koleji pokazywac pytania uzytkownikowi
#2.chcemy pytac uzytkownika o wlasciwa odpowiedz
#3.dodwac punkty jezeli uzytkownk udzieli wlasciwej odpowiedzi