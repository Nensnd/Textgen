import threading
import numpy as np
import random

def sig(x):
    return float(1 / (1 + np.exp(-x)))

def laymatch(nums, weights, neurons):
    res = []
    x = 0
    for i in range(neurons):
        for j in range(len(nums)):
            x += float(nums[j]) * float(weights[i * len(nums) + j])
        res.append(sig(x))
        x = 0
    return res

txt = "текст, текст для тренировки нейросети"

txt_ready =  txt.replace(",", "").replace(".", "").split()

w1 = []
w2 = []
w3 = []

for i in range(len(list(dict.fromkeys(txt_ready))) * 128):
    w1.append(random.uniform(-0.5, 0.5))

for i in range(128 * 128):
    w2.append(random.uniform(-0.5, 0.5))

for i in range(128 * 128):
    w3.append(random.uniform(-0.5, 0.5))



#функция нейросети
def nn(input, w1, w2, w3):
    out = []
    words_output = dict.fromkeys(txt_ready)
    
    words_input = dict.fromkeys(txt_ready)
    
    
    input = input.replace(",", "").replace(".", "").split()
    
    #сама, собственно говоря, нейросеть
    #создание выходов
    
    
    
    
    r1 = []
    r2 = []
    r3 = []
    
    for i in words_input:
        words_input[i] = 0.0
        
    
    #перебор входа данных
    for i in input:
        for j in words_input:
            if i == j:
                words_input[j] = float(1.0)
                r1 = laymatch(list(words_input.values()), w1, 128)
                r2 = laymatch(r1, w2, 128)
                r3 = laymatch(r2, w3, len(list(words_output.values())))
                words_input[j] = words_input[j] / 2.0
                genword =                                  dict(zip(list(words_output.keys()), r3))
    
                out.append(max(genword, key=genword.get))
    return out                
                
                
    
#тренировка нейросети
for i in range(len(txt_ready)):
    pass                            
                            
            
print(nn("текст", w1, w2, w3)[0])    
    
#функция для нахождения самого вероятного значения
#max_key = max(словарь, key=словарь.get())
