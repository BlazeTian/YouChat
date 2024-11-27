document.addEventListener("DOMContentLoaded", () => {
    const avatar = document.getElementById("avatar");
    const updateAvatarBtn = document.getElementById("updateAvatarBtn");
    const avatarModal = document.getElementById("avatarModal");
    const avatarInput = document.getElementById("avatarInput");
    const saveAvatarBtn = document.getElementById("saveAvatarBtn");
    const cancelAvatarBtn = document.getElementById("cancelAvatarBtn");
    const usernameElement = document.getElementById("username");
    const youchatIdElement = document.getElementById("youchat-id");
    const signatureText = document.getElementById("signatureText");
    const editSignatureBtn = document.getElementById("editSignatureBtn");
    const signatureModal = document.getElementById("signatureModal");
    const signatureInput = document.getElementById("signatureInput");
    const saveSignatureBtn = document.getElementById("saveSignatureBtn");
    const cancelSignatureBtn = document.getElementById("cancelSignatureBtn");

    // 从本地存储获取登录后的youChatID
    const youChatID = localStorage.getItem("youChatID");

    // 加载用户信息
    function loadUserInfo() {
        fetch("http://127.0.0.1:8000/user_info", {
            headers: {
                'YouChat-ID': youChatID,  // 发送youChatID来获取用户数据
            }
        })
        .then(response => response.json())
        .then(data => {
            usernameElement.textContent = `用户名：${data.username}`;
            youchatIdElement.textContent = `YouChat-ID：${data.youchat_id}`;
            avatar.src = data.avatar_path || "default-avatar.png";
            signatureText.textContent = data.signature || "请完善信息";
        })
        .catch(error => console.error("Error loading user info:", error));
    }

    // 显示修改头像弹窗
    updateAvatarBtn.addEventListener("click", () => {
        avatarModal.style.display = "flex";
    });

    // 保存头像
    saveAvatarBtn.addEventListener("click", () => {
        const file = avatarInput.files[0];
        if (!file) {
            alert("请选择一个头像文件！");
            return;
        }

        const formData = new FormData();
        formData.append("avatar", file);
        formData.append("youchat_id", youChatID);  // 发送用户ID

        fetch("http://127.0.0.1:8000/update_avatar", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("头像修改成功！");
                loadUserInfo();  // 更新用户信息
                avatarModal.style.display = "none";  // 关闭弹窗
            } else {
                alert("头像修改失败：" + data.message);
            }
        })
        .catch(error => console.error("Error updating avatar:", error));
    });

    // 取消修改头像
    cancelAvatarBtn.addEventListener("click", () => {
        avatarModal.style.display = "none";
    });

    // 显示修改签名弹窗
    editSignatureBtn.addEventListener("click", () => {
        signatureModal.style.display = "flex";
        signatureInput.value = signatureText.textContent !== "请完善信息" ? signatureText.textContent : "";
    });

    // 保存签名
    saveSignatureBtn.addEventListener("click", () => {
        const signature = signatureInput.value.trim();
        fetch("http://127.0.0.1:8000/update_signature", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ signature, youchat_id: youChatID }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("个性签名修改成功！");
                loadUserInfo();  // 更新用户信息
                signatureModal.style.display = "none";  // 关闭弹窗
            } else {
                alert("修改失败：" + data.message);
            }
        })
        .catch(error => console.error("Error updating signature:", error));
    });

    // 取消修改签名
    cancelSignatureBtn.addEventListener("click", () => {
        signatureModal.style.display = "none";
    });

    loadUserInfo();  // 加载初始用户信息
});
