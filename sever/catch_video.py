import os
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

VIDEO_FOLDER = './app/uploads/video'  # 保存视频的路径


def download_video(video_url, save_path):
    try:
        # 确保保存路径的目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 发起 HTTP 请求下载视频
        response = requests.get(video_url, stream=True)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 获取视频的总大小（字节）
            total_size = int(response.headers.get('content-length', 0))
            
            print(f"开始下载视频，总大小: {total_size / 1024 / 1024:.2f} MB")
            
            with open(save_path, 'wb') as file:
                downloaded_size = 0
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # 检查块是否为空
                        file.write(chunk)
                        downloaded_size += len(chunk)
                        # 实时打印下载进度
                        print(f"\r下载进度: {downloaded_size / total_size * 100:.2f}%", end='')
            print(f"\n视频已保存到: {save_path}")
        else:
            print(f"下载失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")


@app.route('/download', methods=['GET'])
def download_video_endpoint():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"status": "error", "message": "Missing URL"}), 400

    video_filename = video_url.split('/')[-1]+'.mp4'  # 假设文件名来自 URL
    local_path = os.path.join(VIDEO_FOLDER, video_filename)

    # 调用下载函数
    download_video(video_url, local_path)
    
    return jsonify({"status": "success", "message": f"Video downloaded to {local_path}"})


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
