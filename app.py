import sqlite3

import tkinter as tk
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk

class Database:
	def __init__(self, dbname):
		self.dbname = dbname

	def create_conn(self):
		try:
			conn = sqlite3.connect(self.dbname)
		except sqlite3.Error as e:
			conn = None
		return conn

	def read_all(self):
		conn = self.create_conn()
		if conn is not None:
			sql = "SELECT * FROM todo;"
			cursor = conn.cursor()
			cursor.execute(sql)
			rows = cursor.fetchall()
			return rows

	def create(self, todo):
		conn = self.create_conn()
		sql = "INSERT INTO todo(text) VALUES(?)"
		if conn is not None:
			cursor = conn.cursor()
			cursor.execute(sql, (todo,))
			conn.commit()
			return cursor.lastrowid

	def delete(self, todo_id):
		conn = self.create_conn()
		if conn is not None:
			sql = "DELETE FROM todo WHERE id=?"
			cursor = conn.cursor()
			cursor.execute(sql, (todo_id,))
			conn.commit()


	def update(self):
		pass


class Todo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		self.db = Database(dbname="todo.db")
		self.check_var = tk.BooleanVar()
		self.todo_id = kwargs.get("todo_id")
		self.todo_text = kwargs.get("todo_text")

		# images
		self.delete_img =  ImageTk.PhotoImage(Image.open("./images/001-delete.png"))
		self.update_img =  ImageTk.PhotoImage(Image.open("./images/002-pencil.png"))
		# A todo
		self.check = ttk.Checkbutton(self, variable=self.check_var)
		self.check["command"] = self.on_check
		self.todo_entry = ttk.Entry(self)
		self.todo_entry.insert(0, self.todo_text)
		self.delete = ttk.Button(self, text="Delete", image=self.delete_img)
		self.delete["command"] = self.on_delete
		# Grid widgets
		self.check.grid(row=0, column=0)
		self.todo_entry.grid(row=0, column=1, stick="ew")
		self.delete.grid(row=0, column=3)

		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=2)

		# binds
		self.todo_entry.bind("<KeyPress>", self.on_keypress)
		# responsive shits
		self.columnconfigure(1, weight=10)

	def on_check(self):
		# if checkbutton check cross over todo_text entry
		if self.check_var.get():
			self.todo_text["font"] = font.Font(overstrike=1, slant="italic")
		else:
			self.todo_text["font"] = font.Font(overstrike=0)

	def on_delete(self):
		# get id of the todo 
		self.db.delete(self.todo_id)

		self.forget()

	def on_keypress(self, *args):
		print("you typed!!")
		# update db when type something.


class AddTodo(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master)
		self.db = Database(dbname="todo.db")
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
		todo.pack(padx=5, fill=tk.X)
		# adding to do to the database
		conn = self.db.create_conn()
		if conn is not None:
			todo_id = self.db.create(self.todo_text.get())
			print(todo_id)

		# clear todo_text entry after adding the todo
		self.todo_text.delete(0, tk.END)


class TodoList(ttk.Frame):
	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		# self.message = ttk.Label(self, text="List of all todo's")
		# self.message.pack(expand=True, fill=tk.BOTH)
		self.db = Database(dbname="todo.db")
		self.create_todos()

	def create_todos(self):
		all_todo = self.db.read_all()
		for todo in all_todo:
			todo_frame = Todo(self, todo_text=todo[1], todo_id=todo[0])
			todo_frame.pack(padx=5, fill=tk.X)


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
