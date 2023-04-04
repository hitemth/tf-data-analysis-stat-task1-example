import pandas as pd
import numpy as np


chat_id = 156287560 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # v = v_0 + at => a = v/10
    error = 31 + np.exp(1)
    a = (x + np.random.normal(0, error, size=len(x))) / 10


    return a.mean() # Ваш ответ
