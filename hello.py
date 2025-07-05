"Was passiert technisch, wenn ich python hello.py im Terminal eingebe?"
"Antwort: 1. Es wird Text(Code) in einer Datei hello.py"
"2. Der Python-Interpreter liest die Datei"
"3. Python übersertzt Zeile für Zeile in Bytecode(Zwischencode)"
"4. Die sogenannte Python Virtual Machine(PVM) führt diesen Bytecode direkt aus."
"5. Die Ausgaeb erscheint im Terminal"
"Merke: Code → Interpreter → Bytecode → Ausführung → Ausgabe"

"Technische Details: Python ist keine Kompiliersprache wie C. Es wird interpretiert. Der Code wird nicht in eine .exe-Datei umgewandelt. Python prüft jede Zeile beim Ausführen - Syntaxfehler stoppen sofort den Ablauf."
print("Hello.")
