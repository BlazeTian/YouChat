import json
import os

USER_DATA_FILE = "user.json"

def load_user_data():
    """加载用户数据"""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def save_user_data(data):
    """保存用户数据"""
    with open(USER_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def handle_register(post_data):
    """处理注册逻辑"""
    try:
        user_info = json.loads(post_data)
        username = user_info.get("username")
        youchat_id = user_info.get("youChatID")
        password = user_info.get("password")

        if not username or not youchat_id or not password:
            return 400, {"success": False, "message": "所有字段都是必填的！"}

        user_data = load_user_data()

        for user in user_data.values():
            if user["username"] == username:
                return 409, {"success": False, "message": "用户名已被注册，请更换！"}
            if user["youchat_id"] == youchat_id:
                return 409, {"success": False, "message": "YouChat-ID 已被注册，请重新生成！"}

        user_id = str(len(user_data) + 1)
        user_data[user_id] = {
            "username": username,
            "youchat_id": youchat_id,
            "password": password,
        }
        save_user_data(user_data)

        return 200, {"success": True, "message": "注册成功！"}

    except json.JSONDecodeError:
        return 400, {"success": False, "message": "请求数据格式错误！"}
