# 706.088 Informatik 1


### Tupel, Listen,...; String Slicing,...; List Comprehensions, lambda functions


# Wiederholung


* Geschichte:
  * Mechanische, Elektronische Rechenmaschinen


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Schickardmaschine.jpg#/media/File:Schickardmaschine.jpg"><img src="imgs/03/Schickardmaschine.jpg" alt="Schickardmaschine.jpg"></a><br/>Schickard'sche Rechenmaschine (1623 n. Chr)
<br/>By <a href="https://de.wikipedia.org/wiki/User:Klaeren" class="extiw" title="de:User:Klaeren">Herbert Klaeren</a> - Transferred from <a class="external autonumber" href="http://de.wikipedia.org/w/index.php?title=Datei:Schickardmaschine.jpg">[1]</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=8159979">Link</a></p>


<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:Hollerith_Punched_Card.jpg#/media/File:Hollerith_Punched_Card.jpg"><img alt="Hollerith Punched Card.jpg" src="imgs/03/Hollerith_Punched_Card.jpg" height="287" width="640"></a><br/>
Lochkarte <br/>
By <span lang="en">Unknown</span><a href="//www.wikidata.org/wiki/Q4233718" title="wikidata:Q4233718"></a> - Library of Congress <a rel="nofollow" class="external free" href="http://memory.loc.gov/mss/mcc/023/0008.jpg">http://memory.loc.gov/mss/mcc/023/0008.jpg</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=30538485">https://commons.wikimedia.org/w/index.php?curid=30538485</a></p>


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Z3_Deutsches_Museum.JPG#/media/File:Z3_Deutsches_Museum.JPG"><img alt="Z3 Deutsches Museum.JPG" src="imgs/03/Z3_Deutsches_Museum.JPG" ></a><br>
Z3 im Deutschen Museum<br/>Von <a href="https://de.wikipedia.org/wiki/User:Venusianer" class="extiw" title="de:User:Venusianer">Venusianer</a> aus der <a href="https://de.wikipedia.org/wiki/" class="extiw" title="de:">deutschsprachigen Wikipedia</a>, <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3632073">https://commons.wikimedia.org/w/index.php?curid=3632073</a></p>


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:H96566k.jpg#/media/File:H96566k.jpg"><img alt="H96566k.jpg" src="imgs/03/H96566k.jpg"></a><br>By Courtesy of the Naval Surface Warfare Center, Dahlgren, VA., 1988. - U.S. Naval Historical Center Online Library Photograph <a rel="nofollow" class="external text" href="http://www.history.navy.mil/photos/images/h96000/h96566kc.htm">NH 96566-KN</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=165211">https://commons.wikimedia.org/w/index.php?curid=165211</a><br/>
 </p>


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Eniac.jpg#/media/File:Eniac.jpg"><img alt="Eniac.jpg" src="imgs/03/Eniac.jpg"></a><br>Eniac</br>Von <span xml:lang="de" lang="de">Unbekannt</span><a href="//www.wikidata.org/wiki/Q4233718" title="wikidata:Q4233718"></a> - <a rel="nofollow" class="external text" href="http://ftp.arl.mil/ftp/historic-computers">U.S. Army Photo</a>, Gemeinfrei, <a href="https://commons.wikimedia.org/w/index.php?curid=55124">https://commons.wikimedia.org/w/index.php?curid=55124</a></p>


<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Mail%C3%BCfterl_Wien.jpg#/media/File:Mail%C3%BCfterl_Wien.jpg"><img src="imgs/04/1200px-Mail%C3%BCfterl_Wien.jpg" alt="Mailüfterl Wien.jpg"></a><br/>Mailüfterl, techn. Museum Wien;<br/>Von Dr. Bernd Gross - <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC-BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=46982699">Link</a></p>


# Zahlensysteme
Basis: 10, 2 (`0b`), 8 (`0o`), 16 (`0x`)

Python default: 10
```python
int(str(100),2)
```
```python
4
```
<!-- .element: class="fragment" data-fragment-index="1" -->


```txt
>>> help(int)
int(x=0) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no
arguments are given.  If x is a number, return x.__int__().  
For floating point numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a
string, bytes, or bytearray instance representing an integer
literal in the given base.  The literal can be preceded by
'+' or '-' and be surrounded by whitespace.  The base
defaults to 10. Valid bases are 0 and 2-36. Base 0 means to
interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
```


```python
int(str(0b100),0)
```
```python
4
```
<!-- .element: class="fragment" data-fragment-index="1" -->



## Bitoperatoren
```python
def ip_to_int(ip):
    '''converts classic IP representation to int IP'''
    ip_parts = []
    for element in ip.split('.'):
      ip_parts.append( int(element) )
    int_ip = ip_parts[0] << 24
    int_ip += ip_parts[1] << 16
    int_ip += ip_parts[2] << 8
    int_ip += ip_parts[3]
    return int_ip
```


```python
def convert_ip(ip):
    classic_ip = [None]*4
    classic_ip[0] = (ip & (255 << 24)) >> 24
    classic_ip[1] = (ip & (255 << 16)) >> 16
    classic_ip[2] = (ip & (255 << 8)) >> 8
    classic_ip[3] = (ip & (255))
    str_ip = []
    for element in classic_ip:
      str_ip.append( str(element) )
    return ".".join(str_ip)
```


