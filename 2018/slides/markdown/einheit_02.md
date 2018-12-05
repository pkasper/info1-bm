# 706.088 Informatik 1
### Einführung in die Programmierung


### Wiederholung


### Zusammenfassung - Überblick
* Werkzeuge zur Programmierung
  * Compiler, Interpreter
* Python3
  * Strukturen, Variablen, Schleifen etc.



Wie wird aus "Text" ein ausführbares Programm?


## Programmier Werkzeuge
Bei der Übersetzung von **Quellcode (Source-Code)**,
geschriebenem Programmcode,
übersetzt der Computer das Programm in Maschinensprache.

2 Arten der Übersetzung…


* **Compiler**
  * einmalige Übersetzung in eine Binärdatei
* **Interpreter**
  * Interpretation des Quellcodes bei der Ausführung


## Compiler
* übersetzt Befehle in Maschinensprache
* Das entstandene Programm enthält nur mehr Maschinenbefehle
  * ist nicht mehr für den Menschen lesbar
  * als Binärdatei gespeichert
* Übersetzung findet **einmalig** statt
* Vorgang wird "Compilierung" genannt
* Computer führt Programm direkt aus


## Interpreter
* ähnlich zum Compiler wird das Programm in Maschinensprache ausgeführt, allerdings
  * wird jeder Befehl erst bei seiner Ausführung übersetzt
  * entsteht kein zusätzliches, übersetztes Programm
* Programme werden **bei jeder Ausführung erneut übersetzt**
* Dieser Vorgang wird als "Interpretation" bezeichnet
* Je nach Art des Programms kann die Verwendung eines Compilers Geschwindigkeitsvorteile bringen



### Voraussetzungen für die Übung
* Computer (Linux, Mac Os X, Windows)
  * kein Tablet
  * kein Handy
* Texteditor (Atom, vim, Emacs, Notepad, etc)
* Konsole (xterm, Terminal.app, etc.)
* Python3 Interpreter (CPython)



# Python<!-- .element: class="light shadow" -->
<!-- .slide: data-background-image="imgs/02/photo-1474314170901-f351b68f544f.jpeg" -->


## Python3
* für Übung: Python 3.5
* gut lesbar, klar strukturiert <!-- .element: class="fragment" data-fragment-index="1" -->
* interpretiert <!-- .element: class="fragment" data-fragment-index="2" -->
* seit 1991, Python3 seit 2008 <!-- .element: class="fragment" data-fragment-index="3" -->
* läuft auf allen gängigen Betriebssystemen <!-- .element: class="fragment" data-fragment-index="4" -->


