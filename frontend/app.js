
document.addEventListener('DOMContentLoaded', function(){

    const messagesContainer = document.querySelector("#messagesContainer");
    const messageInput = document.querySelector("#exampleFormControlTextarea1")
    const sendMessageButton = document.querySelector("[name=sendMessageButton]")

    let websocketClient = new WebSocket("ws://localhost:8765");

    websocketClient.onopen = () => {
        sendMessageButton.onclick = () => {
            websocketClient.send("SendMessage " + messageInput.value);
            messageInput.value = "";
        };
    };

    websocketClient.onmessage = (message) => {
        console.log(message.data);
        const newMessage = document.createElement('div');
        newMessage.innerHTML = message.data;
//        messagesContainer.appendChild(message);
    };

}, false);
