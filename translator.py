import tkinter as tk 
from tkinter import ttk , messagebox
from deep_translator import GoogleTranslator

# Language mapping
lang_dict = {
    "Auto Detect": "auto",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Chinese (Simplified)": "zh-cn",
    "Arabic": "ar",
    "Russian": "ru",
    "Japanese": "ja",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Korean": "ko",
    "Hindi": "hi",
    "Turkish": "tr",
    "Swedish": "sv",
    "Greek": "el",
    "Hebrew": "he",
    "Polish": "pl",
    "Danish": "da",
    "Finnish": "fi",
    "Czech": "cs",
    "Hungarian": "hu",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Malay": "ms"
}

#function to perform translation 
def translate_text():
    try:
        source_lang = lang_dict.get(source_lang_combo.get(), "auto")
        target_lang = lang_dict.get(target_lang_combo.get(), "en")
        text = input_text.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return
        
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")
        

#GUI setup
root = tk.Tk()
root.title("Language Translator" )
root.geometry("800x650")

style = ttk.Style(root)
style.theme_use("xpnative")

#Dropdown options
lang_list =list(lang_dict.keys())

#Source language dropdown
source_lang_label = ttk.Label(root, text="Source Language:", foreground="#4285F9" , background="#FFFFFF" , font=("Sans serif", 10))
source_lang_label.pack(pady=(10, 0))
source_lang_label.pack()

source_lang_combo = ttk.Combobox(root, values=lang_list, width=20 , foreground="black" , background="white", font=("Sans serif",9))
source_lang_combo.pack()
source_lang_combo.set("Auto Detect")

#Text input area
input_label = ttk.Label(root, text="Input Text:" , foreground="#4285F9" , background="#FFFFFF" , font=("Sans serif", 9))
input_label.pack()

input_text = tk.Text(root, height=10, width=80 , foreground="black" , background="#FFFFFF" , font=("Sans serif", 10) , insertbackground="white", wrap="word")
input_text.pack()
input_text.pack(pady=(0, 10))

#Target language dropdown
target_lang_label = ttk.Label(root, text="Target Language:", foreground="#4285F9" , background="#FFFFFF" , font=("Sans serif", 10))
target_lang_label.pack()

target_lang_combo = ttk.Combobox(root, value=lang_list, width=20 , font=("Sans serif",9))
target_lang_combo.pack()
target_lang_combo.set("English")

#Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text , foreground="#4285F9", background="#FFFFFF", activebackground="#4285F4")
translate_button.pack(pady=10)

#Output text area
output_label = ttk.Label(root, text="Translated Text:"  , foreground="#4285F9" , background="#FFFFFF" , font=("Sans serif", 9))
output_label.pack()

output_text = tk.Text(root, height=10, width=80 , foreground="black" , background="#FFFFFF" , font=("Sans serif", 10) , insertbackground="white", wrap="word")
output_text.pack()



#run the GUI
root.mainloop()