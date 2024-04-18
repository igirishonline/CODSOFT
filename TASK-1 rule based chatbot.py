data={
    "hi":"Hi there! I'm a friendly chatbot here to assist you?",
    "hello":"Hello! How can I help you today?",
    "tell me about AI bots":"An artificial intelligence bot is a computer program designed to simulate human conversation and provide automated responses.",
    "what can you do":"I can reply for your text and can answer you on a predefined rules",
    "what is paracetamol":"Paracetamol (acetaminophen[a] or para-hydroxyacetanilide) is a non-opioid analgesic and antipyretic agent used to treat fever and mild to moderate pain.[13][14][15] It is a widely used over the counter medication. Common brand names include Tylenol and Panadol.",
    "what is your name":"well i dont have a name! maybe you can say AI bot",
    "bye":"Bye! Take care and have a great day!",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Chatbot: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Chatbot: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Chatbot:",response)
    