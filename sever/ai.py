import openai
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  

# 设置 OpenAI API Key - 推荐从环境变量中读取
import os
openai.api_key = os.getenv('OPENAI_API_KEY', '')

# 创建一个 Flask 应用
app = Flask(__name__)
CORS(app)  # 启用 CORS，允许所有来源的请求


openai.api_base = ''#基地址，每个key也许使用方式不一样，自己阅读哈，不会找天哥

@app.route('/')
def index():
    return render_template('ai.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 使用 gpt-3.5-turbo 模型
            messages=[{"role": "user", "content": user_input}],
            max_tokens=200,
            temperature=0.7
        )
        
        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
