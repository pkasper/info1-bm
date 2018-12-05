# 706.088 Informatik 1


# Internet P2P

## Inhalt
* Internet Struktur
* Mesh Networking
* Client Server Modell
* Peer-to-Peer



## Wiederholung




## SSH
Secure Shell, zB OpenSSH
* verschlüsselte Verbindung zum:
  * Ausführen von Kommandos (ssh)
  * Übertragen von Dateien (scp, rsync, SFTP)
  * Passwortlosen Login
  * Tunneln von Verbindungen (ssh -L, ssh -R)
  * Verbinden via SOCKS Proxy (ssh -D)
  * Einbinden des Filesystems (sshfs)



## Routing
* Hubs/Switches nur im lokalen Netz (zB: 192.168.0.0/32)
* **Router** kommunizieren zwischen Netzwerken <br/>und **leiten weiter**
* kleine Netze: Routing per Hand (Statisches Routing)
* grosse Netze: komplex, häufige Änderungen (Dynamisches Routing)
* Routingtabellen: beinhalten die kürzesten Wege zu Zielknoten

<!-- ## Kürzeste Wege: Dijkstra
* Algorithmus zum Finden des kürzesten Weges //-->


## Automome Systeme
* Sind IP-Netze die als Einheit verwaltet werden.
* kann aus mehreren IP-Netzen bestehen, die intern geroutet werden
* AS haben eine 16-Bit AS-Nummer (65.536 mögliche AS)
  * derzeit ~55.000 vergeben, Erweiterung auf 32 Bit abgeschlossen
