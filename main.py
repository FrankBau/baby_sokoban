### Diese Datei main.py soll bearbeitet (editiert) werden.
### Wenn für die Lösung einer Übungsaufgabe eine Datei abgegeben werden soll, dann diese!

import sokoban

# Benutzen Sie für die Abgaben Ihre eigene Matrikelnummer.
# Jede Matrikelnummer erzeugt eine andere Welt.
# In seltenen Fällen ist ihr Spiel nicht lösbar weil die z.B. Box am Rand steht. 
# Wenden sie sich in diesem Fall an den Dozenten um eine alternativen Startwert zu erhalten.
 
# Die hier angegebene Matrikelnummer erzeugt nur meine Referenzwelt die auch in der Doku verwendet wird, bitte ändern.
s = sokoban.World("s0123456")

### BEGIN fügen sie unter dieser Zeile ihren Code zur Lösung ein.

while s.me.x < s.w-1:
    s.right()


### END

# Idealerweie ist die Box jetzt auf dem Target und das Spiel gewonnen.
# Falls (noch) nicht, können sie den Sokoban mit der Tastatur (Pfeiltasten) bewegen.
# Ändern Sie ab hier nichts mehr. 

# manual keyboard control
while not s.winning():
    k = s.waitKey()
    if k=='q':
        break
    if k == 'w':
        s.up()
    if k == 'a':
        s.left()
    if k == 's':
        s.down()
    if k == 'd':
        s.right()

# ende, sie haben gewonnen