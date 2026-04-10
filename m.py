import requests

url = "https://api.green-api.com/waInstance{{id}}/sendMessage/{{token}}"

payload = {
    "chatId": "201119644023@c.us",
    "message": "نفس الرسالة القنبلة بتاعتك هنا"
}

headers = {'Content-Type': 'application/json'}

# الإرسال في جزء من الثانية
response = requests.post(url, json=payload, headers=headers)
print(response.text)