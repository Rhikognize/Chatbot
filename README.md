# Chatbot conversațional în Python

Acest proiect este un chatbot simplu scris în Python, care interacționează cu utilizatorul prin intermediul consolei, colectează răspunsuri și le salvează într-un fișier Excel.

## Funcționalități

- Pune întrebări de bază: nume, vârstă, interese.
- Procesează vârsta pentru a încadra utilizatorul într-o categorie (ex: "un copil", "un adult").
- Recunoaște și transformă unele interese comune în propoziții naturale.
- Salvează întreaga conversație într-un fișier `conversatii.xlsx`.
- Permite utilizatorului să continue sau să încheie conversația.

## Structură fișiere

- `main.py` – Logica principală a chatbotului.
- `transformations.py` – Funcții pentru procesarea textului, vârstei și intereselor.
- `excel.py` – Funcționalitate pentru salvarea conversației în Excel.
- `interests.py` – Dicționar cu interese recunoscute și forme transformate.

## Cum se folosește

1. Rulează scriptul principal:
2. Răspunde la întrebările botului.
3. La finalul fiecărei conversații, răspunsurile sunt salvate în conversatii.xlsx.