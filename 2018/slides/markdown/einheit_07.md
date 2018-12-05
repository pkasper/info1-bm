# 706.088 Informatik 1
### Das Internet


## Wiederholung

* Module in Python
* PyPi (`pip install`)
* `import myModule`
* Fehlerbehandlung: Exceptions


## Exception Objekt
* Enthält Attribute und Methoden (Funktionen) zur Klassifizierung des Fehlers
* Eigene Exceptions nur von `Exception` ableiten
```python
>>> e = Exception("My generic error")
>>> e.args
('My generic error',)
>>> class MyException(Exception):
...     """Custom Exception raised in special cases of..."""
...     pass
>>> e = MyException("very severe error in...")
>>> e.__doc__
'Custom Exception raised in special cases of...'
>>> e.args
('very severe error in...',)
```


## try - except - else - finally
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
finally:
    print("cleaning up - always")
```


## assert
* Setzt Bedingung, die, wenn falsch, zu einer Exception führt.
* Nur zur Entwicklung sinnvoll.
* Nur mit &#95;&#95;debug&#95;&#95;``` == True``` aktiv
* Wird mit ```python3 -O``` deaktiviert ( &#95;&#95;debug&#95;&#95; = False)



# Das Internet <!-- .slide: data-background-image="imgs/07/internet.svg" --><!-- .element: class="dark shadow" -->


## Geschichte des Internet

* 1851: erstes Telegraphenkabel zwischen Paris und London
* ~1866: Transatlantik-Kabel
* 1969: ARPANET erster Vorläufer des Internet
* 1971: **15 Knoten** sind an das ARPANET angeschlossen
* 1987: neues Backbone für das ARPANET (27.000 Knoten)


## ARPANET 1973
<p class='wikipedia'><a href="https://commons.wikimedia.org/wiki/File:Arpanet_map_1973.jpg#/media/File:Arpanet_map_1973.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Arpanet_map_1973.jpg" alt="Arpanet map 1973.jpg"></a><br>By ARPANET - ARPANET, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=54039329">Link</a></p>



## Protokoll Modelle
* Protokoll Modelle helfen die Protokolle des Internet zu strukturieren
* Sie sammeln die Protokolle, die verwendet werden um Daten zu übertragen
* Sie werden in Schichten eingeteilt und zugeordnet
* Wir sehen uns 2 Modelle genauer an:
  * OSI-Modell
  * DoD-Modell


## OSI-Modell<!-- .slide: style="font-size:.8em" -->
"Open Systems Interconnection Model"

| Layer Nr | Name | engl. Name |
| :---: |---|---|
| 1. | Bitübertragungsschicht | (Physical Layer) |
| 2. | Sicherungsschicht  | (Data Link Layer) |
| 3. | Vermittlungsschicht | (Network Layer) |
| 4. | Transportschicht  | (Transport Layer) |
| 5. | Sitzungsschicht  | (Session Layer) |
| 6. | Darstellungsschicht | (Presentation Layer) |
| 7. | Anwendungsschicht |(Application Layer) |


## OSI-Modell<!-- .slide: style="font-size:.8em" -->
* Layer 1: stellt physische Übertragung von Bits zur Verfügung (Kabel, Stecker, Hub)

<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:4_port_netgear_ethernet_hub.jpg#/media/File:4_port_netgear_ethernet_hub.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/4_port_netgear_ethernet_hub.jpg" alt="4 port netgear ethernet hub.jpg"></a><br>Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=422174">Link</a></p>


## OSI-Modell<!-- .slide: style="font-size:.8em" -->
* Layer 2: gewährleistet fehlerfreie Übertragung (IEEE 802.2, ARP, LLC, MAC, Switch, Bridge)

<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Gigabit_LAN_Netzwerk_Switch_(10581106056).jpg#/media/File:Gigabit_LAN_Netzwerk_Switch_(10581106056).jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Gigabit_LAN_Netzwerk_Switch_%2810581106056%29.jpg/1200px-Gigabit_LAN_Netzwerk_Switch_%2810581106056%29.jpg" alt="Gigabit LAN Netzwerk Switch (10581106056).jpg"></a><br>By <a rel="nofollow" class="external text" href="http://www.flickr.com/people/107086296@N08">Dirk Vorderstraße</a> - <a rel="nofollow" class="external text" href="http://www.flickr.com/photos/dirkvorderstrasse/10581106056/">Gigabit LAN Netzwerk Switch</a>, <a href="http://creativecommons.org/licenses/by/2.0" title="Creative Commons Attribution 2.0">CC BY 2.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=31872355">Link</a></p>


## OSI-Modell<!-- .slide: style="font-size:.8em" -->
* Layer 3: Weiterleitung von Datenpaketen (IP, Router, ICMP)
* beinhaltet Weg-Suche-Mechanismen zwischen Netzwerkknoten


## OSI-Modell<!-- .slide: style="font-size:.8em" -->
* Layer 4: Segmentierung der Daten, Stauvermeidung (TCP, UDP)
  * TCP (Transmission Control Protocol):
    * Fehler in der Datenübertragung werden erkannt
    * weit verbreitet, zuverlässig
  * UDP (User Datagram Protocol):
    * Verbindungsloses Protokoll
    * nur Adressierung keine Zustellgarantie
    * schnellere Übertragung, da kein Garantie-Overhead


## OSI-Layer-Modell

* Layer 5: Dient der Wiederaufnahme der Datenübertragung nach Ausfall der Verbindung
* Layer 6: Datenkomprimierung, Verschlüsselung
* Layer 7: Dienste und Anwedungen (Web, E-Mail, IRC, Jabber, etc.)
* Layer 1 & 2 und 5-7 werden in anderen Modellen zu einem Layer vereinfacht.


## DoD-Modell
auch bekannt als **"Internet protocol suite"**

| Nr  |   Name        |      engl. Name       |     OSI Layer       |
| -- |  --           |        ---              | :--: |
| 1 |  Netzzugriff    |   (Network access)   |   1,2   |
| 2 |  Internet   |   (Internet)   |   3   |
| 3 |  Transport   |   (Host-to-Host)   |   4   |
| 4 |  Anwendung    |   (Process)   |   5,6,7   |


## DoD-Modell
benannt nach dem "Department of Defense"
* Layer 1: löst das Problem der Datenübertragung: Kommunikation via zB Ethernet, WLAN (ARP, MAC)
* Layer 2: Netzwerkweite Adressierung (IPv4, IPv6, IPSec, ICMPv6)
* Layer 3: Verbindung 2er Prozesse auf verschiedenen Systemen (TCP, UDP)
* Layer 4: Definiert Aufbau der eigentlichen Nachricht (SMTP, HTTP, DNS, DHCP etc)


## Arten Pakete zu verschicken

* **verbingungslos**: keine Kontrolle über Zustellung (wie zB Brief)
* **bestätigen** aber verbindungslos: Kontrolle über Empfang (Einschreiben mit Rückschein)
* **verbindungsorientiert**: Kontrollinformation wird immer übertragen, auch wenn keine Daten geschickt werden (Pers. Gespräch, Gesichtsausdruck)
* UDP/TCP: **UDP**: schnell und verbindungslos; **TCP**: zuverlässige Übertragung von Daten


## Adressierung
### IPv4
* IPv4: 4 8-bit Blöcke (32bit), Schreibweise mit Punkt getrennt, dezimal
  * 127.0.0.1, 129.27.200.1
  * 2<sup>32</sup> Adressen = 4.294.967.296 Geräte
* Netze: A: 255.0.0.0/8; B: 255.255.0.0/16; </br> C: 255.255.255.0/24
* Private: z.B. 192.168.0.0/16; 10.0.0.0/8


## Adressierung
### IPv6
* IPv6: 8 16-bit Blöcke (128bit), Schreibweise mit Doppelpunkt getrennt in Hex
  * 2a00:1450:4001:813::200e, 2001:0db8:0000:0042:0000:8a2e:0370:7334
  * 2<sup>128</sup> Adressen = 3.4 * 10<sup>38</sup>
* kein Broadcast wie IPv4, aber Multicast


### IPv6
* führende Nullen können weggelassen werden, einmal können aufeinander folgende Null-Blöcke mit '::' abgekürzt werden
  * Bsp: 2001:0db8:0000:0000:0000:ff00:0042:8329 -> 2001:db8:0:0:0:ff00:42:8329 -> 2001:db8::ff00:42:8329
* Localhost: '**::1**'
* ICMPv6 und DNS ist für IPv6 besonders wichig


## Netzwerktopologien

<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:NetworkTopologies.svg#/media/File:NetworkTopologies.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/NetworkTopologies.svg/1200px-NetworkTopologies.svg.png" alt="NetworkTopologies.svg"></a><br>By <a href="//commons.wikimedia.org/wiki/File:NetworkTopologies.png" title="File:NetworkTopologies.png">NetworkTopologies.png</a>: Maksim
derivative work: <a href="//commons.wikimedia.org/wiki/User:Malyszkz" title="User:Malyszkz">Malyszkz</a> (<a href="//commons.wikimedia.org/wiki/User_talk:Malyszkz" title="User talk:Malyszkz"><span class="signature-talk">talk</span></a>) - <a href="//commons.wikimedia.org/wiki/File:NetworkTopologies.png" title="File:NetworkTopologies.png">NetworkTopologies.png</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=15006915">Link</a></p>


## Anwendungen im Internet
(via TCP/UDP)

* Das Web (HTTP): Port 80
  * Web mit TLS/SSL: Port 443
* E-Mail: TCP Port 25
* SSH: TCP Port 22
* FTP: TCP Port 20/21
* NTP: UDP Port 123
* DNS: UDP/TCP Port 53



## Web - (Theoretische) Vorläufer
* [Memex](https://en.wikipedia.org/wiki/Memex) (1945), in 'As we may think', von Vannevar Bush

![](imgs/07/memex.jpg)<!-- .element: style="height:10em" -->


## Web - (Theoretische) Vorläufer
* Hypertext, Hypermedia, [Project Xanadu](https://en.wikipedia.org/wiki/Project_Xanadu) (1963), von Ted Nelson

[![](imgs/07/xanadu.png)](http://also.kottke.org/misc/images/Screenshot%202014-06-05%2008.56.42.png)



## Web
* 1989/1990 Tim Berners-Lee präsentiert das WorldWideWeb (WWW)
* Die Idee ist es Dokumente eindeutig (URL) im Netz zu teilen und zwischen Inhalten linken zu können (Hyperlink)
* HyperText Transfer Protocol (HTTP) war das Resultat
* Veröffentlichung des ersten Web-Browsers und Web-Servers Dezember 1990


# [DEMO](http://info.cern.ch/hypertext/WWW/TheProject.html)


## Web - HTTP
```
GET /home.html HTTP/1.1
Host: www.example.org
```


## Web - HTTP
```
HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
```
```
<html>
  <head>
    <title>Example.org – The World Wide Web</title>
  </head>
  <body>
    <p>The World Wide Web, abbreviated as WWW and commonly known ...</p>
  </body>
