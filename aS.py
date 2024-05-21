import requests

def send_message_to_webhook(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Your webhook URL
webhook_url = "https://discord.com/api/webhooks/1242470402119176252/-UM4OaqM5cvHJrQ2pxiXYmJv5CP3zgCRn8W3dZJws7za87QWr8koLLftOHs4zaCTtxqx"

# Message to send
message = "hi!"

# Send message to webhook
send_message_to_webhook(webhook_url, message)
