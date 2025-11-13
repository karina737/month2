def checktime(func):
    def wrapper():
        from datetime import datetime as dt
        time_now = dt.now()
        print(f'Функция была вызвана в {time_now.hour}:{time_now.minute}:{time_now.second}  {time_now.day}/{time_now.month}/{time_now.year}')
        func()
    return wrapper

@checktime
def hello_world():
	return print("hello world")  
hello_world()
