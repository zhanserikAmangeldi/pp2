import os

# getcwd

# print("local directory:", os.getcwd())

# os.path.isdir if this catalog exist return True

# if not os.path.isdir("folder"):
#     os.mkdir('folder')

# changing name of catalog (where exist this)

# os.chdir("folder")

# print("Текущая директория изменилась на folder:", os.getcwd())


# change name of file

# with open("file.txt", 'a') as file:
#     pass

# os.rename("file.txt", "rename-file.txt")

# replace file

# os.replace("rename-file.txt", "folder/rename-file.txt")

# receive all object in the catalog

# print(os.listdir())

# receive all object

# with open("folder/foldertwo/file.txt", 'a') as file:
#     pass

# for i, j, z in os.walk("."):
    
#     for j in j:
#         print(os.path.join(i, j))

#     for z in z:
#         print(os.path.join(i, z))