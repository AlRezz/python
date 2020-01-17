a = (input('Enter a card number: '))
length = int(a.__len__())
control_sum = 0
isEvenLength = length % 2 == 0

def getValue(n):
    k = n * 2
    if k > 9:
        return k - 9
    else:
        return k


for i in range(0, length):
    if isEvenLength:
        if i % 2 == 0:
            control_sum += getValue(int(a[i]))
        else:
            control_sum += int(a[i])
    else:
        if i % 2 != 0:
            control_sum += getValue(int(a[i]))
        else:
            control_sum += int(a[i])


if (control_sum % 10 == 0):
    print('Valid')
else:
    print('Invalid')

