def lucky_ticket(ticket_number):                        #Функция идентификации счастливого номера
    def summ(s):                                        #Подфункция суммирования цифер в числе:
        a = 0
        for i in s:
            a += int(i)
        return a

    ticket_number = str(ticket_number)                  #Преобразование в строку для работы с длиной чисел

    if len(ticket_number) != 6:                         #В условии задачи у номера билета 6 цифр, верен ли формат номера?
                                                        #Если не верен, то возвращается текст несоответствия условию
        return ticket_number + "\t- Номер билета не соответствует условию задачи"

    fst = ticket_number[:int(len(ticket_number)/2)]     #Определение первого трехзначного числа
    sec = ticket_number[int(len(ticket_number)/2):]     #Определение второго трехзначного числа

    if summ(fst) == summ(sec):                          #Равна ли сумма цифер первого и второго трехзначных чисел?
        return ticket_number + "\t- Билет счастливый"   #Если равна, то возвращаем текст о том, что билет счастливый.
    return ticket_number + "\t- Билет не является счастливым"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
