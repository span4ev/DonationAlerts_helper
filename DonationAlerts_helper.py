import locale
# Локаль для правильной сортировки русских букв
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

with open ('donations.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if '\ufeff' in lines[0]:
        lines[0] = lines[0].replace('\ufeff', '')

x_1 = '<li><span class="username">'
x_2 = '</span><span class="delimiter"> - </span><span class="amount">'
x_3 = ' <span class="currency">RUB</span></span></li>'


temp_lst = []

for i in lines:
    split = i.split(x_1)
    if len(split) > 1:
        x = split[-1].split(x_2)
        y = x[1].split(x_3)[0]
        temp_lst.append((x[0], y))


temp_dict = {}
for i in temp_lst:
    x, y = i[0], int(i[1])
    if not x in temp_dict:
        temp_dict[x] = y
    else:
        temp_dict[x] += y

temp_lst = []
for i, k in temp_dict.items():   
    temp_lst.append((i, k))



with open ('config.txt', 'r', encoding='utf-8') as f:
    config = f.readlines()


# Настройка по умолчанию - сортировка по большему донату
sorting = 2
# Настройка по умолчанию - указание валюты после суммы отсутствует
line_ending = ''
# Настройка по умолчанию - указание общей суммы всех донатов
total_sum = 1

for i in config:
    if 'sorting' in i:
        x = i.split('=')[-1].strip()
        if x.isdigit() and 0 <= int(x) <= 4:
            sorting = int(x)
        else:
            sorting = 2
    if 'line_ending' in i:
        x = i.split('=')[-1].strip()
        line_ending = x
    if 'total_sum' in i:
        x = i.split('=')[-1].strip()
        if x.isdigit() and int(x) == 0 or x.isdigit() and int(x) == 1:
            total_sum = int(x)
        else:
            total_sum = 1


if sorting == 0:
    temp_lst = temp_lst
if sorting == 1:
    temp_lst = temp_lst[::-1]
if sorting == 2:
    temp_lst = [(t[1], t[0]) for t in temp_lst]
    temp_lst = sorted(temp_lst, key=lambda x: x[0], reverse=True)
    temp_lst = [(t[1], t[0]) for t in temp_lst]
if sorting == 3:
    temp_lst = [(t[1], t[0]) for t in temp_lst]
    temp_lst = sorted(temp_lst, key=lambda x: x[0])
    temp_lst = [(t[1], t[0]) for t in temp_lst]
if sorting == 4:
    temp_lst = sorted(temp_lst, key=lambda item: locale.strxfrm(item[0]))


with open ('donations_result.txt', 'w', encoding='utf-8') as f:
    result_sum = 0
    for i in temp_lst:
        line = f'{i[0]} - {i[1]} {line_ending} \n'
        result_sum += i[1]
        f.writelines(line)
    if total_sum:
        f.write(f'\nОбщая сумма - {result_sum} {line_ending}')






