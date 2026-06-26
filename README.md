# 🤖 Sajmonpic4 Chat AI

Lokalny czat AI wykorzystujący model **Ollama** (`llama3.1:8b`) z minimalistycznym, responsywnym interfejsem webowym. Działa w 100% lokalnie – brak zewnętrznych API ani chmury.

---

## 📸 Zrzuty ekranu

### 🖥️ Interfejs główny
<img width="1864" height="949" alt="image" src="https://github.com/user-attachments/assets/ad72f694-2fea-4eaf-901a-abb6b4419470" />

### 💬 Przykładowa rozmowa
<img width="1863" height="945" alt="image" src="https://github.com/user-attachments/assets/63f1a6f8-b990-46fc-ac78-e3ce528852d7" />


### 📱 Widok mobilny
<img width="581" height="922" alt="image" src="https://github.com/user-attachments/assets/d9e3eed3-e72a-408f-90f1-cfc5baa69b15" />


---

## ✨ Funkcje

- 🧠 **Lokalne AI** – wykorzystuje model `llama3.1:8b` uruchomiony przez Ollama
- 🎨 **Nowoczesny interfejs** – elegancki, responsywny design z efektami wizualnymi
- ⌨️ **Skróty klawiszowe** – wyślij wiadomość przez `Ctrl+Enter`
- ✨ **Czyszczenie odpowiedzi** – automatyczne usuwanie kodów ANSI i powtarzających się słów
- ⚡ **Szybka komunikacja** – REST API (`/chat`) przyjmuje wiadomości i zwraca odpowiedź
- 🛡️ **Obsługa błędów** – czytelne komunikaty w przypadku problemów z AI lub połączeniem

---

## 🛠️ Technologie

| Warstwa | Technologie |
|---------|-------------|
| **Backend** | Python, FastAPI, Uvicorn |
| **AI** | Ollama (model `llama3.1:8b`) |
| **Frontend** | HTML5, CSS3 (zmienne, flexbox, gradienty), Vanilla JS |

---

## 📦 Wymagania

- Python 3.8+
- [Ollama](https://ollama.com/) zainstalowane i uruchomione
- Model `llama3.1:8b` pobrany:
```bash
ollama pull llama3.1:8b


