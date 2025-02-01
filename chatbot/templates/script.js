function sendQuery() {
    const queryInput = document.getElementById('query-input');
    const chatMessages = document.getElementById('chat-messages');
    
    fetch('/legal-query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: queryInput.value })
    })
    .then(response => response.json())
    .then(data => {
        chatMessages.innerHTML += `
            <div class="user-message">${queryInput.value}</div>
            <div class="ai-message">${data.response}</div>
        `;
        queryInput.value = '';
    });
}
function sendQuery() {
    const queryInput = document.getElementById('query-input');
    const chatMessages = document.getElementById('chat-messages');
    
    fetch('/legal-query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: queryInput.value })
    })
    .then(response => response.json())
    .then(data => {
        chatMessages.innerHTML += `
            <div class="user-message">${queryInput.value}</div>
            <div class="ai-message">${data.response}</div>
        `;
        queryInput.value = '';
    });
}
