# 706.088 Informatik 1
## Geschichte & Binäre Operationen


## Wiederholung Programmierung


## Deklaration von Variablen
* Boolsche Werte (True, False)
* Natürliche Zahlen (integer: 1, 11, 100000)
* Reelle Zahlen (float: 0.1, 3.7)
* Text (string: "Kette von Zeichen")
* Kein Wert (None)
* Tupel
* Listen
* Dictionary



## Operatoren

Operatoren definieren die Interaktion <br/> von Variablen und (deren) Werten

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| +x, -x | -2 | -2  |
| +, - | 3 + 4 | 7  |
| *, / | 3 * 4 | 12  |


## Operatoren

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| //, %  | 13//3, 13 % 3   |  4,1  |
| ** | 3**2 | 9  |


## Operatoren

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| not | not True | False  |
| and, or | True or False, True and False  | True, False  |
| <, <=, >=, >, == |  4 > 5  | False |


## Operatoren

Zuweisung

| Operator | Beispiel | Ausgabe |
|  ----    | -----    |  -----:  |
| =  |   a = 4, b = a |  a = 4, b = 4 |
| += |  a += b |  a = 8, b = 4 |
| -= |  a -= b |  a = 4, b = 4 |
| *= |  a *= 3 |  a = 12, b = 4 |
| /= |  a /= b |  a = 3.0, b = 4 |
| //= |  b //= a |  a = 3.0, b = 1.0 |



## Kontrollstrukturen
```python
if True:
  print("always here")
else:
  print("never here")
```
```bash
always here
```



## Schleifen
```python
print("forever")
while True:
    print("and ever")
```
```bash
forever
and ever
and ever
and ever
...
```


## Schleifen
```python
list = ["test1", "test2", "test3"]
for element in list:
    print(element)
```
```bash
test1
test2
test3
```


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



# Geschichte der Informatik


## Was ist Informatik
Wissenschaft der ** " systematischen " ** oder " ** automatischen Verarbeitung ** " von " ** Information ** "

**Infor**mation + Auto**matik**


## Geschichte der Informatik
* Aus 3 Teilgebieten zusammengesetzt
  1. Mathematik
  2. Mechanik
  3. Elektronik
* ... oder vom Abakus zum Quantencomputer


## Geschichte der Informatik
'Logische Maschinen' bereits im 13. Jahrhundert

Wunsch der Automation von mathematischen Berechnungen

Erstes **mechanisches** Rechengerät wurde im Jahr 1623 von Wilhelm Schickard gebaut



### Mathematik, Mechanik und Informatik
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Schickardmaschine.jpg#/media/File:Schickardmaschine.jpg"><img src="imgs/03/Schickardmaschine.jpg" alt="Schickardmaschine.jpg"></a><br/>Schickard'sche Rechenmaschine (1623 n. Chr)
<br/>By <a href="https://de.wikipedia.org/wiki/User:Klaeren" class="extiw" title="de:User:Klaeren">Herbert Klaeren</a> - Transferred from <a class="external autonumber" href="http://de.wikipedia.org/w/index.php?title=Datei:Schickardmaschine.jpg">[1]</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=8159979">Link</a></p>



### Schickard'sche Rechenmaschine

* 1623 n. Chr
* Basierend auf Zahnräderen
* Addition und Subtraktion von bis zu **sechsstelligen** Zahlen
* Speicherüberlauf
  * Akustisches Signal
* Pläne bis 1960 verloren



### Blaise Pascal - Pascaline
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Arts_et_Metiers_Pascaline_dsc03869.jpg#/media/File:Arts_et_Metiers_Pascaline_dsc03869.jpg"><img src="imgs/03/1200px-Arts_et_Metiers_Pascaline_dsc03869.jpg" alt="Arts et Metiers Pascaline dsc03869.jpg"></a><br>Pascaline<br/>By © 2005 <a href="//commons.wikimedia.org/wiki/User:David.Monniaux" title="User:David.Monniaux">David Monniaux</a>&nbsp;/&nbsp;, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=186079">Link</a></p>


* Erster (mechanischer) Taschenrechner
* 50 Prototypen
* Öffentliche Präsentation 1645
* Funktionsumfang
  * Addition
  * Subtraktion
  * von 2 Zahlen



## Mathematik, Mechanik und Informatik
* Charles Babbage (1791 - 1871)
  * Mathematiker, Philosoph, Erfinder und Entwickler.
  * “Einer der Väter des (mechan ischen) Computers”
  * Bekannt für die Babbage- oder Difference-Engine zur Lösung polinomialer Gleichungen.


