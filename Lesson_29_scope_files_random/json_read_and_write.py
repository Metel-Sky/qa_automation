import json

# # dump - ��� ������ � ����
# data = {"name": "Pavlo", "salary": "120 000"}
#
# # �� � �������� ��������� �� �������� ��� ���� �� ��������� ���� ����� ensure_ascii=False
# with open("data_json", "w") as file:
#     json.dump(data, file, ensure_ascii=False)


# dumps - ��� ������ � ����
# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))
# print(type(data))

with open("data_json", "r") as file:
    data2 = json.load(file)
    print(data2)