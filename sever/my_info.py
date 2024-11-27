'''import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import cgi

USER_DATA_FILE = "user.json"
AVATAR_DIR = "avatars"

# 加载用户数据
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# 保存用户数据
def save_user_data(data):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 保存头像
def save_avatar(file_data, youchat_id):
    if not os.path.exists(AVATAR_DIR):
        os.makedirs(AVATAR_DIR)

    avatar_filename = f"{youchat_id}_avatar.png"
    avatar_path = os.path.join(AVATAR_DIR, avatar_filename)

    with open(avatar_path, "wb") as avatar_file:
        avatar_file.write(file_data)

    return avatar_path  # 返回服务器路径

# 更新个性签名
def update_signature(signature, youchat_id):
    user_data = load_user_data()
    for user in user_data.values():
        if user["youchat_id"] == youchat_id:
            user["signature"] = signature
            save_user_data(user_data)
            return True
    return False

# 处理CORS
def set_cors_headers(handler):
    handler.send_header('Access-Control-Allow-Origin', '*')
    handler.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    handler.send_header('Access-Control-Allow-Headers', 'Content-Type, YouChat-ID')

# 请求处理类
class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        set_cors_headers(self)
        self.end_headers()

    def do_POST(self):
        if self.path == "/update_avatar":
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
            file_item = form['avatar']
            youchat_id = form.getvalue('youchat_id')

            if file_item.filename and youchat_id:
                file_data = file_item.file.read()
                avatar_path = save_avatar(file_data, youchat_id)

                # 更新用户数据中的头像路径
                user_data = load_user_data()
                for user in user_data.values():
                    if user["youchat_id"] == youchat_id:
                        user["avatar_path"] = avatar_path
                        save_user_data(user_data)
                        break

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": "头像更新成功！"}).encode('utf-8'))
            else:
                self.send_error(400, "头像文件或YouChat-ID缺失")

        elif self.path == "/update_signature":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)
            signature = data.get('signature')
            youchat_id = data.get('youchat_id')

            if signature and youchat_id:
                if update_signature(signature, youchat_id):
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "message": "个性签名更新成功！"}).encode('utf-8'))
                else:
                    self.send_error(404, "用户未找到")
            else:
                self.send_error(400, "签名或YouChat-ID缺失")

        else:
            self.send_response(404)
            self.end_headers()

# 运行服务器
def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
'''


import json
import os
import cgi

USER_DATA_FILE = "user.json"
AVATAR_DIR = "avatars"

# 加载用户数据
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# 保存用户数据
def save_user_data(data):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 保存头像
def save_avatar(file_data, youchat_id):
    if not os.path.exists(AVATAR_DIR):
        os.makedirs(AVATAR_DIR)

    avatar_filename = f"{youchat_id}_avatar.png"
    avatar_path = os.path.join(AVATAR_DIR, avatar_filename)

    with open(avatar_path, "wb") as avatar_file:
        avatar_file.write(file_data)

    return avatar_path  # 返回服务器路径

# 更新个性签名
def update_signature(signature, youchat_id):
    user_data = load_user_data()
    for user in user_data.values():
        if user["youchat_id"] == youchat_id:
            user["signature"] = signature
            save_user_data(user_data)
            return True
    return False

# 处理更新头像请求
def handle_update_avatar(post_data, files):
    file_item = files.get("avatar")
    youchat_id = post_data.get("youchat_id")

    if file_item and youchat_id:
        file_data = file_item["body"]  # 读取文件内容
        avatar_path = save_avatar(file_data, youchat_id)

        # 更新用户数据中的头像路径
        user_data = load_user_data()
        for user in user_data.values():
            if user["youchat_id"] == youchat_id:
                user["avatar_path"] = avatar_path
                save_user_data(user_data)
                return 200, {"success": True, "message": "头像更新成功！"}

    return 400, {"success": False, "message": "头像文件或YouChat-ID缺失"}

# 处理更新个性签名请求
def handle_update_signature(post_data):
    signature = post_data.get("signature")
    youchat_id = post_data.get("youchat_id")

    if signature and youchat_id:
        if update_signature(signature, youchat_id):
            return 200, {"success": True, "message": "个性签名更新成功！"}
        return 404, {"success": False, "message": "用户未找到"}

    return 400, {"success": False, "message": "签名或YouChat-ID缺失"}
