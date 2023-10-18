before_lunch = []
right_order = [(1, '1+1'), (2, '2+2'), (3, 'UA:Pershyi'), (4, '24 Kanal'), (5, 'Channel 5 (Ukraine) HD'),
               (6, 'Espreso TV'), (7, 'GALYCHYNA HD'), (8, 'STB HD'), (9, 'NOVY CHANNEL HD'),
               (10, 'ICTV HD'), (11, 'ICTV 2'), (12, 'Inter HD'), (13, 'INTER + HD'), (14, 'TET'), (15, 'NTN HD'),
               (16, '1+1 International'), (17, '1+1 Ukraine'), (18, '1+1 Ukraine'), (19, 'UA KULTURA'), (20, 'K1 HD'),
               (21, 'K2 HD'), (22, 'Bigudi'), (23, 'SONCE (UA)'), (24, '1ZAHID HD'), (25, 'Televsesvit'), (26, 'Eko TV'),
               (27, 'OCE HD'), (28, 'DIM TV'), (29, 'Enter Film HD'), (30, 'ZOOM HD'), (31, 'XSport'), (32, 'SUSPILNE SPORT'),
               (33, 'MEGA HD'), (34, 'PIXEL HD'), (35, 'Plus Plus'), (36, 'Fauna'), (37, 'Nauka'), (38, 'Terra'), (39, 'Trofey'),
               (40, 'Espreso TV'), (41, '/////PRYAMIY'), (42, 'Unian TV'), (43, 'Kyiv TV'), (44, 'WE-UKRAINE'), (45, 'Svoboda / Holos Ameryky'),
               (46, 'RADA HD'), (47, 'ChornomorskaTV'), (48, 'SuspilneNews'), (49, 'Apostrophe TV'), (50, 'AVERS'), (51, 'BELSAT TV HD'),
               (52, 'YEMEN TV'), (53, 'UA DONBAS'), (54, 'UA KRYME'), (55, 'UATVa/Holos Ameryky'), (56, 'Current Time HD'),
               (57, 'ATR'), (58, 'PERSHYI HD'), (59, 'M1 HD'), (60, 'M2 HD'), (61, 'STARS.TV'),
               (62, '4Fun.TV'), (63, '4Fun Kids'), (64, '4Fun Dance'), (65, 'Eska TV Extra')]


sort_of_channel = []


with open('AfterLunch.txt',mode='r') as file:
    for n,row in enumerate(file,1):
        channel_name = row[4:].strip()
        # if n == 41: channel_name = channel_name[7:]

        before_lunch.append((n,channel_name))




# with open('RightOrder.txt',mode='r') as file:
#     for n,row in enumerate(file,1):
#         channel_name = row[4:].strip()
#         if n == 31:
#             channel_name = row[7:].strip()
#         right_order.append((n,channel_name))

already_use = []

for number_channel in right_order:
    for number_channel2 in before_lunch:
        if number_channel[1] == number_channel2[1] and number_channel2[0] not in already_use:
            # print(number_channel[1],number_channel2[1])
            sort_of_channel.append(number_channel2[0])
            already_use.append(number_channel2[0])
            break


with open('array_for_cpp.txt','w') as file:
    layer = 'int l[] = {%s};'
    order = ','.join([str(x) for x in sort_of_channel])
    result = layer % order
    print(result)

    file.write(result)




print(before_lunch)
print(right_order)
print([(n,n1) for n,n1 in enumerate(sort_of_channel,1)])
