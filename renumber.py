numb_channel = ''
FILE = 'AfterLunch.txt'


with open(FILE, mode='r') as file:
    for n,row in enumerate(file,1):
        if not row:
            continue

        name_channel = row[4:].strip()
        number = f'000{n}' if n<10 else f'00{n}' if n<100 else f'0{n}'

        numb_channel += f'{number} {name_channel}\n'



with open(FILE,'w') as file:
    file.write(numb_channel)
