'''from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from register import handle_register
from login import handle_login

# 路由映射：路径 -> 处理函数
ROUTES = {
    "/register": handle_register,
    "/login": handle_login,
}

class MainHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="application/json"):
        """设置 HTTP 响应头"""
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        """处理 OPTIONS 请求，用于 CORS 预检"""
        self._set_headers()

    def do_POST(self):
        """处理 POST 请求，根据路径动态调用对应的处理函数"""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")

        # 根据路径查找对应的处理函数
        handler = ROUTES.get(self.path)
        if handler:
            # 调用处理函数，返回状态码和响应数据
            status_code, response = handler(post_data)
        else:
            # 路径未找到
            status_code, response = 404, {"success": False, "message": "路径未找到！"}

        # 设置响应头并返回响应数据
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=MainHTTPRequestHandler, port=8000):
    """启动 HTTP 服务器"""
    server_address = ("0.0.0.0", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from register import handle_register
from login import handle_login
from my_info import handle_update_avatar, handle_update_signature  # 导入 my_info.py 中的处理函数

# 路由映射：路径 -> 处理函数
ROUTES = {
    "/register": handle_register,
    "/login": handle_login,
    "/update_avatar": handle_update_avatar,
    "/update_signature": handle_update_signature,
}

class MainHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="application/json"):
        """设置 HTTP 响应头"""
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        """处理 OPTIONS 请求，用于 CORS 预检"""
        self._set_headers()

    def do_POST(self):
        """处理 POST 请求，根据路径动态调用对应的处理函数"""
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")

        # 根据路径查找对应的处理函数
        handler = ROUTES.get(self.path)
        if handler:
            # 调用处理函数，返回状态码和响应数据
            status_code, response = handler(post_data)
        else:
            # 路径未找到
            status_code, response = 404, {"success": False, "message": "路径未找到！"}

        # 设置响应头并返回响应数据
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=MainHTTPRequestHandler, port=8000):
    """启动 HTTP 服务器"""
    server_address = ("0.0.0.0", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()