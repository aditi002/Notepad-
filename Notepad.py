import tkinter as tk
from tkinter import ttk
from tkinter import font, filedialog, messagebox
import os
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("800x600")
root.title("My NotePad")
root.iconbitmap("C:/Users/ACER/Desktop/notepad.ico")

main_menu = tk.Menu()
new = Image.open("C:/Users/ACER/Desktop/new.png")
renew = new.resize((20, 20), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(renew)
open = Image.open("C:/Users/ACER/Desktop/open.png")
reopen = open.resize((20, 20), Image.ANTIALIAS)
open_pic = ImageTk.PhotoImage(reopen)
save = Image.open("C:/Users/ACER/Desktop/save.png")
resave = save.resize((20, 20), Image.ANTIALIAS)
save_pic = ImageTk.PhotoImage(resave)
saveas = Image.open("C:/Users/ACER/Desktop/save as.png")
resaveas = saveas.resize((20, 20), Image.ANTIALIAS)
saveas_pic = ImageTk.PhotoImage(resaveas)

exit = Image.open("C:/Users/ACER/Desktop/exit.png")
reexit = exit.resize((20, 20), Image.ANTIALIAS)
exit_pic = ImageTk.PhotoImage(reexit)

copy = Image.open("C:/Users/ACER/Desktop/copy.png")
recopy = copy.resize((20, 20), Image.ANTIALIAS)
copy_pic = ImageTk.PhotoImage(recopy)
paste = Image.open("C:/Users/ACER/Desktop/paste.png")
repaste = paste.resize((20, 20), Image.ANTIALIAS)
paste_pic = ImageTk.PhotoImage(repaste)
cut = Image.open("C:/Users/ACER/Desktop/cut.png")
recut = cut.resize((20, 20), Image.ANTIALIAS)
cut_pic = ImageTk.PhotoImage(recut)
clear = Image.open("C:/Users/ACER/Desktop/clear.png")
reclear = clear.resize((20, 20), Image.ANTIALIAS)
clear_pic = ImageTk.PhotoImage(reclear)

tool = Image.open("C:/Users/ACER/Desktop/tool bar.png")
retool = tool.resize((20, 20), Image.ANTIALIAS)
tool_pic = ImageTk.PhotoImage(retool)
status = Image.open("C:/Users/ACER/Desktop/status bar.png")
restatus = status.resize((20, 20), Image.ANTIALIAS)
status_pic = ImageTk.PhotoImage(restatus)



bold = Image.open("C:/Users/ACER/Desktop/bold.png")
rebold = bold.resize((20, 20), Image.ANTIALIAS)
bold_pic = ImageTk.PhotoImage(rebold)
italic = Image.open("C:/Users/ACER/Desktop/italic.png")
reitalic = italic.resize((20, 20), Image.ANTIALIAS)
italic_pic = ImageTk.PhotoImage(reitalic)

left = Image.open("C:/Users/ACER/Desktop/left.png")
releft = left.resize((20, 20), Image.ANTIALIAS)
left_pic = ImageTk.PhotoImage(releft)
centre = Image.open("C:/Users/ACER/Desktop/centre.png")
recentre = centre.resize((20, 20), Image.ANTIALIAS)
centre_pic = ImageTk.PhotoImage(recentre)
right = Image.open("C:/Users/ACER/Desktop/right.png")
reright = right.resize((20, 20), Image.ANTIALIAS)
right_pic = ImageTk.PhotoImage(reright)

file = tk.Menu(main_menu, tearoff=False)
file1 = tk.Menu(main_menu, tearoff=False)

file3 = tk.Menu(main_menu, tearoff=False)
file2 = tk.Menu(main_menu, tearoff=False)


main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=file1)
main_menu.add_cascade(label="View", menu=file3)

main_menu.add_cascade(label="Exit", menu=file2)



file1.add_command(label="Copy", image=copy_pic, compound=tk.LEFT,
                  command=lambda: Text_editor.event_generate("<Control c>"))
file1.add_command(label="Paste", image=paste_pic, compound=tk.LEFT,
                  command=lambda: Text_editor.event_generate("<Control v>"))
file1.add_command(label="Cut", image=cut_pic, compound=tk.LEFT,
                  command=lambda: Text_editor.event_generate("<Control x>"))
file1.add_command(label="Clear", image=clear_pic, compound=tk.LEFT, command=lambda: Text_editor.delete(1.0, tk.END))

show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_label.pack_forget()
        show_toolbar = False
    else:
        Text_editor.pack_forget()
        statusbar.pack_forget()
        tool_label.pack(side=tk.TOP, fill=tk.X)
        Text_editor.pack(fill=tk.BOTH, expand=True)
        statusbar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        statusbar.pack_forget()
        show_status_bar = False
    else:
        statusbar.pack(side=tk.BOTTOM)
        show_status_bar = True


file3.add_checkbutton(label="Toolbar", image=tool_pic, onvalue=True, offvalue=0, variable=show_toolbar,
                      compound=tk.LEFT, command=hide_toolbar)
file3.add_checkbutton(label="Statusbar", image=status_pic, onvalue=True, offvalue=0, variable=show_status_bar,
                      compound=tk.LEFT, command=hide_statusbar)

tool_label = ttk.Label(root)
tool_label.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_label, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5, pady=5)

size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_label, width=20, textvariable=size_variable, state="readonly")
font_size["values"] = tuple(range(8, 100, 2))
font_size.current(2)
font_size.grid(row=0, column=1, padx=5)




