import os

cat = input()

############### first ###############


# for i, j, z in os.walk(cat):
    
#     for j in j:
#         print(os.path.join(i, j))

#     for z in z:
#         print(os.path.join(i, z))

############### second ###############

'''
print(os.access(cat, os.F_OK))

print(os.access(cat, os.R_OK))

print(os.access(cat, os.W_OK))

print(os.access(cat, os.E_OK))
'''

############### third ###############

############### fourth ###############

sum = 0

with open(cat, 'r',encoding="utf-8") as file:
    for i in file:
        print(len(i))
        sum += len(i)
print (sum)

############### fifth ###############



# with open(cat, 'w') as file:
    

############### sixth ###############

# try:
#     os.mkdir('test')
# except:
#     print("Exist")

# for i in 'ABCCDEFGHIJKLMNOPQRSTUVWXYZ':
#     open("test/{}.txt".format(i), 'a')

############### seventh ###############

# catcopy = input()

# with open(cat, 'r') as file, open(catcopy, 'r') as fileforcopy:
#     for i in file:
#         fileforcopy.write(i)


############### eighth ###############


# if os.path.exists(cat):
#     os.remove(cat)
# else:
#     print("does not exist")


############### ###### ###############
