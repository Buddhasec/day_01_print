zahl = 42
print(type(zahl))   # Ausgabe: <class 'int'>

x = 42
y = str(x)          # Umwandlung in einen String
z = bool(x)         # Umwandlung in einen Boolean (True, weil x ungleich 0)

print(y)            # "42"
print(type(y))      # <class 'str'>
print(z)            # True

antwort = None
if antwort is None:
    print("Noch keine Antwort gegeben.") # Wird ausgeführt

# Gute und schlechte Beispiele für Namenskonventionen
benutzer_name = "Buddha"
anzahl = 5
MAXIMAL_WERT = 100 # Konstante (Großbuchstaben)

# Input
name = input("Wie heißt Du? ")
print(f"Hallo {name}!") # Gibt den Namen aus

# Konstanten-Konvention: Großbuchstaben
PI = 3.14159
UMFANG = 2 * PI * 5
print(UMFANG)
