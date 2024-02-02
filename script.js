function getHostIP() {
    return window.location.hostname;
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const content = messageInput.value;

    if (content.trim() !== '') {
        const apiUrl = `http://${getHostIP()}:8888/api/messages`;

        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content: content }),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            messageInput.value = '';
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Message content cannot be empty');
    }
}

function getMessages() {
    const messageTableBody = document.getElementById('messageTableBody');
    const apiUrl = `http://${getHostIP()}:8888/api/messages`;

    fetch(apiUrl, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        renderMessages(data.messages);
    })
    .catch(error => console.error('Error:', error));
}

function renderMessages(messages) {
    const messageTableBody = document.getElementById('messageTableBody');
    messageTableBody.innerHTML = '';

    messages.forEach(message => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${message.id}</td>
            <td>${message.content}</td>
            <td>${message.created_at}</td>
        `;
        messageTableBody.appendChild(row);
    });
}
