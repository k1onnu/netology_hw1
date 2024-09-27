
def lucky_ticket():
    ticket = input("number: ")
    if len(ticket) != 6 or not ticket.isdigit():
        print("Некорректный номер билета")
        return

    first_half = sum(int(digit) for digit in ticket[:3])
    second_half = sum(int(digit) for digit in ticket[3:])

    if first_half == second_half:
        print("Счастливый билет")
    else:
        print("Несчастливый билет")

lucky_ticket()