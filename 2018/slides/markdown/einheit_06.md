# 706.088 Informatik 1


## Wiederholung
* Klassen
* Vererbung



## Klassen
```python
class Rectangle():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getArea(self):
        return self._x * self._y
```


## Vererbung
```python
class Square(Rectangle):
    def __init__(self,x):
        super().__init__(x, x)
    # alle Methoden und Eigenschaften der Basisklasse geerbt
    def getY(self):
        # print("there is no y")
        return self._x
```


## Klassenvariablen
```python
class Circle:
    # Eigenschaft wird von allen Instanzen geteilt
    pi = 3.141592653589793
    def __init__(self,r):
      # Eigenschaft einer einzelnen Instanz
      self._r = r
    def getArea(self):
        return self._r ** 2 * Circle.pi
```


## Klassenvariablen
```python
class Circle:
    # wird von allen Instanzen geteilt
    pi = 3.141592653589793
    circle_counter = 0
    def __init__(self,r):
        self._r = r
        Circle.circle_counter += 1
    def getArea(self):
        return self._r ** 2 * Circle.pi
    def __del__(self):
        Circle.circle_counter -= 1
        if Circle.circle_counter == 0:
            print("no more circles left")
```


## Module in Python

* helfen Programme aufzuteilen
* Programmcode kann wieder verwendet werden
* einzubinden über `import`
* externe Module/Bibliotheken können importiert werden


## Module in Python
* Bsp:
  * `math`
    * `sin()`,`cos()`,`log()`
    * `pi`, `e`
  * `os`
    * `listdir()`,`name`, `uname()`...
  * `datetime`
  * `random`


## PyPi
- [Python Package Index](https://pypi.python.org/pypi)
- [pip3](https://pip.pypa.io/en/stable/) install <package>


## Einbinden eigener Module
* Bsp:
  * Helfer Funktionen in `myfunctions.py`
  * `import myfunctions`
    * stellt Funktionen von `myfunctions.py` bereit

```python
# myfunctions.py
def helper(test):
    return test*100
```
```python
# myprogram.py
import myfunctions

print(myfunctions.helper(10))
```


## Einbinden eigener Module
```python
# myfunctions.py
def helper(test):
    return test*100
```
```python
# myprogram.py
import myfunctions as mf

print(mf.helper(10))
```


## Module zu Paketen zusammenfassen
* Ordner mit Paketnamen
* Ein File für jedes Modul

```txt
mypackage/
  __init__.py # optional
  myfunctions.py
  module2.py
  module3.py
```
```python
from mypackage import myfunctions
from mypackage import * # alles importieren, setzt __init__.py voraus
```
Siehe Doku [<i class="fa fa-info-circle" aria-hidden="true" title="Info"></i>](https://docs.python.org/3/tutorial/modules.html#packages)



# Fehler-behandlung in Python


## Fehlerbehandlung in Python
* Ausnahmebehandlung, engl: **Exception Handling**
* Vereinfacht Fehlerbehandlung durch speziellen Mechanismus
* Rückgabewerte von Funktionen können für ordentlichen Programmablauf verwendet werden
* Fehler können strukturiert behandelt werden


## Exception Handling
* Fehler 'wirft' eine _Exception_ (Objekt) nach 'oben', Funktion ist beendet.
* Übergeordnete Funktion kann:
  * fangen, fortfahren
  * fangen, weiterwerfen, Funktion ist beendet
  * lässt passieren, Funktion ist beendet


## Exception Objekt
Enthält Attribute und Methoden (Funktionen) zur Klassifizierung des Fehlers
```python
>>> e = Exception("My custom error")
>>> e.args
('My custom error',)
>>> e = Exception("My custom error","test", 1,2)
>>> e.args
('My custom error', 'test', 1, 2)
```


## Exception werfen
```python
>>> raise Exception("My Exception")
```
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
Exception: My Exception
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## Exception werfen
Nur BaseException und davon Abgeleitete dürfen geworfen werden
```python
>>> raise "test"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must derive from BaseException
```


## Eingebaute exceptions
* BaseException
* Exception (Basisklasse für Benutzer)
* SyntaxError
* NameError
* TypeError
* ImportError
* [...](https://docs.python.org/3.5/library/exceptions.html#exception-hierarchy)


## Exception Behandlung
* _try_ öffnet den Try-Block
* Exceptions aus dem Try-Block werden im Except-Block gefangen
* _except_ definiert welche Exceptions behandelt werden


## Exception fangen
```python
>>> open("/tmp/non_existing_file",'r')
```
```txt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/non_existing_file'
```
```python
try:
    open("/tmp/non_existing_file")
except OSError as e:
    print("Caught:", e)
```
<!-- .element: class="fragment" data-fragment-index="1" -->
```txt
Caught: [Errno 2] No such file or directory: '/tmp/non_existing_file'
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## try - except - else
```python
try:
    print("all good")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error!")
    raise
else:
    print("everything is fine")
```


## except - else
```python
try:
    print("all good")
    open("/tmp/non_existing_file")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error!")
    raise
else:
    print("everything is fine")

print("normal program flow")
```
```txt
all good
Don't know this error!
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/non_existing_file'
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## except - else
```python
try:
    print(a) # undefined!
    print("all good")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error")
    raise
else:
    print("everything is fine")

print("normal program flow")
```
```txt
Undefined vars found
normal program flow
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## except - else
```python
try:
    print("all good")
except NameError:
    print("Undefined vars found")
except:
    print("Don't know this error!")
    raise
else:
    print("everything is fine")

print("normal program flow")
```
```txt
all good
everything is fine
normal program flow
```
<!-- .element: class="fragment" data-fragment-index="1" -->


## finally
```python
try:
  open("/tmp/non_existing_file",'r')
except FileNotFoundError:
  print("file does not exist")
except:
  print("don't know this error")
  raise
finally:
  print("cleaning up")
```
```txt
file does not exist
cleaning up
```
<!-- .element: class="fragment" data-fragment-index="1" -->



## assert
* Setzt Bedingung, die, wenn falsch, zu einer Exception führt.
* Nur zur Entwicklung sinnvoll.
* Nur mit &#95;&#95;debug&#95;&#95;``` == True``` aktiv
* Wird mit ```python3 -O``` deaktiviert (&#95;&#95;debug&#95;&#95;``` = False```)


## assert
```python
a = [1,2]
a[0] = 17
assert a == [17,2]
```
```python
a[1] = a[1] + 3
assert a == [17,4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```
<!-- .element: class="fragment" data-fragment-index="1" -->



# Fragen?
