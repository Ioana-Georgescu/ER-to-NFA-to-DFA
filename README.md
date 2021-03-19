# ER-to-NFA-to-DFA
Transformarea unei expresii regulate (ER) intr-un automat finit detrminist (AFD/DFA)
in Python 3

Expresia este transformata intai intr-un automat finit nedetrminist (AFN/NFA) care
este apoi convertit intr-un AFD

Rulare: python3 main.py <input-file-ER> <output-file-AFN> <output-file-AFD>

Format input-file-ER:
	litere mici din intervalul 'a'...'z'
	ab sau (ab) - concatenarea a 2 subexpresii
	a|b sau (a|b)- reuniunea a 2 subexpresii
	(a)∗ - kleene star aplicat unei subexpresii

Format output-file-AFN si output-file-AFD:
<numarul de stari>
<lista de stari finale separate de cate un spatiu>
<tranzitie: stare_initiala simbol lista_starilor_urmatoare>

starea intiala = 0
epsilon = eps

Exmplu output-file-AFN:
3
2
0 a 0
0 b 0 1
1 a 2
1 b 2
1 eps 2

Exmplu output-file-AFD:
4
2 3
0 b 1
0 a 0
1 b 2
1 a 3
2 b 2
2 a 3
3 b 1
3 a 0


Am folosit ANTLR4 pentru generarea arborelui de parsare pornind de la gramatica
descrisa in Regex.g4
Am ignorat whitespace in parsare
Am rezolvat cazul mai multor Kleene star cosecutive prin definirea KLEENE ca un
sir de minim o *
Am definit reguli tinand cont de ordinea operatiilor: de la operatia care se
executa ultima la prima pentru a ma asigura ca arborele e format corespunzator


------------------------------------------------------------------------------
Am extins clasa RegexVisitor in RegexToNFAVisitor unde am creat alfabetul,
tranzitiile si multimea starilor pt NFA
Am folosit logica prezenata la cursul 5 pentru realizarea operatiilor intre
automatele care accepta un simbol => automatul va avea o singura stare finala
Functia .visit(tree) va intoarce acesata stare finala
Pe masura ce am parcurs arborele in fiecare dintre funciile de vizitare am
adaugat stari si tranzitii si am intors starea finala a secventei nou
construite

Functia de vizitare a unui simbol creaza tranzitiile pentru un automat cu doua
stari care accepta acel simbol

Functia de vizitare pentru regula de atom adauga ori tranzitiile pentru un
automat pentru un simbol ori pentru automatul pentru expresia dintre paranteze

Functia de vizitare pentru regula de Kleene star tine minte starea curenta,
adauga o stare noua si pornind de la aceasta stare adauga tranzitiile pentru
automatul care ar accepta expresia careia i se aplica. Adauga o tranzitie de la
starea finala la starea initiala a miniautomatului pentru ciclare, o noua stare
finala si o tranzitie pentru producerea lui epsilon, conform schemei de la curs

Functia de vizitare pentru regula de concatenare genereaza pe rand tranzitiile
necesare automatelor care ar accepta fiecare jumatate a expresiei apoi leaga
satrea finala a primului cu starea initiala a celui de-al doilea printr-o
tranzitie pe epsilon

Functia de vizitare pentru regula de reuniune genereaza pe rand tranzitiile
necesare automatelor care ar accepta fiecare jumatate a expresiei apoi leaga
starile lor initiale la o noua stare initiala si cele finale la o noua satare
finala prin tranzitii pe epsilon

Tranzitiile sunt stocate intr-un dictionar cu cke tuplu (stare, simbol) si
valori liste de stari. La adaugare unei tranzitii trebuie sa verific daca
trebuie creata o tranzitie noua sau doar adaugata o stare la valoarea unei
tranzitii deja existente
La crearea unei stari noi trebuie s-o adaug in lista de stari. Lista de stari e
un set pentru a introduce elemente usor fara riscul de a avea duplicate

Starea curenta (current_state) porneste de la 0 (starea initiala) si creste de
fiecare data cand adug o stare. Este folosita pentru a ma asigura ca nu
denumesc doua stari la fel si pentru a putea tine usor minte care sunt starile
initiale si finale ale automatelor intermediare create pe parcurs


------------------------------------------------------------------------------
NFAandDFA.py:

