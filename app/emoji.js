// 获取emoji按钮和emoji面板
const emojiButton = document.getElementById('emoji-button');
const emojiPanel = document.getElementById('emoji-panel');
const messageInput = document.getElementById('message-input');

// 切换emoji面板的显示/隐藏
emojiButton.addEventListener('click', function() {
    const isPanelVisible = emojiPanel.style.display === 'block';
    emojiPanel.style.display = isPanelVisible ? 'none' : 'block';
});

// 插入表情符号到输入框
function insertEmoji(emoji) {
    const cursorPosition = messageInput.selectionStart;
    const currentText = messageInput.value;
    messageInput.value = currentText.slice(0, cursorPosition) + emoji + currentText.slice(cursorPosition);
    messageInput.focus();
    messageInput.selectionEnd = cursorPosition + emoji.length; // 保持光标位置
    emojiPanel.style.display = 'none'; // 发送表情后隐藏面板
}

// 如果点击输入框以外的区域，则关闭emoji面板
document.addEventListener('click', function(event) {
    if (!emojiPanel.contains(event.target) && event.target !== emojiButton) {
        emojiPanel.style.display = 'none';
    }
});
