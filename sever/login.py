'''import json
from register import load_user_data

def handle_login(post_data):
    """处理登录逻辑"""
    try:
        user_info = json.loads(post_data)
        youchat_id = user_info.get("youChatID")
        password = user_info.get("password")

        user_data = load_user_data()

        for user in user_data.values():
            if user["youchat_id"] == youchat_id and user["password"] == password:
                return 200, {"success": True, "message": "登录成功！"}

        return 401, {"success": False, "message": "账号或密码错误！"}

    except json.JSONDecodeError:
        return 400, {"success": False, "message": "请求数据格式错误！"}'''
        
import json
import os
from register import load_user_data  # 导入register.py中的load_user_data

USER_DATA_DIR = "user_data"  # 存放每个用户的详细信息的目录

# 登录处理逻辑
def handle_login(post_data):
    """处理登录逻辑"""
    try:
        user_info = json.loads(post_data)
        youchat_id = user_info.get("youChatID")
        password = user_info.get("password")

        user_data = load_user_data()  # 加载所有用户数据

        # 查找用户并验证密码
        for user in user_data.values():
            if user["youchat_id"] == youchat_id and user["password"] == password:
                # 登录成功，检查是否需要创建用户信息文件
                user_file_path = os.path.join(USER_DATA_DIR, f"{youchat_id}.json")

                if not os.path.exists(user_file_path):
                    # 如果文件不存在，创建新的 JSON 文件
                    user_info = {
                        "youchat_id": youchat_id,
                        "username": user["username"],
                        "avatar_path": "",  # 头像路径，后续可以更新
                        "signature": ""  # 个性签名，后续可以更新
                    }

                    # 确保目录存在
                    os.makedirs(USER_DATA_DIR, exist_ok=True)

                    with open(user_file_path, "w", encoding="utf-8") as file:
                        json.dump(user_info, file, ensure_ascii=False, indent=4)

                return 200, {"success": True, "message": "登录成功！"}

        return 401, {"success": False, "message": "账号或密码错误！"}

    except json.JSONDecodeError:
        return 400, {"success": False, "message": "请求数据格式错误！"}

