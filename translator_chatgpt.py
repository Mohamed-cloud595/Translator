import tkinter as tk 
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Language mapping dictionary
lang_dict = {
    "Auto Detect": "auto", "English": "en", "French": "fr", "Spanish": "es", "German": "de", 
    "Italian": "it", "Chinese (Simplified)": "zh-cn", "Arabic": "ar", "Russian": "ru", 
    "Japanese": "ja", "Portuguese": "pt", "Dutch": "nl", "Korean": "ko", "Hindi": "hi", 
    "Turkish": "tr", "Swedish": "sv", "Greek": "el", "Hebrew": "he", "Polish": "pl", 
    "Danish": "da", "Finnish": "fi", "Czech": "cs", "Hungarian": "hu", "Thai": "th", 
    "Vietnamese": "vi", "Indonesian": "id", "Malay": "ms"
}

# Function to perform translation
def translate_text():
    try:
        source_lang = lang_dict.get(source_lang_combo.get(), "auto")
        target_lang = lang_dict.get(target_lang_combo.get(), "en")
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        # Translation logic
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Translation Error", f"Failed to translate: {e}")

# Function to clear input/output text
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("800x650")
root.configure(bg="#f4f4f4")

# Styling with ttk
style = ttk.Style(root)
style.theme_use("xpnative")

# Dropdown options
lang_list = list(lang_dict.keys())

# Source language selection
source_lang_label = ttk.Label(root, text="Source Language:", foreground="#4285F9", background="#f4f4f4", font=("Arial", 10))
source_lang_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

source_lang_combo = ttk.Combobox(root, values=lang_list, width=20, font=("Arial", 9))
source_lang_combo.grid(row=0, column=1, padx=10, pady=5, sticky="w")
source_lang_combo.set("Auto Detect")

# Input Text Label & Area
input_label = ttk.Label(root, text="Input Text:", foreground="#4285F9", background="#f4f4f4", font=("Arial", 10))
input_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

input_text = tk.Text(root, height=10, width=80, font=("Arial", 10), wrap="word", bg="#FFFFFF", fg="black")
input_text.grid(row=1, column=1, padx=10, pady=5)

# Target Language selection
target_lang_label = ttk.Label(root, text="Target Language:", foreground="#4285F9", background="#f4f4f4", font=("Arial", 10))
target_lang_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

target_lang_combo = ttk.Combobox(root, values=lang_list, width=20, font=("Arial", 9))
target_lang_combo.grid(row=2, column=1, padx=10, pady=5, sticky="w")
target_lang_combo.set("English")

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, foreground="#4285F9", background="#FFFFFF", font=("Arial", 10), relief="solid")
translate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_text, foreground="#4285F9", background="#FFFFFF", font=("Arial", 10), relief="solid")
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

# Output Text Label & Area
output_label = ttk.Label(root, text="Translated Text:", foreground="#4285F9", background="#f4f4f4", font=("Arial", 10))
output_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

output_text = tk.Text(root, height=10, width=80, font=("Arial", 10), wrap="word", bg="#f9f9f9", fg="black")
output_text.grid(row=5, column=1, padx=10, pady=5)

# Start the GUI mainloop
root.mainloop()
