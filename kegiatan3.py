dt_list = [3.1, 'Hello', 2.7, 'Python', 105, 'World', 737, 'AI', 412, 5.5]


def tipe(value):
    if isinstance(value, float):
        return 'float'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, str):
        return 'string'


data_float = tuple(filter(lambda x: tipe(x) == 'float', dt_list))
data_int = list(filter(lambda x: tipe(x) == 'int', dt_list))
data_string = list(filter(lambda x: tipe(x) == 'string', dt_list))


def int_ke_dict(data):
    ratusan = data // 100
    puluhan = (data % 100) // 10
    satuan = data % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}


dt_mapped = map(int_ke_dict, data_int)

print("Data Float : ", data_float)
print("Data Int : ")
for data in dt_mapped:
    print(data)
print("Data String : ", data_string)
