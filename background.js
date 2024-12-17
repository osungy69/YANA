console.log("Background service worker running!");

// WebSocket 연결 예제
const socket = new WebSocket("wss://your-chat-server.com");

socket.onopen = () => {
  console.log("WebSocket connected!");
};
