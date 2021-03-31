class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

len(super_list1)
super_list1.append(5)
print(len(super_list1))
print(super_list1[3])