* AS Nummern und IPs werden in Europa von der [RIPE NCC](https://www.ripe.net/) vergeben.
  * AS1113: TU Graz


## Autonome Systeme
* **Kunden**: zahlen für Zugang und Routing (downstream)
* **Provider**: geben Zugang zu anderen AS
* **Peer**: gleich gestelltes AS mit dem kooperiert wird (Kostenteilung von Leitungen)
* Tier-1 Provider: ist selbst nicht Kunde, Tier-2 Provider: ist nur Kunde von Tier-1 Providern
* BGP (Border Gateway Protocol)


## Routing Methoden
* Statisch
  * Gewichtung der Verbindungen wird nicht verändert
* Dynamisch/Adaptiv
  * Ausfälle, Latenzen werden dynamisch berücksichtigt
* Zentral
  * Eine Zentrale berechnet kürzeste Wege
* Verteilt
  * Jeder Knoten evaluiert für sich selbst die beste Route


## Ad Hoc Netze
* topologiebasiert
  * logische Information über Verbindungen reicht aus
* Proaktiv (zB [OLSR](https://de.wikipedia.org/wiki/Optimized_Link_State_Routing))
  * bevor Daten übertragen werden stehen Routen fest
* Reaktiv (zB [AODV](https://de.wikipedia.org/wiki/Ad-hoc_On-demand_Distance_Vector))
  * Bestimmung der Pfade erst bei Nutzung
* Hybrid (zB [802.11s](https://de.wikipedia.org/wiki/IEEE_802.11s))
  * Kombination aus proaktiv und reaktiv


## Wireless Mesh Networking
* [802.11s](https://de.wikipedia.org/wiki/IEEE_802.11s), Verwendung zB:
  * [OLPC (One Laptop per Child)](https://de.wikipedia.org/wiki/OLPC_XO-1)
  * [Google WiFi](https://blog.google/products/google-wifi/introducing-new-kind-wi-fi-system/)

<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Freifunk_mesh_cloud.png#/media/File:Freifunk_mesh_cloud.png"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Freifunk_mesh_cloud.png" alt="Freifunk mesh cloud.png"></a><br>Von <span class="int-own-work" lang="de">Eigenes Werk</span>, <a href="http://creativecommons.org/licenses/by-sa/3.0/" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=1525096">Link</a></p>


## Funkfeuer - Freifunk
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Wireless_mesh_network_diagram.jpg#/media/File:Wireless_mesh_network_diagram.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Wireless_mesh_network_diagram.jpg" alt="Wireless mesh network diagram.jpg"></a><br>By David Johnson, Karel Matthee, Dare Sokoya, Lawrence Mboweni, Ajay Makan, and Henk Kotze (Wireless Africa, Meraka Institute, South Africa) - <a href="https://en.wikipedia.org/wiki/File:Building_a_Rural_Wireless_Mesh_Network_-_A_DIY_Guide_v0.8.pdf" class="extiw" title="en:File:Building a Rural Wireless Mesh Network - A DIY Guide v0.8.pdf">Building a Rural Wireless Mesh Network: A do-it-yourself guide to planning and building a Freifunk based mesh network</a>, <a href="http://creativecommons.org/licenses/by-sa/2.5" title="Creative Commons Attribution-Share Alike 2.5">CC BY-SA 2.5</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=30799980">Link</a></p>


## Mesh Netzwerk in Graz
* Freifunk und [Funkfeuer](https://graz.funkfeuer.at/) Mesh Netzwerk (in Graz)
* verwendet OLSR
* jeder kann teilnehmen
* funktioniert parallel zum Internet



## URI - URN - URL
* URI (Uniform Resource Identifier)
 * URN (Uniform Resource Name)
   * Definiert Resource anhand Nummer/Hash in Namespace
     * ISBN, Magnet Link, [Tel](https://www.rfc-editor.org/rfc/rfc3966.txt), [xmpp](https://www.ietf.org/rfc/rfc4622.txt)
 * URL (Uniform Resource Locator)
   * Definiert Datum anhand eines Protokolls und Pfades
     * https://www.tugraz.at/studium/studienangebot


## URL - URN
```
 foo://example.com:8042/over/there?name=ferret#nose
 \_/   \______________/\_________/ \_________/ \__/
  |           |            |            |        |
 scheme     authority     path        query   fragment
  |   _____________________|__
 / \ /                        \
 urn:example:animal:ferret:nose
 ```



## Client-Server-Modell
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Client-server-model.svg#/media/File:Client-server-model.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/1200px-Client-server-model.svg.png" alt="Client-server-model.svg"></a><br>By David Vignoni
<a href="//commons.wikimedia.org/wiki/File:Gnome-fs-server.svg" title="File:Gnome-fs-server.svg">Gnome-fs-server.svg</a>, <a href="http://www.gnu.org/licenses/lgpl.html" title="GNU Lesser General Public License">LGPL</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=15782858">Link</a></p>


## Client-Server-Modell
Standardmodell für Dienste im Internet
* **Client**: fordert Dienst mit Request an
* **Server**: stellt Dienst bereit
* **Dienst**: definierte Aufgabe die ein Server anbietet (Layer 7 OSI-Modell)
* **Request**: Anfrage des Client an den Server
* **Response**: Antwort des Servers an den Client


## Client-Server Dienste
* Das Web (HTTP): Port 80
  * Web mit TLS/SSL: Port 443
* E-Mail: TCP Port 25
* SSH: TCP Port 22
* FTP: TCP Port 20/21
* NTP: UDP Port 123
* DNS: UDP/TCP Port 53


## P2P
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:P2P-network.svg#/media/File:P2P-network.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/P2P-network.svg/1200px-P2P-network.svg.png" alt="P2P-network.svg"></a><br>Von <a href="//commons.wikimedia.org/wiki/User:Mauro_Bieg" title="User:Mauro Bieg">User:Mauro Bieg</a> - <span class="int-own-work" lang="de">Eigenes Werk</span>, Gemeinfrei, <a href="https://commons.wikimedia.org/w/index.php?curid=2551723">Link</a></p>


## P2P
Peer-to-Peer Modell
* gleich berechtigte Knoten
* kommunizieren untereinander
* keine zentrale Stelle


## P2P
* Verfügbarkeit einzelner Knoten kann nicht garantiert werden
* Ausfall einzelner Knoten wird toleriert
* Netzwerk ist selbstorganisierend
* Peers bieten Dienste an
* Peers nehmen Dienste anderer an
* Peers sind autonom (Freiwilligkeit)


## P2P Typen
* Zentral (Napster)
  * Eine zentrale Verwaltung wird benötigt
* reines P2P Netz (zB: Gnutella, [Freenet](https://de.wikipedia.org/wiki/Freenet))
* Hybrides P2P Netz (zB: Gnutella2)
  * einzelne Knoten bekommen Hub Status (Supernode)
* strukturiert (zB: Bittorrent)
* unstrukturiert (zB: Gnutella, KaZaA)


## P2P Anwendungen
* [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent), FileSharing (FS)
* [Bitcoin](https://de.wikipedia.org/wiki/Bitcoin), Geld
* [Ethereum](https://en.wikipedia.org/wiki/Ethereum), decentralized VM, smart contracts
* [GNUnet](https://en.wikipedia.org/wiki/GNUnet) ([F2F](https://en.wikipedia.org/wiki/Friend-to-friend)), Messaging, FS
* [BitMessage](https://en.wikipedia.org/wiki/Bitmessage), Messaging
* [RetroShare](https://en.wikipedia.org/wiki/RetroShare) (F2F), FS, IM, ...
* [Tox](https://en.wikipedia.org/wiki/Tox_(protocol), IM, video messaging
* [Coral Content Distribution Network](https://en.wikipedia.org/wiki/Coral_Content_Distribution_Network) †, [CoDeeN](https://en.wikipedia.org/wiki/CoDeeN) (CDN) †



## Bittorrent
* strukturiertes P2P Netz
* Tracker und `.torrent` Files
* DHT (Distributed Hash Table) gibt Struktur
  * Verteiltes Such-System, Ersatz für Tracker
* Dateien können in Teilen von mehreren Peers geladen werden
* Ports 6881-6889, TCP

<!--

## DHT
Distributed Hash Table
<p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:DHT_en.svg#/media/File:DHT_en.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/DHT_en.svg/1200px-DHT_en.svg.png" alt="DHT en.svg"></a><br>By Jnlin - Jnlin, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=1585652">Link</a></p>
-->


## Magnet Link
* Ersatz für `.torrent` Datei
* ist ein URI-Standard für Dateien
* `magnet:` als Namespace
* Hash als Query: eXact Topic (xt)
* Optionen: TRacker (tr), eXact Lenght in bytes (xl), Acceptable Source (as), Manifest Topic (mt), ...
  * <i class="fa fa-magnet fa-tugraz-color fa-rotate-180" aria-hidden="true"></i> [magnet:?xt=urn:btih:88594AAACBDE40E…](magnet:?xt=urn:btih:88594AAACBDE40EF3E2510C47374EC0AA396C08E)


## BitTorrent Einsatz
* Verteilen grosser Dateien zB:
  * Linuxdistributionsimages: Redhat, Novell, Debian etc.
  * OpenOffice, LibreOffice
* Facebook, Twitter setzen BT in ihren Rechenzentren ein
* Amazon S3 bietet BitTorrent als Downloadform
* Blizzard verteilte Spiele und Patches per BitTorrent
* Florida State University verteilt grosse wissenschaftliche Datensätze per BT



# Blockchain<!-- .element: class="light shadow" --><!-- .slide: data-background-image="imgs/09/chains.jpg" -->


## Blockchain
* Kerntechnologie hinter Kryptowährungen
* öffentliches Kontobuch
* [verteilte Datenbank](https://en.wikipedia.org/wiki/Blockchain_(database&#41;)
* jeder Full-Node hat komplette Blockchain (BC)
* Transaktionen werden veröffentlicht und in BC gespeichert
* jeder Knoten kann Transaktionen verifizieren


## Blockchain
* Transaktionen werden validiert und in Blöcke zusammengefasst
* jeder Block baut auf einem vorigen auf (Chain) und beinhalten (vereinfacht):
  * **Hash des vorigen Blocks**
  * Zeitstempel
  * Daten (Transaktionen)
* regelmäßig ein neuer Block
* keine zentrale Behörde notwendig!


## Blockchain & Bitcoin
<!-- <p class=wikipedia><a href="https://commons.wikimedia.org/wiki/File:Bitcoin_logo.svg#/media/File:Bitcoin_logo.svg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bitcoin_logo.svg/1200px-Bitcoin_logo.svg.png" alt="Bitcoin logo.svg"></a><br>By Bitboy - <a rel="nofollow" class="external text" href="http://forum.bitcoin.org/?topic=1756.0">Bitcoin forums</a>, <a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en" title="Creative Commons Zero, Public Domain Dedication">CC0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=15411063">Link</a></p> -->
* 2008 vorgestellt, Jänner 2009 erste Version
* Kryptowährung: dezentralisierte, digitale Währung
* Zeichen: (XBT, BTC, <i class="fa fa-bitcoin" aria-hidden="true"></i>)
* Open-source
* Bitcoin bezeichnet:
  * P2P Software
  * die Geldeinheit
  * das Netzwerk/Protokoll


## Bitcoin
* basiert auf Public-Private Keys
* 'permission less'
  * niemand muss um Erlaubnis gefragt werden
* Peers validieren Transaktionen
* pseudonymes Netzwerk
  * Adressen und **Transaktionen sind öffentlich**
  * Besitzer der Adressen sind nicht mit Namen vermerkt


## Double Spending Problem
doppeltes Ausgeben des selben Geldes
* **wird durch Blockchain verhindert**
* Transaktionen dürfen sich nicht widersprechen
* muss durch Transaktionen in der Blockchain genügend Reserven haben
* gültige Transaktionen haben als Input nur Output vorheriger Transaktionen


## Transaktionen
* Adresse A signiert eine Transaktion zu Adresse B
* Input A → Output B und C (C ist Wechselgeldadresse von User A)
* mehrere Inputs und Outputs möglich
* Wenn Input > Output, behält sich Miner den Rest (Transaction Fee)


## Miner
* validieren Transaktionen und packen sie in einen Block
* sie behalten sich die 'Transaction Fee' und bekommen einen fixen Betrag (dzt 12.5 BTC) pro Block
* Müssen einen 'Proof-of-Work' erbringen
  * Aufwendige Berechnung um eine Nummer (nonce) mit spezieller Eigenschaft zu finden
  * Eigenschaft in jedem Block anders


## Produktion / Limit
* jeder Block +12.5 BTC an Miner
* maximal 21 Mio
* alle 4 Jahre Blockbelohnung halbiert


## Wallet
* Software um Schlüssel zu verwalten und Überweisungen zu signieren
* muss nicht die Blockchain halten
  * verbindet sich meist zu Server
* Private Key ist Schlüssel zum Guthaben!


## Andere Blockchains
* [Ethereum](https://www.ethereum.org/)
  * verteilte programmierbare Plattform auf BC Basis
* Litecoin
  * erste alternative Kryptowährung (anderer Hash)
* Zcash
  * anonyme Kryptowährung (Sender, Empfänger, Betrag bleiben anonym)
* [Sia](http://sia.tech/)
  * verteilter Datenspeicher



# Praxis
## Blockchain Christmas Lights



## Fragen?

<!--
## Blockchain Christmas Lights
<!-- . element: class="light shadow" - -> <!-- . slide: data-background-image="imgs/09/lights.gif" - ->
//-->

<!--
## Prüfung
2019-01-23 20:00
//-->

<!--
## Frohe Feiertage
<i class="twa twa-candle twa-5x"></i><i class="twa twa-christmas-tree twa-5x"></i>
## und guten Rutsch!
<i class="twa twa-party-popper twa-5x"></i><i class="twa twa-fireworks twa-5x"></i>
//-->
