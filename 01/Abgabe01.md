# 1.1 Search Space properties

# 1.2 Search Space 1
1.
Wenn man eine rein geographische Route planen möchte, wäre der Zustandsraum alle Haltestellen des Nahverkehrs. Dann sind die Knoten die Haltestellen, die Kanten sind alle Strecken zwischen zwei Stationen, die ohne Zwischenhalt gefahren werden und die Kantengewichte repräsentieren die Fahrtdauer zwischen den beiden.

2. 
    a.
Das Modell repräsentiert den Füllstand der beiden Jugs als Tuple mit dem 4-Liter Jug als erste und dem 3-Liter Jug als zweite Stelle. Die Werte des Tupels sind in Litern, somit ist 0 für beide Stellen der minimale und 4 bzw 3 (4,3) die maximalen Werte. Der Startzustand ist (0,0).
Übergänge entstehen durch Füllen eines Jugs mit dem Zapfhahn, entleeren eines Jugs oder durch Umfüllen eines Jugs in den Anderen, wobei entweder der befüllte Jug komplett gefüllt oder der füllende Jug komplett entleert werden muss.
Mögliche Zustände sind: (0,0), (4,0), (1,3), (4,3), (0,3), (3,0), (3,3), (4,2), (0,2), (2,0).
Das Ziel ist der Zustand (2,0).
Die Zustandsreihenfolge um das Rätsel zu lösen ist: (0,0), (0,3), (3,0), (3,3), (4,2), (0,2), (2,0)
    b. Das Rätsel ist immer noch genauso lösbar, nur trinkt man den Wein anstatt ihn wegzukippen. Dass dies eventuell länger dauert, ist zu vernachlässigen.
