// 处理登录表单的提交
/*function handleLogin(event) {
    // 阻止表单的默认提交行为
    event.preventDefault();

    // 获取用户输入的账号和密码
    const youChatID = document.getElementById("youchat-id").value.trim();
    const password = document.getElementById("password").value.trim();

    // 检查输入是否为空
    if (!youChatID || !password) {
        alert("请输入完整的账号和密码！");
        return false;
    }

    // 构造请求数据
    const data = {
        youChatID: youChatID,
        password: password,
    };

    // 使用 fetch 发送 POST 请求到服务器
    fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data), // 将数据序列化为 JSON 格式
    })
        .then((response) => response.json()) // 将服务器返回的 JSON 数据解析为对象
        .then((result) => {
            // 根据服务器的响应，显示对应的弹窗消息
            if (result.success) {
                alert(result.message); // 登录成功
                window.location.href = "../my_info/my_info.html"; // 跳转到绝对路径
            } else {
                alert("登录失败: " + result.message); // 显示失败信息
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("网络错误，请稍后重试！");
        });

    return false; // 阻止默认表单行为
}*/
// 处理登录表单的提交
function handleLogin(event) {
    // 阻止表单的默认提交行为
    event.preventDefault();

    // 获取用户输入的账号和密码
    const youChatID = document.getElementById("youchat-id").value.trim();
    const password = document.getElementById("password").value.trim();

    // 检查输入是否为空
    if (!youChatID || !password) {
        alert("请输入完整的账号和密码！");
        return false;
    }

    // 构造请求数据
    const data = {
        youChatID: youChatID,
        password: password,
    };

    // 使用 fetch 发送 POST 请求到服务器
    fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data), // 将数据序列化为 JSON 格式
    })
        .then((response) => response.json()) // 将服务器返回的 JSON 数据解析为对象
        .then((result) => {
            // 根据服务器的响应，显示对应的弹窗消息
            if (result.success) {
                alert(result.message); // 登录成功

                // 保存登录成功的 youChatID 到 localStorage
                localStorage.setItem("youChatID", youChatID);

                window.location.href = "../my_info/my_info.html"; // 跳转到绝对路径
            } else {
                alert("登录失败: " + result.message); // 显示失败信息
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("网络错误，请稍后重试！");
        });

    return false; // 阻止默认表单行为
}

