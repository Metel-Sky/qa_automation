# �� ���������� ����� � ����� ������ �� ��������� � ��������� ���� �� ����� ²Ѳ� ��ǲ�!!!
with open("1.txt", "w") as file:
    for i in range(9):
        file.write(i)

#���������� ����� � ����� ������ �� ��������� � ��������� ���� �� ����� ���� ���
with open("2.txt", "w") as file:
    text = ""
    for i in range(9):
        text += str(i)
    file.write(text)