```python
def is_same_subnet(ip1, ip2, sub=subnet_24):
    '''returns True if ip1 and ip2 are on the same subnet'''
    if (ip1 & sub) == (ip2 & sub):
        return True
    return False

def device_number(ip, sub=subnet_24):
    '''returns address of device on the subnet'''
    return ((ip & sub) ^ ip)
```


## Sequentielle Datentypen
`list, tuple, str, byte, bytearray`


# Listen
**`list`**: listet beliebige Instanzen; veränderlich


# Tupel
**`tuple`**: listet beliebige Instanzen; **unveränderlich**


# String
**`str`**: Text, Sequenz von Buchstaben,<br/>
auch Sonderzeichen; **unveränderlich**


# Bytes
**`bytes`**: Binärdaten, Sequenz von Bytes (8-Bit); **unveränderlich**


# Bytearray
**`bytearray`**: Binärdaten, Sequenz von Bytes (8-Bit); veränderlich


## Slicing
```python
s = "This is a test string"
s[0] # T
s[8] # a
s[0:3] # Thi
s[8:14] # a test
s[0:14:3] # Tss s
```


## Slicing
```python
s = "This is a test string"
s[-2] # n
s[-2:] # ng
s[-11::3] # tttn
s[:-5:] # This is a test s
```


## Slicing
```python
s = "This is a test string"
s[::-1] # gnirts tset a si sihT
s[:-5:-1] # gnir
s[-16::-1] # i sihT
s[-10::-2] # e  ish
s[-5:-12:-2] # t st
s[-13:12] # a te
```



## List Comprehensions

Erstellen einer neuen Liste, aus bestehender Liste, nach bestimmten Regeln.


## List Comprehensions
```python
my_list = [1,2,3,4,5,6,7,8,9]
[x**2 for x in my_list]
```
```python
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## List Comprehensions
```python
my_list = [1,2,3,4,5,6,7,8,9]
[x**2 for x in my_list if x % 2 == 0]
```
```python
[4, 16, 36, 64]
```
<!-- .element: class="fragment" data-fragment-index="1" -->


```python
def ip_to_int(ip):
    '''converts classic IP representation to int IP'''
    # ip_parts = []
    # for element in ip.split('.'):
    #   ip_parts.append(int(element))
    ip_parts = [int(x) for x in ip.split('.')]

    int_ip = ip_parts[0] << 24
    int_ip += ip_parts[1] << 16
    int_ip += ip_parts[2] << 8
    int_ip += ip_parts[3]
    return int_ip
```


```python
def convert_ip(ip):
    classic_ip = [None]*4
    classic_ip[0] = (ip & (255 << 24)) >> 24
    classic_ip[1] = (ip & (255 << 16)) >> 16
    classic_ip[2] = (ip & (255 << 8)) >> 8
    classic_ip[3] = (ip & (255))
    # str_ip = []
    # for element in classic_ip:
    #   str_ip.append( str(element) )
    str_ip = [str(x) for x in classic_ip]

    return ".".join(str_ip)
```


```python
my_list1 = ["A", "B", "C"]
my_list2 = ["D", "E", "F"]
[(a,b) for a in my_list1 for b in my_list2 ]
```
```python
[('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'D'),
 ('B', 'E'), ('B', 'F'), ('C', 'D'), ('C', 'E'),
 ('C', 'F')]
 ```
 <!-- .element: class="fragment" data-fragment-index="1" -->


```python
my_list1 = ["A", "B", "C"]
my_list2 = ["D", "E", "F"]
my_list3 = ["G", "H", "I"]
[(a,b,c) for a in my_list1 for b in my_list2 for c in my_list3]
```
```python
[('A', 'D', 'G'), ('A', 'D', 'H'), ('A', 'D', 'I'), ('A', 'E', 'G'),
 ('A', 'E', 'H'), ('A', 'E', 'I'), ('A', 'F', 'G'), ('A', 'F', 'H'),
 ('A', 'F', 'I'), ('B', 'D', 'G'), ('B', 'D', 'H'), ('B', 'D', 'I'),
 ('B', 'E', 'G'), ('B', 'E', 'H'), ('B', 'E', 'I'), ('B', 'F', 'G'),
 ('B', 'F', 'H'), ('B', 'F', 'I'), ('C', 'D', 'G'), ('C', 'D', 'H'),
 ('C', 'D', 'I'), ('C', 'E', 'G'), ('C', 'E', 'H'), ('C', 'E', 'I'),
 ('C', 'F', 'G'), ('C', 'F', 'H'), ('C', 'F', 'I')]
 ```
 <!-- .element: class="fragment" data-fragment-index="1" -->



<a href="bsp/04/poker.py"><i class="twa twa-heart-suit twa-2x"></i>
<i class="twa twa-spade-suit twa-2x"></i>
<i class="twa twa-diamond-suit twa-2x"></i>
<i class="twa twa-club-suit twa-2x"></i></a>



## Lambda Funktionen
### Anonyme Funktionen

- müssen nicht benannt werden
```python
lambda x: x**2
sq = lambda x: x**2
sq(3) # 9
(lambda x: x**2)(3) # 9
```


```python
def convert_ip(ip):
    classic_ip = [None]*4
    classic_ip[0] = (ip & (255 << 24)) >> 24
    classic_ip[1] = (ip & (255 << 16)) >> 16
    classic_ip[2] = (ip & (255 << 8)) >> 8
    classic_ip[3] = (ip & (255))

    # str_ip = [str(x) for x in classic_ip]
    str_ip = list( map(lambda x: str(x), classic_ip) )

    return ".".join(str_ip)
```


# Fragen?
