from tkinter import *
from PIL import Image, ImageDraw
import PIL
import pickle
import img_processing
import time


# задание размеров окна
WIDTH, HEIGHT = 400, 400
CENTER = WIDTH // 2

BLACK = (0, 0, 0)


# класс-графическая оболочка
class PaintGUI:

    def __init__(self):

        self.flag = 0
        self.last_update_time = time.time()

        # создание окна
        self.root = Tk()
        self.root.configure(background='white')
        self.root.title('MNIST GUI')

        # параметры кисти для рисования
        self.brush_width = 6
        self.current_color = '#ffffff'

        # создание области для рисования и бинд рисования на нажатие мыши
        self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg='black')
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)

        # само изображение для рисования и объект для рисования
        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), BLACK)
        self.draw = ImageDraw.Draw(self.image)

        # рамка для кнопок и вывода результата
        self.frame1 = Frame(self.root)
        self.frame1.pack(fill=X)

        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame1.columnconfigure(2, weight=1)

        # задание кнопки Clear
        self.clear_btn = Button(self.frame1, text='Clear', command=self.clear)
        self.clear_btn.grid(row=0, column=1, sticky=W+E)

        # задание кнопки Predict
        self.predict_btn = Button(self.frame1, text='Predict', command=self.predict_num)
        self.predict_btn.grid(row=1, column=1, sticky=W + E)

        # задание кнопки увеличения размера кисти
        self.bplus_btn = Button(self.frame1, text='B+', command=self.brush_plus)
        self.bplus_btn.grid(row=0, column=0, sticky=W+E)

        # задание кнопки уменьшения размера кисти
        self.bminus_btn = Button(self.frame1, text='B-', command=self.brush_minus)
        self.bminus_btn.grid(row=1, column=0, sticky=W+E)

        # задание лейбла для вывода результата
        self.label = Label(self.frame1, text='[  ]', font=("Arial", 30))
        self.label.grid(row=0, column=2, rowspan=2, sticky=W+E)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes("-topmost", True)

        while True:
            self.root.update_idletasks()
            self.root.update()

            # через сколько после рисования секунд угадывать значение
            cut = round(time.time() - self.last_update_time)
            if (cut == 2) & (self.flag):
                self.predict_num()
                self.flag = 0


    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.cnv.create_rectangle(x1, y1, x2, y2, outline='white', fill='white', width=self.brush_width)
        self.draw.rectangle([x1, y1, x2+self.brush_width, y2+self.brush_width], outline='white', fill='white', width=self.brush_width )
        self.last_update_time = time.time()

        if ~self.flag:
            self.flag = 1
    def clear(self):
        self.cnv.delete("all")
        self.draw.rectangle([0,0, 1000, 1000], fill='black')
        self.label.config(text='[  ]')
        self.flag = 0

    def predict_num(self):
        # обработка изображения перед предстказанием
        resized_end = img_processing.processing(self.image)

        # предсказание и вывод результата в label
        lst = clf.predict(resized_end)
        self.label.config(text=lst)
        self.flag = 0
        #resized.save('resized.png')

    def brush_plus(self):
        self.brush_width += 2

    def brush_minus(self):
        if self.brush_width > 2:
            self.brush_width -= 2

    def on_closing(self):
        self.root.destroy()
        exit(0)

# загрузка ранее обученной модели
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

start_time = time.time()
# запуск граф.интерфейса
PaintGUI()
