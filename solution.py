import pandas as pd
import numpy as np


chat_id = 156287560 # Ваш chat ID, не меняйте название переменной
'''
def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # v = v_0 + at => a = v/10
    error = 31 + np.exp(1)
    a = (x + np.random.normal(0, error, size=len(x))) / 10


    return a.mean() # Ваш ответ
'''


def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # v = v_0 + at => a = v/10
    error_distribution = np.random.exponential(1, size = len(x))
    error_distribution = error_distribution - 31
    a = (x + error_distribution) / 10
    
    return a.mean() # Ваш ответ
'''
from sklearn.metrics import mean_squared_error as mse
arr = [1,2,3,4,5,6,7,8,9,10] 

sols_1 = []
sols_2 = []
for i in range(10):
    ar = np.random.exponential(size = 10)
    sols_1.append(solution(ar))
    sols_2.append(solution_2(ar))
print(np.mean((np.array(sols_1) - np.array(sols_2))**2))'''