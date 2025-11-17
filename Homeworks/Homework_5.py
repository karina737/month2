from datetime import datetime as dt
def checktime(func):
    def wrapper():
        time_now = dt.now()
        print(f'Функция была вызвана в {time_now.hour}:{time_now.minute}:{time_now.second}  {time_now.day}/{time_now.month}/{time_now.year}')
        func()
    return wrapper

@checktime
def hello_world():
	return print("hello world")  
hello_world()

#Доп задание1
from datetime import datetime as dt
def checktime_before_after(func):
     def wrapper():
        time_now = dt.now()
        print(f'Функция была вызвана в {time_now.hour}:{time_now.minute}:{time_now.second}  {time_now.day}/{time_now.month}/{time_now.year}')
        func()
        time_end = dt.now()
        print(f'Функция была закончена в {time_end.hour}:{time_end.minute}:{time_end.second}  {time_end.day}/{time_end.month}/{time_end.year}')
     return wrapper


from time import sleep
@checktime_before_after
def hello_world():
    print("hello world")  
    sleep(2)
hello_world()

#Доп задание 2
from datetime import datetime as dt
def async_check_time(func):
    async def wrapper():
        time_now = dt.now()
        print(f'Функция была вызвана в {time_now.hour}:{time_now.minute}:{time_now.second}  {time_now.day}/{time_now.month}/{time_now.year}')
        result=await func()
        time_end = dt.now()
        print(f'Функция была закончена в {time_end.hour}:{time_end.minute}:{time_end.second}  {time_end.day}/{time_end.month}/{time_end.year}')
        return result
    return wrapper

import asyncio
@async_check_time
async def my_coroutine():
    print("Hello")
    await asyncio.sleep(3)
asyncio.run(my_coroutine())