### Python
* Informationen zu Python:  [www.python.org](https://www.python.org)
* Python Dokumentation:  [docs.python.org](https://docs.python.org/3/)
* Python Tutorial: [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial)


## Pyhon Cheatsheets
Google: Python Cheat Sheet
* [www.cogsci.rpi.edu\[...\]pdf](http://www.cogsci.rpi.edu/~destem/igd/python_cheat_sheet.pdf)
* [www.astro.up.pt\[...\]pdf](http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf)
* [Such Link…](http://lmgtfy.com/?q=Python3+Cheat+Sheet)



# Hello World!<!-- .element: class="dark shadow higher" -->
<!-- .slide: data-background-image="imgs/02/photo-1461770354136-8f58567b617a.jpeg" -->



## Konsole
* Navigation
* Basiskommandos (cd, cd .., mkdir, man)
* [Linuxtage Merkzettel für Fortgeschrittene](https://github.com/linuxtage/commands-cheatsheet/raw/master/cheatsheet.pdf)



## Lernziele
* Erstellen eines Programms
  * Arbeitsschritte, Tools
* Programmablauf steuern
  * Variablen, Datentypen
  * Kontrollstrukturen
  * Schleifen
* Programm strukturieren
  * Funktionen
  * Klassen



## Warum Python
* **Scriptsprache**
  * Abstrahiert komplexe Konzepte
  * Einfacher Einstieg
    * Texteditor, Programm & Konsole
  <!-- * Einfache Installation -->
  * Gute Dokumentation
  * Zwingt zu klarer Code-Struktur
  * Für alle grossen Plattformen verfügbar
  * sogar auf Micro-Controllern <!-- .element: class="fragment" data-fragment-index="5" --> → [µPython](https://micropython.org)



<!-- slide: data-background-image="imgs/pybv10-pinout.jpg" -->
![Micropython PyBoard](imgs/02/pybv10-pinout.jpg)<!-- .element: style="width:90%;z-index:200;" -->



# Demo<!-- .element: class="light shadow" -->
<!-- .slide: data-background-image="imgs/02/14116941824817ba1f28e78c8dff1.jpeg" -->


# Video<!-- .element: class="light" -->
<!-- .slide: data-background-iframe="https://www.youtube.com/embed/5LbgyDmRu9s" -->
[<i class="fa fa-youtube-square" aria-hidden="true"></i> go there](https://youtu.be/5LbgyDmRu9s)



## Aufbau eines Programms <!-- .slide: class="data-background" -->
```python
import sys

# Kommentar
#main() function
def main():
    # Hier startet die Abarbeitung
    return 0

# pythonic way um main zu definieren
if __name__ == "__main__":
    main()
```



## Syntax - Einrückung
```python
import sys

def main():
    a = 10
    b = 20
    print(a)
    print(b)

c = 30
print(c)

if __name__ == "__main__":
    main()
```
```bash
$ python3 test.py
30
10
20
```



## Einrückungsregeln - PEP8
[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

* 4 Spaces (Leerzeichen) pro Level bei Einrückung
* max. 79 Zeichen pro Zeile
* <!-- .element: class="fragment" data-fragment-index="1" -->
Im Detail studieren und für Übung beachten!
* <!-- .element: class="fragment" data-fragment-index="2" -->
 <i class="fa fa-exclamation-triangle fa-tugraz-color" aria-hidden="true"></i> Beispiele der Vorlesung halten sich nicht unbedingt an diese Vorgaben (Platzbedarf)




```python
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```



### Bestandteile von Programmen
#### Begriffe
**strukturierte** Programme bestehen aus verschiedenen Elementen:
* Variablen & Datentypen
* Operatoren
* Kontrollstrukturen
* Schleifen
* Funktionen, Signaturen & Parameter
* Eingabe-/Ausgabe Parameter



# Variablen & Datentypen



## Variablen & Datentypen
* **Variablen** sind Platzhalter
* **Datentypen** definieren wofür eine Variable Platz hält.
```python
kilometers = 42
car_name = "Volkswagen"
```

| Name       |    Typ |
| ---------- | ---:|
| kilometers | _natürliche Zahl_ mit Wert *42* |
| car_name   | _Text_ mit Wert *Volkswagen*    |


## Deklaration von Variablen
Variablen sind Platzhalter für Werte.

Zuweisung eines Werts heisst **deklarieren**.




## Variablen Namen
Namen sollen englisch, **kurz** und **eindeutig** sein, keine Leerzeichen und Sonderzeichen (außer '\_') enthalten.

Ausserdem sind folgende Worte in Pyhton **reserviert**:

<!-- ```python
import keyword
print(list(w for w in keyword.kwlist), end=" ")
``` //-->
```python
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
'with', 'yield']```


## Einfache Werte
```python
# Wahrheitswerte (Boolean)
var = True
# Natürliche Zahl (Integer)
var = 1234
# Reelle Zahl (Float)
var = 3.1415
# Text (String)
var = "Ein Text hat viele Zeichen"
# Kein Wert
var = None
```



## Sequenzielle Datentypen
```python
liste = [1, 2, 3] # Liste aus Integern
liste[0]

string = "Das ist ein Text" # String
string[1]
string[-2]
string

dic = {"element1": 5, "element2": 6}
dic["element1"]
```
```bash
>>>
1
'a'
'x'
'Das ist ein Text'
5
```



## Wahrheitswerte
| Datentyp | False-Wert |      |
| -------- | ---------- | ---- |
| bool     | False      |  Wahrheitswert False |
| int      | 0          |  numerisch Null |
| float    | 0.0        |  numerisch Null |
| str      | ""         |  leerer String |
| list     | []         |  leere Liste |
| dict     | {}         |  leeres Dictionary |



## Gültigkeit von Variablen (Scope)
```python
import sys

GLOBAL1 = 1

def main():
    a = 10
    print(a)
    print(GLOBAL1)

#print(a)
if __name__ == "__main__":
  main()
```
```bash
$ python3 scope.py
10
1
```


```python
import sys

GLOBAL1 = 1

def main():
    a = 10
    print(a)
    print(GLOBAL1)

print(a)
if __name__ == "__main__":
  main()
```
```bash
$ python3 scope.py
Traceback (most recent call last):
  File "scope.py", line 10, in <module>
    print(a)
NameError: name 'a' is not defined
```


## Operatoren
Operatoren definieren die Interaktion <br/> von Variablen und (deren) Werten

**a = 3, b = 4, c = 2**

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| +x, -x | -c | -2  |
| +, - | a + b | 7  |
| *, / | a * b, b / a | 12, 1.3333333  |
| //, %  | 13//3, 13 % 3   |  4, 1  |
| ** | a**c | 9  |


## Logische Operatoren
Boolsche Operatoren

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:|
| not | not True  | False  |
| or  | True or False | True  |
| and | True and False | False  |



## Komperatoren
| Komperator | Beispiel | Ausgabe |
| :----: | :----: | :----: |
| < |  1 < 2.1 | True |
| > |  1 > 1 | False |
| <= | 1 <= 1.0 | True |
| >= | 2 >= 3 | False |
| == | 2 == 2 | True |
| != | 2 != 2 | False |



## Division
```python
a = 9
b = 3
c = 10

print(c//b) # Ganzzahldivision
print(c/b) # Division (Datentyp wird angepasst: Ergebnis ist Float)
```
```bash
3
3.3333333333333335
```


## Division
```python
a = 9.0
b = 3.0
c = 10.0

print(a/b)
print(c/b)
```
```bash
3.0
3.3333333333
```



## Kontrollstrukturen
* Werden benötigt um den Ablauf eines Programms zu steuern
  * if
  * else
  * elif


### if else
```python
a = 10
b = 12

if (a > b):
  print("a > b")
else:
  print("b >= a!")
```
```bash
b >= a!
```
<!-- .element: class="fragment" data-fragment-index="1" -->


### if elif else
```python
a = 10
b = 2

if a < 10 and b > 0:
  print(a/b)
elif a > 10 or b > 2:
  print("a > b")
else:
  print("neither, ... ")
```
```bash
neither, ...
```
<!-- .element: class="fragment" data-fragment-index="1" -->


### if verschachtelt
```python
a = 10
b = 2

if a < 15:
  if b > 0:
    print("a = {}".format(a))
  else:
    print("b = {}".format(b))
else:
  print("a >= 15!")
```
```bash
a = 10
```
<!-- .element: class="fragment" data-fragment-index="1" -->


# Schleifen <!-- .element: class="light shadow lower" --> <!-- X -->
<!-- .slide: data-background-image="imgs/02/tiger-and-turtle-52691.jpg" --> <!-- X -->


## Schleifen
Ermöglichen mehrere Durchläufe von Codestellen
* while
  * solange bis ...
* for
  * durch iterierbare Objekte durchlaufen (zB Listen)


## while
```python
a = 1
while a < 10:
  a += 1 # same as: a = a + 1
  #print(a)
print(a)
```
```bash
10
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## while
kann mit __*continue*__ von oben fortgesetzt werden:
```python
a = 1
while a < 10:
  a += 1
  if not a % 2:
    print(a)
    continue
  a += 2
print(a)
```
```bash
2
6
10
10
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## while
kann mit __*break*__ abgebrochen werden:
```python
a = 1
while a < 10:
  if a > 3:
    break
  a += 1
print(a)
```
```bash
4
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## for
Schleife um durch iterierbare Objekte zu laufen
```python
ark = ["Camel", "Cat", "Dog", "Snake", "Cow"]

for animal in ark:
  print(animal)
```
```bash
Camel
Cat
Dog
Snake
Cow
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## for als Zählschleife
mit Hilfe der Funktion *range()*
```python
for count in range(0,5): # von 0, bis exklusive 5
  print(count)
```
```bash
0
1
2
3
4
```
<!-- .element: class="fragment" data-fragment-index="1" -->
```python
for count in range(0,5,2): # mit Schrittgröße 2
  print(count)
```
<!-- .element: class="fragment" data-fragment-index="2" -->
```bash
0
2
4
```
<!-- .element: class="fragment" data-fragment-index="3" -->



### Definition eines guten Programms
* Funktionalität <!-- .element: class="fragment" data-fragment-index="1" -->
* Lesbarkeit <!-- .element: class="fragment" data-fragment-index="2" -->
* Wartbarkeit <!-- .element: class="fragment" data-fragment-index="3" -->
* Robustheit <!-- .element: class="fragment" data-fragment-index="4" -->
* Korrektheit <!-- .element: class="fragment" data-fragment-index="5" -->
* Effizienz <!-- .element: class="fragment" data-fragment-index="6" -->
* Portierbarkeit <!-- .element: class="fragment" data-fragment-index="7" -->



# Funktionen


## Funktionen
dienen der Kapselung von Code nach logischen Einheiten
```python
pets = ["Hamster", "Cat", "Dog", "Canary"]

def not_a_dog_person(animal):
  return animal.replace("Dog", "Fish")

for pet in pets:
  print("Tom: {:10} Tim: {}".format(pet, not_a_dog_person(pet)))
```
```bash
Tom: Hamster    Tim: Hamster
Tom: Cat        Tim: Cat
Tom: Dog        Tim: Fish
Tom: Canary     Tim: Canary
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## Funktionen
```python
def add(x, y):
    return x + y

def print_result(result):
    print("Result: {}".format(result))

def main():
    a = 10
    b = 20
    c = add(a, b)
    print_result(c)

if __name__ == "__main__":
    main()
```
```bash
Result: 30
```
<!-- .element: class="fragment" data-fragment-index="1" -->



# Fragen? <!-- .element: class="dark shadow" -->
