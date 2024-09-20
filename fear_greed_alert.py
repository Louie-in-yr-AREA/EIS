import requests

# 设置 API 请求的URL和头部信息
url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"
headers = {
    "X-RapidAPI-Host": "fear-and-greed-index.p.rapidapi.com",
    "X-RapidAPI-Key": "d515691a9amsh941d26733ba015bp1769acjsnda76a9887fbc"  
}

# Telegram 机器人 Token 和 Chat ID
TELEGRAM_BOT_TOKEN = "7217513520:AAGVSH1s57NYb35wIZWycyQTX17vUhdV8po"  # Bot Token
TELEGRAM_CHAT_ID = "6520451366"  #Chat ID

# 定义发送 Telegram 消息的函数
def send_telegram_message(current_index):
    message = f"当前恐惧和贪婪指数为：{current_index}，低于50，别人恐惧我贪婪！"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Telegram 消息发送成功")
        else:
            print(f"Telegram 消息发送失败: {response.text}")
    except Exception as e:
        print(f"发送消息时出错: {e}")

# 获取恐惧和贪婪指数
def get_fear_and_greed_index():
    response = requests.get(url, headers=headers)
    
    # 打印完整的响应内容
    print("API Response Text:", response.text)
    
    if response.status_code == 200:
        data = response.json()
        print("Parsed JSON Data:", data)
        if 'fgi' in data:
            current_index = data['fgi']['now']['value']
            return current_index
        else:
            print("Key 'fgi' not found in the response data.")
            return None
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None

# 检查指数并发送通知
def check_and_notify():
    current_index = get_fear_and_greed_index()
    if current_index is not None:
        print(f"当前恐惧指数: {current_index}")
        if current_index < 50:
            print("恐惧指数低于50，发送 Telegram 提醒！")
            send_telegram_message(current_index)
        else:
            print("恐惧指数高于50，市场情绪较好。")
    else:
        print("未能获取到有效的恐惧指数数据。")

# 调用检查函数
check_and_notify()