NFA:
Starile sunt un set de numere intregi
Tranzitiile sunt memorate ca un dictionar

Calculez toate inchiderile epsilon si le tin minte intr-un dictionar pentru ca
imi vor trebui cand determin starile accesibile pentru un caracter si vreau sa
evit recalcularea lor

epsilonClosure:
toate starile accesibile din starea parametru doar prin tranzitii epsilon

checkDown:
metoda recursiva pentru a descoperi starile pentru epsilonClosure

reachableOnSymbol:
un set cu toate starile in care se poate ajunge din starea parametru cu
simbolul parametru. Automatul poate trece prin oricate tranzitii epsilon atat
timp ca trece si printr-o trazitie care consuma simbolul


DFA:
Starile sunt o lista de tupluri de numere intregi. Am schimbat de la set la
lista pentru ca trebuie sa ma asigur ca starea initiala e prima si seturile nu
permit inserarea pe o anumita pozitie
Pentru a scrie starile ca numere in fisier ma voi referi la ele dupa indexul pe
care il au in lista de stari
DFA-ul are acelasi alfabet ca NFA-ul din care provine

printDFA:
scrie DFA-ul in fisier


nfaFromFile:
citeste fisierul de intrare si creeaza NFA-ul corespunzator


convert:
primeste un NFA, creeaza DFA-ul corespnzator si il scrie in fisierul de iesire
O stare pentru DFA va fi un tuplu de stari NFA, cu exeptia lui sink state
Pentru un DFA cu n stari, sink state e reprezenta de numarul n+1
In crearea starilor si listelor cu stari si cu stari finale folosec seturi
pentru a nu risca introducerea unei valori deja existente

E posibil ca DFA sa nu aiba nevoie de sink state => nu are rost sa adaug toate
tranzitiile de la sink state la sink state pentru toate simbolurile din alfabet
Verific daca imi trebuie sink state prin variabila needs_sink

Un element din setul cu toate starile DFA-ului va fi format dintr-o stare (un
tuplu de intregi) si un status (0 = nu am defnit inca tranzitiile care pornesc
din aceasta stare pentru fiecare simbol din alfabet, 1 = am definit toate
tranzitiile). Statusul ma ajuta sa ma asigur ca nu definesc tranzitiile unei
stari de mai multe ori

nextON =  un dictionar cu toate starile accesibile pentru fiecare pereche
(stare NFA, simbol din alfabet). Il completez la inceput pentru a nu trebui
sa recalculez valorile. Il tin ca dictionar pentru a accesa usor elementele

Voi construi DFA-ul pornind de la inchiderea epsilon a starii initiale a
DFA-ului si adaugarea de noi stari pe masura ce definesc tranzitii. Ma voi opri
cand toate starile DFA-ului au statusul 1

La fiecare pas iau prima stare DFA din lista celor cu status 0
Verific daca contine cel putin o satre finala a DFA-ului folosid intersectia
seturilor. Daca da, o adaug la setul starilor finale. Fac verificarea asta
imediat ce am ales starea pentru ca e posibil ca starea initiala a NFAului sa
fie si stare finala
Pentru fiacare simbol din alfabet starea la care duce tranzitia pe el = nextOn
pentru fiecare stare NFA din satrea DFA curenta
Daca setul obtinut e gol => nu se poate ajunge in nicio alta stare pe simbolul
curent => tanzitia pe el va duce la sink state
Altfel adaug in dictionarul de tranzitii tranzitia spre noua stare si verific
daca starea noua exista deja in lista de stari cu statusul 1. Daca nu => nu a
fost inca descoperita / analizata => o adaug cu status 0
Dupa ce iterez prin tot alfabetul sterg intrarea de status 0 pentru starea
curenta si adaug una cu status 1

Daca a trebuit sa definesc cel putin o tranzitie catre sink state trebuie sa-i
adaug tranzitiile catre ea insusi in dictioanarul de tranzitii. Daca nu,
trebuie sa scot sink state din setul de stari

Elimin statusurile din setul cu starile DFA-ului, creez DFA-ul si il scriu in
fisier


------------------------------------------------------------------------------
In main am parsat sirul din fisierul de input, am vizitat arborele si am
reurnat starea finala, am initializat un NFA cu elementele create in visitor,
l-am printat, l-am convertit la DFA si l-am printat
