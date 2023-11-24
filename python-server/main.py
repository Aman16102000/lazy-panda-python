import pyautogui
import time

from flask import Flask

app=Flask(__name__)



@app.route("/")
def press_space():
    pyautogui.press('space')
    return "Hi"     