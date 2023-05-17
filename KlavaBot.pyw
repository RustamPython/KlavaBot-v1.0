import keyboard
import mouse
import time
import random
import pyperclip
import tkinter as tk
from tkinter import ttk
import pyautogui
from win32api import GetSystemMetrics
import win32api

r = tk.Tk()
r.title('КлаваБот')
r.resizable(False, False)

rusLet = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ"
numbers = "0123456789."
specsym = ".,!\"№;%:?*()_+/-=`~[]{}\\|"
conv1 = "aoc,." + chr(171) + chr(187) + chr(8212) + chr(8211)
conv2 = "аос,.\"\"--"
prm = 0
nrm = 0
zrm = 0
mpr = 0
mom = tk.BooleanVar()
mom.set(False)

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)


def show_all():
    global sl
    global sn
    global ss
    global mg
    global po
    global prm
    global nrm
    global zrm
    global mom
    global mpr
    prm = sl.get()
    nrm = sn.get()
    zrm = ss.get()
    mpr = po.get()
    mom = mom.get()
    print(prm, nrm, zrm, mom, mpr)
    return [prm, nrm, zrm, mpr]


def pech(zn):
    if zn in rusLet:
        keyboard.write(zn)
        if not (mom):
            time.sleep(60 / prm / 1.175 + random.randint(-20, 20) / prm)
    elif zn in numbers:
        keyboard.write(zn)
        if not (mom):
            time.sleep(60 / nrm / 1.175 + random.randint(-20, 20) / nrm)
    elif zn in specsym:
        keyboard.write(zn)
        if not (mom):
            time.sleep(60 / zrm / 1.175 + random.randint(-20, 20) / zrm)
    else:
        if zn in conv1:
            pech(conv2[conv1.index(zn)])


def write(text):
    i = 0
    while i < len(text):
        keyboard.release('ctrl')
        if mpr == 0 or random.randint(0, int(len(text) / mpr / 2)) != 0:
            if text[i] != " ":
                pech(text[i])
                i += 1
            else:
                keyboard.press("\u0020")
                time.sleep(60 / prm + random.randint(-20, 20) / prm)
                keyboard.release("\u0020")
                i += 1
        else:
            if text[i] in rusLet:
                a = random.randint(1, 3)
                if i + a < len(text) - 12:
                    keyboard.write(text[i + a])
                    keyboard.press('backspace')
                    keyboard.release('backspace')
                    if not(mom):
                        time.sleep(60 / prm + random.randint(-3, 3) / prm)


def run():
    global prm
    global nrm
    global zrm
    global mpr
    global mom
    r.withdraw()
    for i in show_all():
        for j in range(len(i)):
            if not(i[j] in numbers):
                r.deiconify()
                mom = tk.BooleanVar()
                err = ttk.Label(text="ОШИБКА!", foreground='red', font='Georgia 25')
                err.pack(anchor='nw')
                return 1
    win32api.LoadKeyboardLayout('00000409', 1)
    if prm != '' and nrm != '' and zrm != '' and mpr != '':
        prm = int(prm)
        nrm = int(nrm)
        zrm = int(zrm)
        mpr = float(mpr)
    else:
        r.deiconify()
        err = ttk.Label(text="ОШИБКА!", foreground='red', font='Georgia 25')
        return 1
    #print(type(prm), type(nrm), type(zrm), type(mpr))
    keyboard.wait('alt+k+b')
    keyboard.release('alt+k+b')
    pyperclip.copy("Текст скрыт до начала игры")
    mouse.wheel(10000)
    mouse.move(350 * w / 1920, 90 * h / 1080 + (60 * h / 1080 * int(pyautogui.pixel(mouse.get_position()[0], 100)[0] == pyautogui.pixel(mouse.get_position()[0], 100)[1] == pyautogui.pixel(mouse.get_position()[0], 100)[2])) + 270 * h / 1080)
    i = mouse.get_position()[1]
    while pyautogui.pixel(mouse.get_position()[0], i) != (235, 235, 235):
        i += 1
    mouse.move(mouse.get_position()[0], i + 4 * h / 1080)
    while ("Текст скрыт до начала игры" in pyperclip.paste()):
        mouse.wheel(10000)
        time.sleep(0.01)
        mouse.click("left")
        time.sleep(0.03)
        mouse.click("left")
        time.sleep(0.03)
        mouse.press("left")
        time.sleep(0.03)
        keyboard.press("ctrl+c")
        keyboard.release("ctrl+c")
        mouse.release('left')
    time.sleep(2.1)
    i = mouse.get_position()[1]
    while pyautogui.pixel(mouse.get_position()[0], i) != (255, 255, 255):
        mouse.wheel(10000)
        i += 1
    mouse.move(mouse.get_position()[0], i + 5, True)
    mouse.click('left')
    texta = pyperclip.paste()
    for i in range(len(texta)):
        print(ord(texta[i]), "-", texta[i])
    time.sleep(0.1)
    write(texta)
    r.quit()
    exit(0)


gr = ttk.Label(text="Привет! Я КлаваБот! Мои требования: сделай масштаб страницы 100%! Я пока так не умею  :(   \n")
gr.pack(anchor='nw')


comment = ttk.Label(text="После запуска нужно нажать alt+k+b, чтобы я начал копирование текста,\nэто можно делать еще \
 до начала заезда. А ниже можно настроить меня.  :-)\n")
comment.pack(anchor='nw')

esl = ttk.Label(text="Введи скорость набора букв (в зн./мин)")
esl.pack(anchor='nw')

sl = ttk.Entry()
sl.pack(anchor='nw', padx=3)

esn = ttk.Label(text="Введи скорость набора цифр (также в зн./мин)")
esn.pack(anchor='nw')

sn = ttk.Entry()
sn.pack(anchor='nw', padx=3)

ess = ttk.Label(text="Введи скорость набора знаков перпенания и прочих специальных символов")
ess.pack(anchor='nw')

ss = ttk.Entry()
ss.pack(anchor='nw', padx=3)

epo = ttk.Label(text="Введи процент ошибок")
epo.pack(anchor='nw')

po = ttk.Entry()
po.pack(anchor='nw', padx=3)

pus1 = ttk.Label(text="")
pus1.pack(anchor='nw')

mg = ttk.Checkbutton(text='Набирать текст моментально (в таком случае только у пробелов будет задержка)',
                    variable=mom)
mg.pack(anchor='nw')

pus2 = ttk.Label(text="")
pus2.pack(anchor='nw')

run = ttk.Button(text='Запустить!', command=run)
run.pack(anchor='se')

r.mainloop()
