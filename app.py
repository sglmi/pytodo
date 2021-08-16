import tkinter as tk
from tkinter import ttk

class Todo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		self.check_var = tk.BooleanVar()
		# A todo
		self.check = ttk.Checkbutton(self, variable=self.check_var)
		self.todo_text = ttk.Entry(self)
		self.todo_text.insert(0, kwargs.get("todo_text"))
		self.update = ttk.Button(self, text="Update")
		self.delete = ttk.Button(self, text="Delete")
		# Grid widgets
		self.check.grid(row=0, column=0)
		self.todo_text.grid(row=0, column=1)
		self.update.grid(row=0, column=2)
		self.delete.grid(row=0, column=3)

	def on_check(self):
		pass

	def on_update(self):
		pass

	def on_delete(self):
		pass



class AddTodo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		self.todo_list = kwargs.get("todo_list_frame")
		# widgets
		self.todo_text = ttk.Entry(self)
		self.add_todo = ttk.Button(self, text="Add", command=self.create_todo)
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
		todo.pack()
		# clear todo_text entry after adding the todo
		self.todo_text.delete(0, tk.END)


class TodoList(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.message = ttk.Label(self, text="List of all todo's")
		self.message.pack(expand=True, fill=tk.BOTH)



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