<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:AnalyticalMachine_Babbage_London.jpg#/media/File:AnalyticalMachine_Babbage_London.jpg"><img alt="AnalyticalMachine Babbage London.jpg" src="imgs/03/AnalyticalMachine_Babbage_London.jpg"></a><br>
Analytical Machine von Babbage<br/>
Von Bruno Barral (ByB), <a title="Creative Commons Attribution-Share Alike 2.5" href="http://creativecommons.org/licenses/by-sa/2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=6839854">https://commons.wikimedia.org/w/index.php?curid=6839854</a></p>
<!-- ![Analytical Machine](https://upload.wikimedia.org/wikipedia/commons/a/ac/AnalyticalMachine_Babbage_London.jpg) -->



## Mathematik, Mechanik und Informatik
* Herman Hollerith (1860 - 1929)
  * Erfand das Lochkartensystem zur Datenspeicherung (1884)
  * Automatische Auswertung der gespeicherten Daten durch 'Lochkarten-Leser'
  * Ebnete den Weg zur Speicherung von ersten Computer-Instruktionen.
  * Verwendung der Hollerith Maschine (Tabulating machine
) zur Volkszählung 1890 in den USA


<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:Hollerith_Punched_Card.jpg#/media/File:Hollerith_Punched_Card.jpg"><img alt="Hollerith Punched Card.jpg" src="imgs/03/Hollerith_Punched_Card.jpg" height="287" width="640"></a><br/>
Lochkarte <br/>
By <span lang="en">Unknown</span><a href="//www.wikidata.org/wiki/Q4233718" title="wikidata:Q4233718"></a> - Library of Congress <a rel="nofollow" class="external free" href="http://memory.loc.gov/mss/mcc/023/0008.jpg">http://memory.loc.gov/mss/mcc/023/0008.jpg</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=30538485">https://commons.wikimedia.org/w/index.php?curid=30538485</a></p>



## <!-- .element: class="light shadow" -->
<!-- .slide: data-background-image="imgs/03/casey-horner-339978.jpg"-->


## Relais
* Mechanischer Schalter
  * Probleme:
    * Umschalten dauert einige Sekundenbruchteile
    * Benötigt viel Platz
    * Taktfrequenz sehr beschränkt
    * Mechanische Abnutzung


## Relais
<p class=wikipedia style="text-align:left;position: relative;left:-5%;"><a href="https://commons.wikimedia.org/wiki/File:Relais_Animation.gif#/media/File:Relais_Animation.gif"><img alt="Relais Animation.gif" src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Relais_Animation.gif"></a><br>Von <a href="https://de.wikipedia.org/wiki/User:Quark48" class="extiw" title="de:User:Quark48">Stefan Riepl</a> in der <a href="https://de.wikipedia.org/wiki/" class="extiw" title="de:">Wikipedia auf Deutsch</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a title="Creative Commons Attribution-Share Alike 2.0 de" href="http://creativecommons.org/licenses/by-sa/2.0/de/deed.en">CC BY-SA 2.0 de</a>, <br/> <a href="https://commons.wikimedia.org/w/index.php?curid=10663175">https://commons.wikimedia.org/w/index.php?curid=10663175</a></p>
<p style="text-align: right; position: absolute; left: 60%; width: 40%; top: 35%;">
Spule wird unter Strom gesetzt,
Magnetfeld zieht Anker,
Arbeitskontakte werden geschlossen,
Strom kann fließen
</p>


## Konrad Zuse (1910 - 1995)
Entwickelte den **ersten** **Digital**-rechner weltweit, <br/>die **Z3** (1941)

* 600 Relais für den Prozessor
* 1600 Relais für den Speicher
* Basierte auf **binärer Gleitkommaarithmetik**
* So groß wie ein (sehr großer) Kleiderschrank
* 15-20 Arithmetische Operationen / Sekunde
Weitere Informationen zu Konrad Zuse: http://zuse.zib.de


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Z3_Deutsches_Museum.JPG#/media/File:Z3_Deutsches_Museum.JPG"><img alt="Z3 Deutsches Museum.JPG" src="imgs/03/Z3_Deutsches_Museum.JPG" ></a><br>
Z3 im Deutschen Museum<br/>Von <a href="https://de.wikipedia.org/wiki/User:Venusianer" class="extiw" title="de:User:Venusianer">Venusianer</a> aus der <a href="https://de.wikipedia.org/wiki/" class="extiw" title="de:">deutschsprachigen Wikipedia</a>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3632073">https://commons.wikimedia.org/w/index.php?curid=3632073</a></p>


## First Bug
<i class="twa twa-bug twa-3x"></i>

* Bezeichnung 'Bug' für Fehler in Programmabläufen geht zurück auf Computer Pionierin **Grace Hopper**
* Am 9. September 1947 dokumentierte sie eine Motte in einem Relais des Computers **Mark II Aiken Relay Calculator** im Log-Buch mit den Worten: **"First actual case of bug being found**"


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:H96566k.jpg#/media/File:H96566k.jpg"><img alt="H96566k.jpg" src="imgs/03/H96566k.jpg"></a><br>By Courtesy of the Naval Surface Warfare Center, Dahlgren, VA., 1988. - U.S. Naval Historical Center Online Library Photograph <a rel="nofollow" class="external text" href="http://www.history.navy.mil/photos/images/h96000/h96566kc.htm">NH 96566-KN</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=165211">https://commons.wikimedia.org/w/index.php?curid=165211</a><br/>
 </p>


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Commodore_Grace_M._Hopper,_USN_(covered).jpg#/media/File:Commodore_Grace_M._Hopper,_USN_(covered).jpg"><img alt="Commodore Grace M. Hopper, USN (covered).jpg" src="imgs/03/Commodore_Grace_M._Hopper,_USN_(covered).jpg" height="900" width="720"></a><br>Grace Hopper, By James S. Davis - Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=12421475">https://commons.wikimedia.org/w/index.php?curid=12421475</a>
<br/>
Grace Hopper "Queen of Software" [on Letterman <i class="fa fa-youtube-square" aria-hidden="true"></i>](https://youtu.be/1-vcErOPofQ) </p>



# Elektronenröhre<!-- .element: class="dark shadow" -->
<!-- .slide: data-background-image="imgs/03/valve-840091.jpg"-->


## Elektronenröhre
* ist auch Schalter
* 1000 mal schneller als Relais
* Probleme:
  * benötigt viel Strom
  * Lebensdauer gering
  * Programmierer für ENIAC waren eher Mechaniker


## Elektronenröhre
<p class=wikipedia  style="text-align:left;position: relative;left:0em;"><a href="https://commons.wikimedia.org/wiki/File:Triode-dt-text.svg#/media/File:Triode-dt-text.svg"><img alt="Triode-dt-text.svg" src="imgs/03/Triode-dt-text.svg"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:Svjo&amp;action=edit&amp;redlink=1" class="new" title="User:Svjo (page does not exist)">Svjo</a>; German translation: Wdwd - <a href="//commons.wikimedia.org/wiki/File:Triode-english-text.svg" title="File:Triode-english-text.svg">File:Triode-english-text.svg</a>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=50578519">https://commons.wikimedia.org/w/index.php?curid=50578519</a></p>
<div style="text-align: left; position: absolute; left: 50%; width: 50%; top: 20%;">
Stromführende Kathode, Stromaufnehmende Anode, Spannungsgefälle:
Elektronen wandern von Kathode zu Anode, Strom fließt.
Ist Gitter unter Strom werden Elektronen abgestoßen, Stromfluss stoppt.
</div>


## ENIAC
Erster 'rein elektronischer' Rechner
* 1946 vorgestellt
* Elektronenröhren (Vacuum Tubes) zur elektrischen Speicherung von Zahlen
* 17.468 Elektronenröhren
* 167 m²
* 27 Tonnen
* 170 kW
* USD 468.000 ~ heute USD 6.8 Mio


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Eniac.jpg#/media/File:Eniac.jpg"><img alt="Eniac.jpg" src="imgs/03/Eniac.jpg"></a><br>Eniac</br>Von <span xml:lang="de" lang="de">Unbekannt</span><a href="//www.wikidata.org/wiki/Q4233718" title="wikidata:Q4233718"></a> - <a rel="nofollow" class="external text" href="http://ftp.arl.mil/ftp/historic-computers">U.S. Army Photo</a>, Gemeinfrei, <a href="https://commons.wikimedia.org/w/index.php?curid=55124">https://commons.wikimedia.org/w/index.php?curid=55124</a></p>


### Langlebigkeit von Elektronenröhren
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Elektronenroehren-auswahl.jpg#/media/File:Elektronenroehren-auswahl.jpg"><img src="imgs/03/1200px-Elektronenroehren-auswahl.jpg" alt="Elektronenroehren-auswahl.jpg"></a><br>By Stefan Riepl (<a href="https://de.wikipedia.org/wiki/Benutzer:Quark48" class="extiw" title="de:Benutzer:Quark48">Quark48</a>) - <span class="int-own-work">Self-photographed</span>, <a href="http://creativecommons.org/licenses/by-sa/2.0/de/deed.en" title="Creative Commons Attribution-Share Alike 2.0 de">CC BY-SA 2.0 de</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=14682022">Link</a></p>Ca. alle zwei Tage kam es zu einem Ausfall einer Elektronenröhre

15 Minuten bis fehlerhafte Elektronenröhre gefunden wurde



## Transistor
Shockley, Bardeen und Brattain (Bell Labs) <br/> entdecken 1947 den ersten Transistoreffekt <br/> und stellen den ersten **Transistor** vor.
* 1956 Nobelpreis für Physik


## Transistor
![Bipolar Transistor](imgs/03/transistor-39875.svg)<!-- .element: style="position:absolute; height:9em; float: right; top: 10%; right: -0%;" -->
* Kleiner Strom zwischen **B** asis und **E** mitter <br/>
schaltet großen Strom zwischen <br/> **C** ollektor und Emitter
* Basis ist im Sperrbetrieb
  * kein Strom fließt
  * Kollektor wartet auf Strom
* Wenn Spannung an Basis anliegt schaltet der Transistor
  * Strom fließt zwischen Collector und Emitter
  * Transistor leitet


## Transistor
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Transistor_animation.gif#/media/File:Transistor_animation.gif"><img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Transistor_animation.gif" alt="Transistor animation.gif"></a><br>Von Stefan Riepl (<a href="https://de.wikipedia.org/wiki/Benutzer:Quark48" class="extiw" title="de:Benutzer:Quark48">Quark48</a> 21:02, 2. Dez. 2007 (CET)) - <span class="int-own-work" lang="de">Eigenes Werk</span> (<span lang="de">Originaltext: selbst erstellt</span>), <a href="http://creativecommons.org/licenses/by-sa/2.0/de/deed.en" title="Creative Commons Attribution-Share Alike 2.0 de">CC BY-SA 2.0 de</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=12557861">Link</a></p>


Rechenleistung bis ca. 1960
* 1-2 KByte Speicher
* 0.02 MIPS

Rechenleistung 1986 bis heute
* 8 MByte - ~ 32GByte
* \> 100 MIPS


## Mailüfterl
* 1955 an der TU Wien von Heinz Zemanek mit Studierenden gebaut.
* erster Volltransistor Rechner am Europäischen Festland
* 3.000 Transistoren, 5.000 Dioden, 20 km Draht, 132 kHz
* Transistorspende von Philips
* erste Berechnung 1958


# Mailüfterl<!-- .element: class="light shadow" -->
<!-- .slide: data-background-iframe="https://www.youtube.com/embed/lvaiEW-Sm4A" -->
[<i class="fa fa-youtube-square" aria-hidden="true"></i> go there](https://www.youtube.com/watch?v=lvaiEW-Sm4A)


## Moore's Law
* Anzahl der Transistoren verdoppelt sich in regelmäßigen Abständen (alle 2 Jahre).
→ Leistung in [MIPS](https://en.wikipedia.org/wiki/Instructions_per_second#MIPS) verdoppelt sich auch.


### Moore's Law
<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:Transistor_Count_and_Moore%27s_Law_-_2011.svg#/media/File:Transistor_Count_and_Moore%27s_Law_-_2011.svg"><img alt="Transistor Count and Moore's Law - 2011.svg" src="https://upload.wikimedia.org/wikipedia/commons/0/00/Transistor_Count_and_Moore%27s_Law_-_2011.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/User:Wgsimon" title="User:Wgsimon">Wgsimon</a> - <span class="int-own-work" lang="en">Own work</span>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=15193542">https://commons.wikimedia.org/w/index.php?curid=15193542</a></p>



# Zahlensysteme<!-- .element: class="light shadow lower" -->
<!-- .slide: data-background-image="imgs/03/zahlensysteme_symbolbild.jpg"-->


## Dezimal
* **Dezimal**-system: Basis 10 (std. Integer)

| Ziffern | Präfix |
|:-:|:-:|
| 0-9    |  "" (keiner)      |

```python
>>> i = 123
>>> i
123
>>> f = int("99")
>>> f
99
>>>
```


## Hex
* **Hexadezimal**-system: Basis 16

| Ziffern | Präfix |
|:-:|:-:|
| 0-9, A-F   | "0x"       |

```python
>>> h = 0xA
>>> h
10
>>> h2 = 0xFF
>>> h2
255
```


## Oktal
* **Oktal**-system: Basis 8

| Ziffern | Präfix |
|:-:|:-:|
| 0-7    | "0o" (Null-O)  |

```python
>>> o = 0o7
>>> o
7
>>> o2 = 0o144
>>> o2
100
```


## Binär
* **Binär**-system oder **Dual**-system: Basis 2

| Ziffern | Präfix |
|:-:|:-:|
| 0,1    | "0b"  |

```python
>>> b = 0b101
>>> b
5
>>> b2 = 0b111111
>>> b2
63
```


## Binärsystem
* Basis für Computer
* Reduktion auf 2 Zustände
  * 0: kein Strom, Spannung
  * 1: Strom, Spannung


## Binärsystem
* Einzelne Stelle heisst: Bit (**BI**nary digi**T**)
* rechteste Stelle: Least Significant Bit (LSB)
* linkeste Stelle: Most Significant Bit (MSB)


## Binärsystem
```python
# Dezimal
i = 1*10**3 + 8*10**2 + 1*10**1 + 1*10**0 # 1811

# Binär
b = 1*2**3 + 1*2**2 + 0*2**1 + 1*2**0 # 13
```


## Binärsystem Umrechnung (n=2)
* x(10) → x(n):
  * x/n ⇒ y, Rest z
  * z an Stelle 0
  * y ⇒ x wenn y != 0
  * von Vorne für Stelle 1, 2, …
  * wenn y = 0 fertig.


## Binärsystem Umrechnung
25(10) → binär:
  * 25/2 ⇒ 12, Rest 1
  * 1 an Stelle 0 (LSB)
  * 12/2 ⇒ 6, Rest 0
  * 0 an Stelle 1
  * 6/2 ⇒ 3, Rest 0
  * 0 an Stelle 2
  * …


  * 3/2 ⇒ 1, Rest 1
  * 1 an Stelle 3
  * 1/2 ⇒ 0, Rest 1
  * 1 an Stelle 4
  * fertig: 11001



## Rechnen im Binärsystem
Grundregeln für Addition:

|||
|---|---|
| 0 + 0 | = 0 |
| 0 + 1 | = 1 |
| 1 + 0 | = 1 |
| 1 + 1 | = 0 (1 Übertrag) |
| 1 + 1 + 1 | = 1 (1 Übertrag) |


## Binäre Addition
|+||
|---|---|
| 0101101 | = 45 |
| 0110110 | = 54 |
| 1111    | = Übertrag |
| 1100011 | = 99 |


## Binäre Subtraktion
Computer führt Subtraktion auf Addition zurück:
möglich durch Zweier-Komplementbildung
* Darstellung von negativen Zahlen:
  * MSB trägt Information über Vorzeichen
* Limit an darstellbaren Zahlen:
  * `s`: verfügbare Bits
  * Kleinste darstellbare Zahl: `-2**(s-1)`
  * Größte darstellbare Zahl: `2**(s-1)-1`


## Positive und Negative Binärzahlen<!-- .slide: style="font-size:0.9em" -->
| bin | dec | bin  | dec |
|---|:-:|---|:-:|
| 0000 | 0  | 1000 | -8  |
| 0001 | 1  | 1001 | -7  |
| 0010 | 2  | 1010 | -6  |
| 0011 | 3  | 1011 | -5  |
| 0100 | 4  | 1100 | -4  |
| 0101 | 5  | 1101 | -3  |
| 0110 | 6  | 1110 | -2  |
| 0111 | 7  | 1111 | -1  |


## Zweier-Komplementbildung
* ist MSB 1, ist die Zahl negativ
* Schritt 1: alle Bits invertieren
* Schritt 2: zum Schluss 1 addieren

| 5(10) → -5 | 0101(2) | -5(10) → 5  | 1011(2) |
|---|:-|---|:-|
| Schritt 1: invertieren | 1010  |  |  0100  |
| Schritt 2: +1          | 1011  |  |  0101  |


## Subtraktion
Entspricht einer Addition mit dem Zweier-Komplement
* Was geschieht mit Überläufen?
  * werden verworfen

| 6(10) - 2(10) |→| 6(10) + -2(10) |
|---|-:|---|
| 6(10) | 0110 | |
| -2(10)| 1110 | |
|       | 1 0100 | = 4 |


## Multiplikation
kann __manchmal__ durch Verschieben der Bits nach links
durchgeführt werden

* Multiplikation mit `2**n`:
(Shiften um n Bits)

| 3*2 |     | 20*8    |    |
|---|-:|---|-:|
| **3**        | 011  | **20**  |    010100  |
| **2** (2**1) |  10  | **8** (2**3)   |    001000  |
| **6**        | 110  | **160** | 010100000  |


## Ausnahmen Multiplikation
Bei Multiplikation mit Zahlen ungleich `2**n`

```
13(10) *   5(10)
1101   * 101

 1101
+ 0000
+  1101
1000001  = 65
```


## Division
kann __manchmal__ durch Verschieben der Bits nach rechts
durchgeführt werden

* Division mit `2**n`:
(Shiften um n Bits)

| 4//2 = 2 |     | 24//8 = 3    |    |
|---|-:|---|-:|
| **4**        | 100  | **24**       |     11000  |
| **2** (2**1) |  10  | **8** (2**3) |     01000  |
| **2**        |  10  | **3**        |        11  |


## Ausnahmen Division
Bei Division mit Zahlen ungleich `2**n`

```python
25(10) //   5(10)
   11001   // 101  = 101
   110               ^^^
  -101   >-----------/||
---------             ||
   110                ||
 +1010  Komplement    ||
 +   1                ||
---------             ||
  10001               ||
     10 >-------------/|
     101               |
    -101 >-------------/
---------
     101
   +1010  Komplement
   +   1
---------
   10000 ---> kein Rest
```
<!-- .element: style="font-size:0.42em" -->


## Limitierung der darstellbaren Zahlen
* Gängige Computer haben 32-bit oder 64-bit Architektur:
  * 32-bit: max positive Zahl `2**32 -1`
  * 64-bit: max positive Zahl `2**64 -1`
  * Python kann in Version 3 gut mit langen Zahlen umgehen.
  * Grundproblem bleibt generell für Computer bestehen.


```python
>>> i = 0b11111111111111111111111111111111
>>> i
4294967295
>>> i.bit_length()
32
>>> j = i+1
>>> j.bit_length()
33
>>> bin(j)
'0b100000000000000000000000000000000'
>>> i64 = 0b1111111111111111111111111111111111111111111111111111111111111111
>>> i64.bit_length()
64
>>> i64
18446744073709551615
```


## Umwandlung von 64-bit in 16-bit<!-- .slide: data-background-image="imgs/03/ariane5.gif"-->
* Ariane 5 Explosion [<i class="fa fa-info-circle" aria-hidden="true" title="Info"></i>](http://homepages.inf.ed.ac.uk/perdita/Book/ariane5rep.html) [<i class="fa fa-youtube-square" aria-hidden="true"></i>](https://www.youtube.com/watch?v=PK_yguLapgA)



# Bitoperatoren


## Bitoperatoren<!-- .slide: style="font-size:0.8em" -->
Operatoren für Binärdarstellung

| Operator    |  Zuweisung  |  Ergebnis  |
|  ---        |     ----    |   ----     |
| ~x          |              |  bitweises Komplement <br/> (Einerkomplement)  (= -x-1) |
| ~x+1        |              |  Zweierkomplement  (= -x)  |
| x & y       |   x &= y     |  bitweises UND (AND) |
| x &#124; y  |   x &#124;= y |  bitweises ODER (OR) |
| x ^ y       |   x ^= y      |  bitweises ausschließendes ODER (XOR) |
| x << n      |   x <<= n    |  shiften von x um n Bit nach links  |
| x >> n      |   x >>= n    |  shiften von x um n Bit nach rechts |


## Bitoperatoren
```python
>>> a = 0b1001
>>> b = 0b0110
>>> bin(a | b)
'0b1111'
>>> bin(a & b)
'0b0'
>>> bin(a ^ b)
'0b1111'
>>> bin(~a)
'-0b1010'
>>> bin(~a & b)
'0b110'
```


## Bitoperatoren
```python
>>> a = 0b1001
>>> b = 0b0110
>>> b >>= 1
>>> b
3
>>> bin(b)
'0b11'
>>> bin(a ^ b)
'0b1010'
>>> a << 2
36
>>> bin(a << 2)
'0b100100'
```


## Bitoperatoren in der Praxis
### Demo


# Fragen?
