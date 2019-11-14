from random import randint
map_structure = []  # My array to map
with open("maps.txt") as f:  # Method open can read the text in the file
    lines = f.readlines()  # Method readlines to seperate ligne of the text
    for line in lines:

        #line = line.strip()  # strip

        map_structure.append(list(line))
        print(line[:])
    f.close()
print(map_structure)
for i in range(0,14):
    for j in range(0,14):
       print(map_structure[i][j])
c = 0
while c != 3 :
    i = randint(0,14)
    print("la valeur de i au hazard est:",i)
    j = randint(0,14)
    if map_structure[i][j] == " ":
        map_structure[i][j] = "o"
        c += 1
print("----------------------------------------------------------------------------------------------------")
print("la valeur de c est :",c)
for i in range(0,14):
    for j in range(0,14):
       print(map_structure[i][j])