import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import webbrowser

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.setup_app()
        self.create_widgets()
        self.setup_layout()
        
    def setup_app(self):
        self.root.title("Professional Language Translator")
        self.root.geometry("900x700")
        self.root.minsize(800, 650)
        self.root.configure(bg="#f5f5f5")
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background="#f5f5f5")
        self.style.configure('TLabel', background="#f5f5f5", font=('Helvetica', 10))
        self.style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'), foreground="#1a73e8")
        self.style.configure('TButton', font=('Helvetica', 10), padding=5)
        self.style.map('TButton', 
                      foreground=[('active', '#ffffff'), ('!disabled', '#1a73e8')],
                      background=[('active', '#1a5cb8'), ('!disabled', '#ffffff')])
        
        # Language mapping
        self.lang_dict = {
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
        
    def create_widgets(self):
        # Header frame
        self.header_frame = ttk.Frame(self.root)
        self.header_label = ttk.Label(
            self.header_frame, 
            text="Professional Language Translator",
            style='Header.TLabel'
        )
        self.credit_label = ttk.Label(
            self.header_frame,
            text="Powered by Google Translate API",
            style='TLabel',
            cursor="hand2",
            foreground="#5f6368"
        )
        self.credit_label.bind("<Button-1>", lambda e: webbrowser.open("https://translate.google.com"))
        
        # Input frame
        self.input_frame = ttk.Frame(self.root)
        
        # Source language
        self.source_lang_label = ttk.Label(
            self.input_frame, 
            text="Source Language:",
            style='TLabel'
        )
        self.source_lang_combo = ttk.Combobox(
            self.input_frame,
            values=list(self.lang_dict.keys()),
            width=25,
            state="readonly",
            font=('Helvetica', 9)
        )
        self.source_lang_combo.set("Auto Detect")
        
        # Input text
        self.input_label = ttk.Label(
            self.input_frame,
            text="Text to Translate:",
            style='TLabel'
        )
        self.input_text = tk.Text(
            self.input_frame,
            height=10,
            width=70,
            wrap="word",
            font=('Helvetica', 10),
            padx=10,
            pady=10,
            highlightthickness=1,
            highlightbackground="#dadce0",
            highlightcolor="#1a73e8"
        )
        
        # Action frame
        self.action_frame = ttk.Frame(self.root)
        
        # Target language
        self.target_lang_label = ttk.Label(
            self.action_frame,
            text="Target Language:",
            style='TLabel'
        )
        self.target_lang_combo = ttk.Combobox(
            self.action_frame,
            values=list(self.lang_dict.keys()),
            width=25,
            state="readonly",
            font=('Helvetica', 9)
        )
        self.target_lang_combo.set("English")
        
        # Translate button
        self.translate_button = ttk.Button(
            self.action_frame,
            text="Translate",
            command=self.translate_text,
            style='TButton'
        )
        
        # Swap button
        self.swap_button = ttk.Button(
            self.action_frame,
            text="↔ Swap Languages",
            command=self.swap_languages,
            style='TButton'
        )
        
        # Output frame
        self.output_frame = ttk.Frame(self.root)
        self.output_label = ttk.Label(
            self.output_frame,
            text="Translated Text:",
            style='TLabel'
        )
        self.output_text = tk.Text(
            self.output_frame,
            height=10,
            width=70,
            wrap="word",
            font=('Helvetica', 10),
            padx=10,
            pady=10,
            highlightthickness=1,
            highlightbackground="#dadce0",
            highlightcolor="#1a73e8"
        )
        
        # Status bar
        self.status_bar = ttk.Label(
            self.root,
            text="Ready",
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=('Helvetica', 9),
            foreground="#5f6368"
        )
        
    def setup_layout(self):
        # Header frame
        self.header_frame.pack(pady=(10, 5), fill=tk.X)
        self.header_label.pack()
        self.credit_label.pack()
        
        # Input frame
        self.input_frame.pack(pady=10, padx=20, fill=tk.X)
        self.source_lang_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.source_lang_combo.grid(row=0, column=1, sticky=tk.W, pady=(0, 5))
        self.input_label.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(10, 5))
        self.input_text.grid(row=2, column=0, columnspan=2)
        
        # Action frame
        self.action_frame.pack(pady=10, padx=20, fill=tk.X)
        self.target_lang_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.target_lang_combo.grid(row=0, column=1, sticky=tk.W, pady=(0, 5))
        self.translate_button.grid(row=1, column=0, pady=10, sticky=tk.E, padx=(0, 10))
        self.swap_button.grid(row=1, column=1, pady=10, sticky=tk.W)
        
        # Output frame
        self.output_frame.pack(pady=10, padx=20, fill=tk.X)
        self.output_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.output_text.grid(row=1, column=0, columnspan=2)
        
        # Status bar
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def translate_text(self):
        try:
            source_lang = self.lang_dict.get(self.source_lang_combo.get(), "auto")
            target_lang = self.lang_dict.get(self.target_lang_combo.get(), "en")
            text = self.input_text.get("1.0", tk.END).strip()
            
            if not text:
                messagebox.showwarning("Warning", "Please enter text to translate.")
                self.status_bar.config(text="Warning: No text to translate")
                return
            
            self.status_bar.config(text="Translating...")
            self.root.update_idletasks()  # Update UI immediately
            
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
            
            self.status_bar.config(text="Translation complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"Translation failed: {e}")
            self.status_bar.config(text=f"Error: {str(e)}")
            
    def swap_languages(self):
        current_source = self.source_lang_combo.get()
        current_target = self.target_lang_combo.get()
        
        # Don't swap if source is "Auto Detect"
        if current_source == "Auto Detect":
            return
            
        self.source_lang_combo.set(current_target)
        self.target_lang_combo.set(current_source)
        
        # Also swap the text content
        input_text = self.input_text.get("1.0", tk.END).strip()
        output_text = self.output_text.get("1.0", tk.END).strip()
        
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        
        if output_text:  # Only swap if there's output text
            self.input_text.insert(tk.END, output_text)
        if input_text:
            self.output_text.insert(tk.END, input_text)
            
        self.status_bar.config(text="Languages swapped")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()