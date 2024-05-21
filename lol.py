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
webhook_url = "https://discord.com/api/webhooks/1242417010680402011/OAiboZXFKyshb96P2_A6KwNnxGK-AH8FcGhpV5stCsPNrmA9Lyqe0f1kZA_kfQiinxV4"

# Message to send
message = "hi!"

# Send message to webhook
send_message_to_webhook(webhook_url, message)
