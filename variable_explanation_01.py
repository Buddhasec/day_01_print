"Ein String ist eine Zeichenkette also Text"
"Man schreibt Text in doppelten oder einfachen Anführungszeichen"
string = "Text"

"Ein f-string wird verwendet um Text und Variablen zu kombinieren. Die Variable ist dabei in geschweifte Klammern zu setzen."
print(f"Das ist ein {string}.")

"Ein Integer ist eine ganze Zahl, z.B. 42. Wichtig ist keine Anführungszeichen für diese Variable zu verwenden."
integer = 42
print(f"Die Antwort auf alles lautet {integer}.")

"Ein Float ist eine Zahle mit Dezimalpunkt, z.B. 42.0. Wichtig ist dem Integer der Variable ein float(42) vorran zu setzen."
float_number = float(42)
print(f"Die Antwort auf alles mit Dezimalpunkt lautet {float_number}.")

"Ein Boolean ist ein Wahrheitswert der entweder True oder False ist."
boolean = True
print(f"Bist Du ein Boolean? {boolean}")

if boolean:
    print(f"Ja, ich bin ein Boolean.")
else:
    print(f"Ich bin kein Boolean.")

string1 = "Text1"
integer1 = 43
float1 = float(43)

print(f"Das ist ein {string1} und eine {integer1} nicht zu verwechseln mit einer {float1}.")
if boolean:
    print(f"Das ist ein Boolean1.")
else:
    print(f"Das ist kein Boolean1.")
