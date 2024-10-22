import ttkbootstrap as tk
from ttkbootstrap.constants import *
import codecs
filename = 'data.txt'

def read_file():
    f = codecs.open(filename, 'r', 'utf-8')
    lines = ''
    for line in f:
        lines += line
    f.close()
    return lines

def write_text(txt):
    f = codecs.open(filename, 'w', 'utf-8')
    f.write(txt)

def on_close():
    text = text_frame.get("1.0", END+"-1c")
    write_text(text)
    app.destroy()

app = tk.Window()

app.geometry(f"{app.winfo_screenwidth() // 4}x{app.winfo_screenheight() // 2}+{app.winfo_screenwidth() - (app.winfo_screenwidth() // 4)}+0")
app.overrideredirect(True)
button=tk.Button(app, text="Click to close", command=lambda: on_close(), bootstyle="light-outline")
button.pack(fill=tk.X)
text_frame = tk.Text(app, font=("", 14), bg="white", fg="black", wrap=tk.WORD)
text_frame.insert(tk.END, read_file())
text_frame.pack(fill=tk.BOTH, expand=FALSE, padx=10, pady=10)

app.mainloop()
