import os.path

path1 = r'jpub\dir'
head1, tail1 = os.path.split(path1)
print(head1, tail1)

path2 = r'jpub\dir' + '\\'
head2, tail2 = os.path.split(path2)
print(head2, tail2)

path3 = r'jpub\dir\file.txt'
head3, tail3 = os.path.split(path3)
print(head3, tail3)
