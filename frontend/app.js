
document.addEventListener('DOMContentLoaded', function(){

    const messagesContainer = document.querySelector("#messagesContainer");
    const messageInput = document.querySelector("[name=messageInput]")
    const sendMessageButton = document.querySelector("[name=sendMessageButton]")

    let websocketClient = new WebSocket("ws://localhost:12345");

    websocketClient.onopen = () => {
        console.log("Client connected");
        sendMessageButton.onclick = () => {
            websocketClient.send(messageInput.value);
            messageInput.value = "",
        };
    };

    websocketClient.onmessage = (message) => {
        const message = document.createElement('div');
        message.innerHTML = message.data;
        messagesContainer.appendChild(message):
    };

}, false);
