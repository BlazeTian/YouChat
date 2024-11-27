document.addEventListener('DOMContentLoaded', function () {
    // 初始化聊天记录展示
    loadChatHistory();
    // 每隔3秒请求一次聊天数据，保持实时更新
    setInterval(loadChatHistory, 3000);
});

// 请求并加载聊天记录
function loadChatHistory() {
    fetch('http://localhost:8000/chat')
        .then(response => response.json())
        .then(data => {
            displayMessages(data);
        })
        .catch(error => {
            console.error('加载聊天记录失败:', error);
        });
}

// 渲染消息到聊天框
function displayMessages(messages) {
    const chatHistory = document.querySelector('.chat-history');
    chatHistory.innerHTML = ''; // 清空历史消息

    messages.forEach(msg => {
        const messageElement = createMessageElement(msg);
        chatHistory.appendChild(messageElement);
    });

    // 滚动到聊天窗口底部
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// 创建一条消息元素
function createMessageElement(msg) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message');
    
    // 根据消息的发送者，决定消息显示在左侧还是右侧
    const isSelf = msg.sender === 'user1'; // 判断是否为自己
    messageElement.classList.add(isSelf ? 'self' : 'other');

    const avatar = document.createElement('img');
    avatar.classList.add('message-avatar');
    avatar.src = isSelf ? 'static/images/user1.png' : 'static/images/user2.png'; // 自己和对方的头像不同
    messageElement.appendChild(avatar);

    const content = document.createElement('div');
    content.classList.add('message-content');

    switch (msg.type) {
        case 'text':
            content.textContent = msg.content;
            break;
        case 'image':
            const img = document.createElement('img');
            img.src = msg.content;
            img.alt = '图片消息';
            img.classList.add('message-image');
            content.appendChild(img);
            break;
        case 'audio':
            const audio = document.createElement('audio');
            audio.controls = true;
            audio.src = msg.content;
            content.appendChild(audio);
            break;
        case 'video':
            const video = document.createElement('video');
            video.controls = true;
            video.src = msg.content;
            content.appendChild(video);
            break;
        default:
            content.textContent = '未知消息类型';
    }

    messageElement.appendChild(content);

    return messageElement;
}
