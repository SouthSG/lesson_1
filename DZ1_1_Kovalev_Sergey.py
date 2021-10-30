print('Нажимая ENTER без введения числа, вы испытаете боль!')

duration = int(input('Введите число: '))

#min = duration, 60(секунды)
#hour = duration, 3600(секунды)
#day = duration, 86400(секунды)

if duration <60 and duration >=0:
    print(duration,'сек')
elif duration <0:
    print('Введите значение больше нуля')
elif duration >=60 and duration <3600:
    timemin = duration // 60
    timesec = duration % 60
    print(timemin, 'мин', timesec, 'сек')
elif duration >=3600 and duration <86400:
    timesec = duration % 60
    timemin = duration % 3600 // 60
    timehour = duration // 3600
    print(timehour, 'час', timemin, 'мин',timesec, 'сек')
elif duration >=86400 and duration <604800:
    timesec = duration % 60
    timemin = duration % 3600 // 60
    timehour = duration % 86400 // 3600
    timeday = duration // 86400
    print(timeday, 'дней', timehour, 'час', timemin, 'мин', timesec, 'сек')
else:
    print('Занимайтесь рассчетами самостоятельно, а я спать! o_0')

