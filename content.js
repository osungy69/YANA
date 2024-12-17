const chatBox = document.createElement("div");
chatBox.id = "chat-box";
chatBox.style.position = "fixed";
chatBox.style.bottom = "10px";
chatBox.style.right = "10px";
chatBox.style.backgroundColor = "white";
chatBox.style.border = "1px solid black";
chatBox.style.padding = "10px";
chatBox.innerHTML = `
  <div id="messages"></div>
  <input type="text" id="message-input" placeholder="Type your message..." />
  <button id="send-message">Send</button>
`;
document.body.appendChild(chatBox);
