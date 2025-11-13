from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, target_language='es'):
    translated = translator.translate(text, dest=target_language)
    return translated.text

# Example usage
text = "Hello, how are you?"
print("Translated text:", translate_text(text, 'es'))  # Translates to Spanish