</html>
```


## HTTP mit Python
* Server (nur als Development Server!):
```
$ python3 -m http.server 8000
```
* Client:
  * [requests](http://docs.python-requests.org/en/master/) Library
  * [urllib3](https://urllib3.readthedocs.io/en/latest/)
  * http.client


## HTTP mit Python
Requests Library
```python
>>> import requests
>>> r = requests.get('http://tugraz.at')
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=utf-8'
>>> r.headers['server']
'Apache'
>>> r.text[0:20]
'<!DOCTYPE html>\n<htm'
```


## Links im Web
```
<a href="http://www.example.org/home.html">Example.org Homepage</a>
```


## Links mit Python
HTML parsing
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'html.parser') # Request from before
for a in soup.find_all('a'):
    print(a.get('href','/'))
```


## Struktur des Web
[![](imgs/01/connectivity_of_the_web.jpg)](http://www9.org/w9cdrom/160/160.html)


## Hyper-G - Eine Konkurrenz aus Graz
* Ein Link im Web kann 'gebrochen' werden
  * Wenn eine Seite nicht mehr existiert
  * Wenn die Seite umzieht
* Lösung:
  * Links müssen von beiden Seiten akzeptiert werden
  * Problem: Grosser Ressourcenbedarf und Arbeitsaufwand


## Web Suche

**Problem**: Zu viel (auch falsche) Information. Man möchte Inhalte indizieren und verfügbar machen.
* Das Web ist wie eine Bibliothek ohne Index:
  * Wonach indiziert man?
    * Adresse?
    * Inhalt?
    * Beteiber?
    * Netzwerkstruktur!


## Page Rank
<p class="wikipedia"><a href="https://commons.wikimedia.org/wiki/File:PageRank-hi-res.png#/media/File:PageRank-hi-res.png"><img src="imgs/01/PageRank-hi-res.png" alt="PageRank-hi-res.png"></a><br><a href="http://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=2776582">https://commons.wikimedia.org/w/index.php?curid=2776582</a></p>


## DNS - Domain Name System
* übersetzt Domain Namen in IP Adressen
* Nameserver sind das 'Telefonbuch' des Internet
* UDP Port 53, teilweise unterstützt von TCP (bei grossen Anfragen)


## DNS - Domain Name System

```bash
$ dig A tugraz.at
---------8<--------
;; ANSWER SECTION:
tugraz.at.		3600	IN	A	129.27.2.244
;; AUTHORITY SECTION:
tugraz.at.		2081	IN	NS	ns2.tu-graz.ac.at.
tugraz.at.		2081	IN	NS	ns5.univie.ac.at.
tugraz.at.		2081	IN	NS	ns10.univie.ac.at.
tugraz.at.		2081	IN	NS	ns1.tu-graz.ac.at.
---------8<--------
;; Query time: 2 msec
;; SERVER: 129.27.2.3#53(129.27.2.3)
;; WHEN: Tue Jan 10 19:25:55 CET 2017
;; MSG SIZE  rcvd: 265
```


## DNS Record Types
* A: Haupteintrag IPv4
* AAAA: Haupteintrag IPv6
* CNAME: verweist auf anderen Namen
* MX: Mail Exchange, verweist auf den E-Mail Server
* NS: NameServer, Delegierung der Nameserver untereinander
* TXT: Textinformation (SPF, DMARC, …)
* SRV: Service Locator, Eintrag zu angebotenen Diensten (zB XMPP)


## DNS
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Dns-raum.svg#/media/File:Dns-raum.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Dns-raum.svg/1200px-Dns-raum.svg.png" alt="Dns-raum.svg"></a><br><a href="http://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=556580">Link</a></p>


## DNS Anfrage
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Dns-abfrage.svg#/media/File:Dns-abfrage.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Dns-abfrage.svg/1200px-Dns-abfrage.svg.png" alt="Dns-abfrage.svg"></a><br>Von <a href="//commons.wikimedia.org/w/index.php?title=User:Hank_van_Helvete&amp;action=edit&amp;redlink=1" class="new" title="User:Hank van Helvete (page does not exist)">Hank van Helvete</a> - <span class="int-own-work" xml:lang="de" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=556730">Link</a></p>


## E-Mail
* seit 1971 (erste E-Mail im ARPANET)
* hostbasiertes Nachrichtensystem
* E-Mail Adresse repräsentiert ein Postfach
  * user@host


## E-Mail
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Email.svg#/media/File:Email.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Email.svg/1200px-Email.svg.png" alt="Email.svg"></a><br>By <a href="https://en.wikipedia.org/wiki/User:Yzmo" class="extiw" title="en:User:Yzmo">Yzmo</a> at the <a href="https://en.wikipedia.org/wiki/" class="extiw" title="w:">English language Wikipedia</a>, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3052180">Link</a></p>


## FTP
File Transfer Protocol
* Protokoll zur Übertragung von Daten zu Servern.
* Meist für Webseiten genutzt.
* Unverschlüsselt <i class="fa fa-exclamation-triangle fa-tugraz-color" aria-hidden="true"></i>
* Port 20 (data port), Port 21 (command port)
* Verschieden Modi für Datenformate (ASCII, binary, …)


## SSH
Secure Shell, zB OpenSSH
* verschlüsselte Verbindung zum:
  * Ausführen von Kommandos (ssh)
  * Übertragen von Dateien (scp, rsync, SFTP)
  * Passwortlosen Login
  * Tunneln von Verbindungen (ssh -L, ssh -R)
  * Verbinden via SOCKS Proxy (ssh -D)
  * Einbinden des Filesystems (sshfs)


## Fragen?
