import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk


class Todo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		self.check_var = tk.BooleanVar()
		self.style = ttk.Style()
		self.style.configure("done.TEntry", font='helvetica 24', foreground='red', padding=10)
		# images
		self.delete_img =  ImageTk.PhotoImage(Image.open("./images/001-delete.png"))
		self.update_img =  ImageTk.PhotoImage(Image.open("./images/002-pencil.png"))
		# A todo
		self.check = ttk.Checkbutton(self, variable=self.check_var)
		self.check["command"] = self.on_check
		self.todo_text = ttk.Entry(self)
		self.todo_text.insert(0, kwargs.get("todo_text"))
		self.update = ttk.Button(self, text="Update", image=self.update_img)
		self.delete = ttk.Button(self, text="Delete", image=self.delete_img)
		self.delete["command"] = self.on_delete
		# Grid widgets
		self.check.grid(row=0, column=0)
		self.todo_text.grid(row=0, column=1, stick="ew")
		self.update.grid(row=0, column=2)
		self.delete.grid(row=0, column=3)

		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)

		# responsive shits
		self.columnconfigure(1, weight=10)

	def on_check(self):
		# if checkbutton check cross over todo_text entry
		if self.check_var.get():
			self.todo_text["font"] = font.Font(overstrike=1, slant="italic")
		else:
			self.todo_text["font"] = font.Font(overstrike=0)

	def on_update(self):
		pass

	def on_delete(self):
		self.forget()



class AddTodo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		self.todo_list = kwargs.get("todo_list_frame")
		self.add_img =  ImageTk.PhotoImage(Image.open("./images/003-add.png"))
		# widgets
		self.todo_text = ttk.Entry(self)
		self.add_todo = ttk.Button(self, text="Add", command=self.create_todo, image=self.add_img)
		# widget config
		self.todo_text.focus()
		# pack widgets
		self.todo_text.grid(row=0, column=0, stick="wesn", padx=(0, 5))
		self.add_todo.grid(row=0, column=1, stick="wesn")
		# widget bind
		self.todo_text.bind("<Return>", self.create_todo)
		# responsive
		self.columnconfigure(0, weight=9)
		self.columnconfigure(1, weight=1)
		self.rowconfigure(0, weight=1)

	def create_todo(self, *event):
		todo = Todo(self.todo_list, todo_text=self.todo_text.get())
		todo.configure(relief=tk.GROOVE)
		todo.pack(padx=5, pady=5, fill=tk.X)
		# clear todo_text entry after adding the todo
		self.todo_text.delete(0, tk.END)


class TodoList(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		# self.message = ttk.Label(self, text="List of all todo's")
		# self.message.pack(expand=True, fill=tk.BOTH)



class MainFrame(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		# todo list
		todo_list_frame = TodoList(self, padding="3 3 12 12", relief='sunken')
		todo_list_frame.grid(row=0, column=0, stick="wesn")
		# Make to do part
		todo_frame = AddTodo(self, todo_list_frame=todo_list_frame)
		todo_frame.grid(row=1, column=0, stick="wesn", padx=5, pady=5)
		# responsive stuff
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=15)
		self.rowconfigure(1, weight=1)

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title("Py To Do List")
		self.geometry("500x500")
		mainframe = MainFrame(self)
		mainframe.pack(fill=tk.BOTH, expand=True)
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)


def main():
	app = App()
	# app.title = "Py To Do"
	app.mainloop()


if __name__ == "__main__":
	main()
