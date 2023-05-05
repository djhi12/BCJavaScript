import tkinter as tk

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render(self, canvas):
        canvas.delete("all")
        for shape in self.shapes:
            canvas.create_oval(shape.x - shape.radius, shape.y - shape.radius,
                               shape.x + shape.radius, shape.y + shape.radius,
                               fill=shape.color)

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.add_circle)
        self.canvas.bind("<B1-Motion>", self.move_circle)
        self.canvas.bind("<Button-3>", self.remove_circle)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.change_color)
        self.canvas.bind("<Escape>", self.quit)
        self.canvas.create_text(400, 50, text="Click and drag to create circles")
        self.canvas.create_text(400, 70, text="Right-click to remove circles")
        self.canvas.create_text(400, 90, text="Press a key to change the color of the circle")
        self.canvas.create_text(400, 110, text="Press Esc to quit")

        self.canvas_color = "red"

        self.canvas_obj = Canvas(800, 600)

    def run(self):
        self.root.mainloop()

    def add_circle(self, event):
        x = event.x
        y = event.y
        circle = Circle(x, y, 20, self.canvas_color)
        self.canvas_obj.add_shape(circle)
        self.canvas_obj.render(self.canvas)

    def move_circle(self, event):
        x = event.x
        y = event.y
        for shape in self.canvas_obj.shapes:
            if isinstance(shape, Circle):
                if abs(shape.x - x) <= shape.radius and abs(shape.y - y) <= shape.radius:
                    shape.x = x
                    shape.y = y
                    self.canvas_obj.render(self.canvas)
                    break

    def remove_circle(self, event):
        x = event.x
        y = event.y
        for shape in self.canvas_obj.shapes:
            if isinstance(shape, Circle):
                if abs(shape.x - x) <= shape.radius and abs(shape.y - y) <= shape.radius:
                    self.canvas_obj.shapes.remove(shape)
                    self.canvas_obj.render(self.canvas)
                    break

    def change_color(self, event):
        self.canvas_color = "blue" if self.canvas_color == "red" else "red"
        self.canvas.itemconfig(tk.CURRENT, fill=self.canvas_color)
        for shape in self.canvas_obj.shapes:
            if isinstance(shape, Circle):
                if self.canvas.find_withtag(tk.CURRENT) == self.canvas.find_withtag(shape):
                    shape.color = self.canvas_color

    def quit(self, event):
        self.root.quit()

app = App()
app.run()
