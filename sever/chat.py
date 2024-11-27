from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room
from cryptography.fernet import Fernet

# 初始化 Flask 和 SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'blaze_tian'
socketio = SocketIO(app)

# 生成对称密钥（真实项目中应存储并保护密钥）
SECRET_KEY = Fernet.generate_key()
cipher = Fernet(SECRET_KEY)

# 路由：主页
@app.route('/')
def index():
    return render_template('index.html')

# 加密消息
def encrypt_message(message):
    return cipher.encrypt(message.encode()).decode()

# 解密消息
def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message.encode()).decode()

# 处理消息发送事件
@socketio.on('message')
def handle_message(encrypted_msg):
    try:
        # 解密收到的消息
        msg = decrypt_message(encrypted_msg)
        print(f"收到解密消息: {msg}")

        # 处理逻辑并加密消息广播
        encrypted_response = encrypt_message(f"服务器收到: {msg}")
        send(encrypted_response, broadcast=True)  # 广播加密消息
    except Exception as e:
        print(f"消息解密失败: {e}")

# 用户加入房间
@socketio.on('join')
def handle_join(room):
    join_room(room)
    print(f'用户加入了房间 {room}')

# 用户离开房间
@socketio.on('leave')
def handle_leave(room):
    leave_room(room)
    print(f'用户离开了房间 {room}')

# 启动服务器
if __name__ == '__main__':
    print(f"加密密钥: {SECRET_KEY.decode()} (请保护好此密钥)")
    socketio.run(app, host='0.0.0.0', port=5000)
