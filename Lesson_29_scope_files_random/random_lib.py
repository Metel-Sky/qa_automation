import random

random.seed(1)  # �� � �������� ������

print(random.random()) # [0, 1] float
print(int((random.random()*100))) # [0, 100]
print(int((random.random()*50))) # [0, 50]
print(int(3 + random.random()*(10-3))) # [3, 10]


for i in range(20): # ���� ����� � ��������
    print(random.randint(3,7), end="/")
#
print()
#
for i in range(20): # ���� ����� � �������� � ������
    print(random.randrange(1,7, 2), end="/")
print()
lst = ["apple", "banana", "orange", "carrot", "cherry"]
# print(lst)
# random.shuffle(lst) # ������������ ������
# print(lst)

print(random.sample(lst, counts=[1,1,10,1,10], k=3))
print(random.sample(lst, counts=[1,1,10,1,10], k=3))