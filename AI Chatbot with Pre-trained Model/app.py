from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Load pre-trained conversational model (DialoGPT)
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Initialize the pipeline with text-generation task
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

def chat_with_bot():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Chatbot response generation
        bot_input = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        bot_output = model.generate(bot_input, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        bot_response = tokenizer.decode(bot_output[0], skip_special_tokens=True)
        print("Bot: " + bot_response)

# Start chat with the bot
chat_with_bot()