bold_btn = ttk.Button(tool_label, image=bold_pic)
bold_btn.grid(row=0, column=2, padx=5)
italic_btn = ttk.Button(tool_label, image=italic_pic)
italic_btn.grid(row=0, column=3, padx=5)

left_btn = ttk.Button(tool_label, image=left_pic)
left_btn.grid(row=0, column=4, padx=5)
centre_btn = ttk.Button(tool_label, image=centre_pic)
centre_btn.grid(row=0, column=5, padx=5)
right_btn = ttk.Button(tool_label, image=right_pic)
right_btn.grid(row=0, column=6, padx=5)

Text_editor = tk.Text(root)
Text_editor.config(wrap="word", relief=tk.FLAT)

scrollbar = tk.Scrollbar(root)
Text_editor.focus_set()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
Text_editor.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=Text_editor.yview)
Text_editor.config(yscrollcommand=scrollbar.set)

statusbar = ttk.Label(root, text="Status Bar")
statusbar.pack(side=tk.BOTTOM)

textchange = False


def change_word(event=None):
    global textchange
    if Text_editor.edit_modified():
        textchange = True
        word = len(Text_editor.get(1.0, "end-1c").split())
        character = len(Text_editor.get(1.0, "end-1c").replace("", ""))
        statusbar.config(text=f"character :{character} word :{word}")
    Text_editor.edit_modified(False)


Text_editor.bind("<<Modified>>", change_word)

font_before = "Arial"
font_size_before = 12


def change_font(root):
    global font_before
    font_before = font_family.get()
    Text_editor.configure(font=(font_before, font_size_before))


def change_size(root):
    global font_size_before
    font_size_before = size_variable.get()
    Text_editor.configure(font=(font_before, font_size_before))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)


def bold():
    text_get = tk.font.Font(font=Text_editor["font"])
    if text_get.actual()["weight"] == "normal":
        Text_editor.configure(font=(font_before, font_size_before, "bold"))
    else:
        Text_editor.configure(font=(font_before, font_size_before, "normal"))


bold_btn.configure(command=bold)


def italic():
    text_get = tk.font.Font(font=Text_editor["font"])
    if text_get.actual()["slant"] == "roman":
        Text_editor.configure(font=(font_before, font_size_before, "italic"))
    else:
        Text_editor.configure(font=(font_before, font_size_before, "roman"))


italic_btn.configure(command=italic)


def align_left():
    text_get_all = Text_editor.get(1.0, "end")
    Text_editor.tag_config("left", justify=tk.LEFT)
    Text_editor.delete(1.0, tk.END)
    Text_editor.insert(tk.INSERT, text_get_all, "left")


left_btn.configure(command=align_left)


def align_center():
    text_get_all = Text_editor.get(1.0, "end")
    Text_editor.tag_config("center", justify=tk.CENTER)
    Text_editor.delete(1.0, tk.END)
    Text_editor.insert(tk.INSERT, text_get_all, "center")


centre_btn.configure(command=align_center)


def align_right():
    text_get_all = Text_editor.get(1.0, "end")
    Text_editor.tag_config("right", justify=tk.RIGHT)
    Text_editor.delete(1.0, tk.END)
    Text_editor.insert(tk.INSERT, text_get_all, "right")


right_btn.configure(command=align_right)

text_url = " "


def new_file(event=None):
    global text_url
    Text_editor.delete(1.0, tk.END)


file.add_command(label="New", image=new_pic, compound=tk.LEFT, command=new_file)


def open_file():
    global text_url
    text_url = filedialog.askopenfilename(title="select file",defaultextension=".txt", filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
    try:
        with open(text_url  ,"r") as for_read:
            Text_editor.delete(1.0, tk.END)
            Text_editor.insert(1.0, for_read.read())
    except FileNotFoundError:
        pass
    else:
        pass
    root.title(os.path.basename(text_url))


file.add_command(label="Open", image=open_pic, compound=tk.LEFT, command=open_file)


def save_file(event=None):
    global text_url
    try:
        if text_url:
            content = str(Text_editor.get(1.0, tk.END))
            with open(text_url , "w", encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode="w", defaultextention="txt",
                                                filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
            content2 = Text_editor.get(1.0, tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return


file.add_command(label="Save", image=save_pic, compound=tk.LEFT, command=save_file)


def save_as_file(event=None):
    global text_url
    try:
        content = Text_editor.get(1.0, tk.END)
        text_url = filedialog.asksaveasfile(mode="w", defaultextention="txt",
                                            filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
        text_url.write(content)
        text_url.close()
    except:
        return


file.add_command(label="Save as", image=saveas_pic, compound=tk.LEFT, command=save_as_file)


def exit_file(event=None):
    global text_change
    global text_url
    try:
        if text_change:
            msgbox = messagebox.askyesnocancel("warning", "Do you want to save this file")
            if msgbox is True:
                if text_url:
                    content = Text_editor.get(1.0, tk.END)
                    with open(text_url, "w", encoding="utf-8") as for_read:
                        for_read.write(content)
                        root.destroy()
                else:
                    content2 = Text_editor.get(1.0, tk.END)
                    text_url = filedialog.asksaveasfile(mode="w", defaultextention="txt",
                                                        filetypes=(("Text file", "*.txt"), ("All files", "*.*")))
                    text_url.write(content2)
                    text_url.close()
                    root.destroy()
            elif msgbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


file2.add_command(label="exit", image=exit_pic, compound=tk.LEFT, command=exit_file)

root.config(menu=main_menu)

root.mainloop()
