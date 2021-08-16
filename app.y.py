import tkinter as tk
from tkinter import ttk



class AddTodo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		# widgets
		self.todo = ttk.Entry(self)
		self.add_todo = ttk.Button(self, text="Add", command=self.create_todo)
		# widget config
		self.todo.focus()
		# pack widgets
		self.todo.pack(side=tk.LEFT)
		self.add_todo.pack(side=tk.RIGHT)

	def create_todo(self):
		print(self.todo.get())

class TodoList(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.message = ttk.Label(self, text="List of all todo's")
		self.message.pack(expand=True, fill=tk.BOTH)



class MainFrame(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)

		# Make to do part
		todo_frame = AddTodo(self)
		todo_frame.pack(expand=True, fill=tk.BOTH)

		# todo list
		todo_list_frame = TodoList(self, padding="3 3 12 120", relief='sunken')
		todo_list_frame.pack(expand=True, fill=tk.BOTH)


class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.title("Py To Do List")
		mainframe = MainFrame(self)
		mainframe.pack(fill=tk.BOTH, expand=True)


def main():
	app = App()
	# app.title = "Py To Do"
	app.mainloop()


if __name__ == "__main__":
	main()
