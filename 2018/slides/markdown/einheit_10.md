# 706.088 Informatik 1


# Daten Visualisieren mit Python

## Inhalt
* Motivation
* NumPy Wiederholung
* Von Daten zur Visualisierung
* Packages für Python3
 * Anhand von __Matplotlib__ und __Bokeh__
* Designüberlegungen beim Visualisieren
<div style='position:absolute; bottom:0; left:0%; opacity:0.15; width:100%'>![Example Graph](/imgs/10/graph_bg.png)</div>



## Motivation
Was ist Datenvisualisierung?
* Visuelle Representation von Daten
* Unterstützung von geschriebenen Argumenten


Warum visualisieren wir Daten?


Warum visualieren wir Daten?

<span style='color:red'>_“Never trust a diagram that you have not faked yourself.”_</span>
<span style='font-size:9pt'>(http://www.tylervigen.com/spurious-correlations)</span>


## Grundlagen
* Warum visualieren wir Daten?
 * Um etwas über die Daten zu lernen
 * Um Anderen die Ergebnisse und Daten kompakt zu präsentieren
 * Um ein Gefühl im Umgang mit visuellen Datenrepräsentationen zu bekommen



## <a href="https://www.numpy.org/">NumPy</a> Wiederholung
<div style='position:absolute; top:0; right: 0; width:30%; text-align:center; transform: translateY(-120%)'>![NumPy Logo](/imgs/10/logo_numpy.png)</div>

```python
import numpy as np
```

 "MATLAB in Python"
* Mathematische Funktionalitäten für Python
* Arrays und Matrizen
 * Elementweise Operationen
* Hoch performant
 * Unterbau in C und C++
* Ausführliche Dokumentation <a href="https://www.numpy.org/"><i class="fa fa-external-link"></i></a>


### NumPy Arrays
* Grundliegendes Konzept von Numpy
 * Sind als Vektoren anzusehen
 * Arrays haben einen fixen Datentyp (int, float, ...)
  * Komplexe array (mit dtype Object) sind möglich
 * Normale Operationen (`+`, `-`, `*`, ...) Elementweise
* Numpy arrays sind typischer Datentyp beim Plotten


### <a href="https://pandas.pydata.org/">Pandas</a>
<div style='position:absolute; top:0; right: 0; width:30%; text-align:center; transform: translateY(-50%)'>![Falling Pandabear](/imgs/10/falling_panda.jpg)</div>

```python
import pandas as pd
```

* Mächtiges Package auf NumPy aufbauend
* <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html">Dataframe</a> als grundliegender Datentyp
 * Simpel gesagt "Dictionary aus numpy arrays"
* Inkludiert sehr viel Funktionalität für Analyse großer Datenmengen
* Inkludiert Visualisierungstools (Auf Basis von Matplotlib)
 * Nur Basisfunktionalitäten simpel anwendbar
* Moderne Visualisierungspackages verwenden Dataframes als Input
* Kann direkt mit CSV (und anderen Dateitypen) umgehen



## Von Daten zur Visualisierung

<div style="display: inline-block; vertical-align: middle;"><iframe frameborder="0" src="bsp/10/data_table.html" style="width:35rem; height:26rem;"></iframe></div>
<i class="fa fa-arrow-circle-right fa-6" style="color: red"></i>
<div style="display: inline-block; vertical-align: middle;"><iframe frameborder="0" src="bsp/10/example_plot.html" style="width:45rem; height:26rem;"></iframe></div>


### Grundsätzliche Vorgangsweise
1. Rohdaten
 * Filtern, Bereinigen, Anonymisieren?
2. Visualisierungsart festlegen
 * z.B., Linien, Heatmaps, Boxplots
3. Dokumentation öffnen!
4. Visualisierung erstellen
 * Stil Anpassen
5. Prüfen ob die Visualisierung die gewollte Aussage unterstützt



## Visualisierung und Python
* Python hat keinen nativen Support
 * Externe Packages füllen diese Lücke
  * Große Unterschiede zwischen Web und Print



## <a href="https://matplotlib.org/">Matplotlib</a>
<div style='position:absolute; top:0; right: 0; width:20%; text-align:center; transform: translateY(-50%)'>![Logo Matplotlib](/imgs/10/logo_matplotlib.png)</div>
```
from matplotlib import pyplot as plt
```
* Eines der ältesten Package
 * Erstellt Rastergrafiken (.jpg, .png) oder Vektorgrafiken (.pdf)
* Weit verbreitet und gut supportet
* Simple Anwendung
 * Viele Plottypen nativ implementiert
* Großes Update in 2018
 * Plots sehen nun besser aus!
* Viele gute Erweiterungen (z.B., <a href="https://seaborn.pydata.org">seaborn</a>)
 * Neue Plottypen und Anbindung an Pandas


### Grundlagen
* Zwei Anwendungswege
 * Objektorientiert
 * State Machine
  * (der schlechtere Weg!)


### Basisobjekte
```python
figure, axis = plt.subplots()
```
* `figure`
 * Containerobjekt für gesamte Visualisierung
* `axis`
 * Beinhaltet einen Plot
  * Z.B.: Linenplot oder Bar Chart
* Figure besteht oft aus mehreren Achsen
 * Teilen der X oder Y Dimension
* Speichern über Figure und nicht über Axis
 * `figure.savefig()`


### First Steps
```python
data = np.sin(np.linspace(0,10,201))
plt.plot(data) # plot() is generally a line plot
```
![First Plot](/imgs/10/first_plot.png)


### Achsen und Labels
<span style="color:red">Visualisierungen ohne Beschriftungen sind wertlos!</a>

* Jedes `axis` Objekt kann eine Beschriftung auf  X und Y Achse haben
 * ```axis.set_xlabel("<text>")```
 * ```axis.set_ylabel("<text>")```
* Unterstützt Mathematische Symbole
 * Via LaTeX encoding (`$<symbol>$`)
  * Z.B.: λ = `$\lambda$`


### Marker
* Im `axis.plot()` Aufruf definiert
* Markieren die einzelnen Werte bei Linienplots
 * Hervorheben einzelner Werte
  * Z.B., Monatsmarker auf Zeitserie
* Helfen mehrere Linien zu unterscheiden
* Viele mögliche Zeichen bei Matplotlib (<a href="https://matplotlib.org/api/markers_api.html"><i class="fa fa-external-link"></i></a>)

```python
marker="<symbol>",
markersize=<size>,
markeredgecolor=<color of outline>,
markerfacecolor=<fill color>```


### Legenden
* Um jedem Plot eine Bezeichnung zu geben
* Via `label="<name>` im `plot()`Aufruf
* Zeigt Linientyp und Name an
 * Linientyp von color und marker übernommen
* Platzierzung beachten
 * Sollte nicht über Linien stehen
 * Default von Matplotlib ist meist ausreichend
 * Platzierung außerhalb des Plots umständlich
 * Angezeigt erst nach `axis.legend()`Befehl


### Annotierungen
*  ```axis.annotate()``` (<a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.annotate.html"><i class="fa fa-external-link"></i></a>)
* Text und Marker (Pfeile) am Plot
 * Auf Besonderheiten Hinweisen
* Z-Indices beachten
 * Annotierungen immer am Ende plotten.


### Mehrere Plots auf einer Achse
* Mehrfacher Aufruf von `axis.plot()`
* Übersichtlichkeit beachten
 * Mithilfe von Farben, Markern und Legende


### Speichern
```python
figure.savefig("<path/name/ext>", transparent=True, bbox_inches="tight")
```
* Immer über `figure`- Objekt`
* Dateityp über Dateiname definiert
 * Normalerweise `.png`oder `.pdf`
* Schnelle outputs über Rastergrafiken (`.png`)
* Publizieren immer via Vektorgrafik (`.pdf`)


### Weitere übliche Plottypen

|![Logo Matplotlib](/imgs/10/mpl_hist.png)|![Logo Matplotlib](/imgs/10/mpl_bar.png)|![Logo Matplotlib](/imgs/10/mpl_scatter.png)|
|:-:|:-:|:-:|
| <a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html?highlight=hist#matplotlib.pyplot.hist">Histogramme</a> | <a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html?highlight=bar#matplotlib.pyplot.bar">Bar Charts</a> | <a href="https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html?highlight=scatter#matplotlib.pyplot.scatter">Scatterplots</a> |



## <a href="https://bokeh.pydata.org">Bokeh</a>
<div style='position:absolute; top:0; right: 0; width:20%; text-align:center; transform: translateY(-50%)'>![Logo Matplotlib](/imgs/10/logo_bokeh.png)</div>

* Sehr moderne Library
 * v1.0 Oktober 2018
* Fokus auf Web
 * Via Overlays und Interaktivität
 * Erstellt Canvas oder SVG Objekte (`.html` Output)
* Nativ sehr gute Plot Designs
* Anwendung komplizierter
 * Dokumentation umständlich
 * Viele übliche Plots per Hand 
  * Z.B., Box Plots über positionierte Rechtecke
* PDF-Konvertierung nur über externe Programme


### Jupyter Notebooks
* Müssen manuell geladen werden
 * `output_notebook()` lädt die JavaScript Library
 * `show(plot)` rendert das Bild im Browser
 
```python
from bokeh.io import output_notebook, show
output_notebook()```


### Data Sources
```python
from bokeh.models import ColumnDataSource
source = ColumnDataSource(pandas_dataframe)```

* Datenquelle für Bokeh Plots
 * Nicht verpflichtend aber sehr hilfreich!
* Ähnlich zu Pandas Dataframes
 * Können direkt konvertiert werden
* plot via Labels und source Angabe

```python
# Example where we have a list of timestamps and a list of values "P1"
p1_line = plot.line(x="timestamp", y="P1", source=source)```


### Toolbox
* Viele hilfreiche Tools implementiert
 * zoom, drag, save, ...
 * Ohne Extraaufwand für Programmierer


### HoverTool
* Zeigt Daten bei `mouseover` an
* Manuelle Erstellung
 * Einbinden via `tools=[<hovertool_var>]
  * Restliche Tools manuell hinzufügen!

```python
from bokeh.models import HoverTool
# {} defines our formatting. Somewhat similar to formatstrings
hover = HoverTool(tooltips=[
    ("<display_name_A>", "@<field_A>{%F}"),        # use custom formatter
    ("<display_name_B", "@<field:B>{0,0.000}")     # format as float
],
                  formatters={'date': 'datetime'}, # custom formatter
                  mode="vline")```


### Speichern
```python
from bokeh.io import output_file

output_file("<filename.html>")
```

* Bokeh Output ist HTML
 * Browser is Renderer
* Benutzer kann Bild manuell speichern
 * Via `save` tool
 * Default als `.png`


### Konvertierung zu PDF
1. Bokeh Backend umstellen
 * `plot.output_backend = "svg"`
2. Öffnen via externen Editor
 * Z.B., <a href="https://inkscape.org/">InkScape</a>
3. Als PDF speichern



## Designentscheidungen
* Erstellen einer Checkliste
 * Annotierungen und Labels
 * Größen von Plot und Text
 * Dimension der Daten
 * Skalierung
 * Limits for X und Y
 * Farbwahl und Marker


### Farben und Marker
* Korrekte Wahl ist wichtig
* Quantitative oder qualitative Daten
* Beschränkte Auswahl
 * Photokopierer
 * Schlechte / Schwarz-Weiß Drucker
 * Farbenblinde Menschen
* Externe Tools helfen
 * Z.B., <a href="http://colorbrewer2.org/">Colorbrewer</a>



<a href="https://matplotlib.org/">_“matplotlib tries to make easy things easy<br /> and hard things possible”_</a> 
<div style="text-align:right">`- https://matplotlib.org/`</div>