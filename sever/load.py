import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# 存储聊天记录的文件路径
CHAT_FILE_PATH = "data/user1.json"

# 请求处理类
class RequestHandler(BaseHTTPRequestHandler):
    
    def _send_response(self, data, status_code=200):
        """发送响应"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def do_GET(self):
        """处理 GET 请求"""
        if self.path == '/chat':
            self._send_chat_history()
        else:
            self.send_error(404, "Not Found")
    
    def _send_chat_history(self):
        """发送聊天记录"""
        try:
            # 读取聊天记录文件
            with open(CHAT_FILE_PATH, 'r', encoding='utf-8') as f:
                chat_history = json.load(f)
            self._send_response(chat_history)
        except FileNotFoundError:
            # 如果文件不存在，则返回空列表
            self._send_response([], 404)
        except Exception as e:
            # 出现其他错误，返回错误信息
            self._send_response({"error": str(e)}, 500)

# 启动服务器
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    """启动 HTTP 服务器"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

# 启动服务器，端口为8000
if __name__ == '__main__':
    run(port=8000)
