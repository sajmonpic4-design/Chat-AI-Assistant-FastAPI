const message = document.getElementById('message');
        const response = document.getElementById('response');
        const sendButton = document.getElementById('send');

        async function sendMessage() {
            const text = message.value.trim();
            if (!text) {
                response.textContent = 'Wpisz wiadomość przed wysłaniem.';
                return;
            }

            sendButton.disabled = true;
            sendButton.textContent = 'Ładowanie...';
            response.textContent = 'Oczekiwanie na odpowiedź...';

            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ content: text })
                });

                const data = await res.json();
                if (!res.ok) {
                    response.textContent = data.error || 'Wystąpił błąd serwera';
                } else {
                    response.textContent = data.reply || 'Brak odpowiedzi.';
                }
            } catch (error) {
                response.textContent = 'Błąd połączenia: ' + error.message;
            } finally {
                sendButton.disabled = false;
                sendButton.textContent = 'Wyślij';
            }
        }

        sendButton.addEventListener('click', sendMessage);
        message.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' && event.ctrlKey) {
                sendMessage();
            }
        });