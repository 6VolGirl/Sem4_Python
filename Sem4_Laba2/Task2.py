def tag(name, *args, **kwargs):
    """
    Формирует строку HTML кода на основании названия тэга, его свойства и его содержания
   """
    attrs = ''.join(f' {key}="{value}"' for key, value in kwargs.items())

    if not args:
        return f'<{name}{attrs} />'

    elements = []
    for content in args:
        elements.append(f'<{name}{attrs}>{content}</{name}>')
    return '\n'.join(elements)



tag ('br')
# ’<br / >’
tag ('p', 'hello')
# ’<p>hello </p>’
print ( tag ('p', 'hello', 'world') )
# <p > hello </ p >
# <p > world </ p >
print (tag ('p', 'hello', id =33))
# ’<p id ="33" > hello </p>’
print (tag ('p', 'hello', 'world', class_ ='sidebar'))
# <p class =" sidebar "> hello </ p >
# <p class =" sidebar "> world </ p >
print (tag ( content ='testing', name ="img"))
# ’<img content =" testing " / >’
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src ': 'sunset .jpg', 'class': 'framed'}
print(tag (** my_tag ))
#  ’<img class = "framed" src = "sunset.jpg" title = "Sunset Boulevard"/ >
