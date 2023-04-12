import pandas as pd
import numpy as np
import math
from scipy.stats import norm

chat_id = 483660375 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Расчет вероятности успеха на контрольной выборке
    p1 = x_success / x_cnt

    # Расчет вероятности успеха на тестовой выборке
    p2 = y_success / y_cnt

    # Расчет статистики Z-критерия
    z = (p2 - p1) / math.sqrt(p1 * (1 - p1) / x_cnt + p2 * (1 - p2) / y_cnt)

    # Расчет критического значения для заданного уровня значимости
    alpha = 0.08
    z_alpha = abs(norm.ppf(alpha / 2))

    # Сравнение статистики с критическим значением и принятие решения
    if abs(z) > z_alpha:
        return True  # Отклоняем нулевую гипотезу
    else:
        return False  # Не отклоняем нулевую гипотезу
