from src.chatbot import get_response

print("🤖 Chatbot başlatıldı (çıkmak için 'q')\n")

while True:
    user = input("Sen: ")

    if user.lower() == "q":
        break

    response = get_response(user)
    print("Bot:", response)