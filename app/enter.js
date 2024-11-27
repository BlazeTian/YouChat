document.addEventListener("DOMContentLoaded", () => {
    const messageInput = document.getElementById("message-input");
    const chatHistory = document.querySelector(".chat-history");

    // 监听输入框的键盘事件
    messageInput.addEventListener("keydown", (event) => {
        // 按下 Enter 键（不包括 Shift+Enter 的组合）
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault(); // 阻止默认行为（换行）
            sendMessage();
        }
    });

    // 发送消息
    function sendMessage() {
        const message = messageInput.value.trim();

        // 如果消息为空，则不发送
        if (!message) return;

        // 清空输入框
        messageInput.value = "";

        // 创建消息 DOM 节点（展示自己的消息）
        const messageElement = document.createElement("div");
        messageElement.classList.add("chat-message", "self");

        const messageContent = document.createElement("div");
        messageContent.classList.add("message-content");
        messageContent.textContent = message;

        const avatar = document.createElement("img");
        avatar.classList.add("message-avatar");
        avatar.src = "user1.png";
        avatar.alt = "我的头像";

        messageElement.appendChild(messageContent);
        messageElement.appendChild(avatar);

        // 将消息添加到聊天记录中
        chatHistory.appendChild(messageElement);

        // 滚动到最新消息
        chatHistory.scrollTop = chatHistory.scrollHeight;

        // 模拟发送消息到服务器（需要后端实现实际逻辑）
        console.log("消息已发送:", message);
    }
});
