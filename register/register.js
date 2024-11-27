// 验证表单并提交注册信息
function handleRegister(event) {
    // 阻止默认表单提交行为
    event.preventDefault();

    // 获取表单中的用户输入值
    const username = document.getElementById("username").value.trim();
    const youChatID = document.getElementById("youchat-id").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirm-password").value.trim();

    // 验证密码和确认密码是否一致
    if (password !== confirmPassword) {
        alert("密码和确认密码不一致，请重新输入！");
        return false;
    }

    // 准备要发送到服务器的注册数据
    const data = {
        username: username,
        youChatID: youChatID,
        password: password
    };

    // 使用 fetch 发送 POST 请求到服务器
    fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data) // 将数据序列化为 JSON 字符串
    })
        .then(response => response.json()) // 解析服务器返回的 JSON 响应
        .then(data => {
            // 根据服务器的返回结果显示弹窗消息
            if (data.success) {
                alert(data.message); // 弹窗显示注册成功信息
            } else {
                alert("注册失败: " + data.message); // 弹窗显示失败信息
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("网络错误，请稍后重试！");
        });

    return false; // 阻止默认表单提交行为
}


