def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()              # функция вызывается, но ничего не возвращает



#inner_function()                     #ОШИБКА: name 'inner_function' is not defined.
                                    #Did you mean: 'test_function'? Не может определить функцию из-за пространства имён
