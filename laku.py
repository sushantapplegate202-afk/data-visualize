from tkinter import filedialog, messagebox
import tkinter as tk  # Import tk explicitly

root = tk.Tk()  # Fixed: lowercase tk, uppercase Tk()
root.title("dockyard ka Text_Editor")
root.geometry("800x800")


#function in scripting
text=tk.Text(
  root,
  wrap=tk.WORD,
  font=("Helvetica",20)
)

text.pack(expand=True,fill=tk.BOTH)

def new_file():
  text.delete(1.0,tk.END)

def open_file():
  #file open dialogue bahi
  file_path=filedialog.askopenfilename(
    defaultextension=".txt",
    filetypes=[("text file","*.txt")]

  )

  if file_path:
    #open selseted menu  file
    with open(file_path, encoding="UTF-8") as file:
      text.delete(1.0,tk.END)
      text.insert(tk.END,file.read())

#now saving of files
def save_file():
  #dilogue for saving a file
  file_path=filedialog.asksaveasfilename(
    defaultextension=".txt",
    filetypes=[("text file","*.txt")]

  )

  if file_path:
    with open(file_path,"w") as file:
      file.write(text.get(1.0,tk.END))



messagebox.showinfo("info","apka file good way me saved ho chuka hai bhai!")      
#menu class creation bhai
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)

#now set up inside menu class like something i way
menu.add_cascade(label="file",menu=file_menu)
menu.add_cascade(label="help",menu=file_menu)
file_menu.add_cascade(label="new",command=new_file)
file_menu.add_cascade(label="open",command=open_file)
file_menu.add_cascade(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_cascade(label="exit",command=root.quit)


    














# Start point of my dockyard text editor software bhai
root.mainloop()
