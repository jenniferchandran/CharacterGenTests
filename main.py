main = open("character.txt", "a")
lines = []

name = input("\n please enter the name of your character: ")
house = input("please enter the house of your character: ")
weapon = input("please enter a characteristic of your character: ")
line = name + "," + house + "," + weapon
lines.append("\n" + line)
lines_str = "\n".join(lines)
main.writelines(lines_str)
main.close()

""""
main = open("character.txt", "r")
lines = main.readlines()
length = len(lines)
index = 0
while index < length: 
  for index in lines :
    line = lines[index].strip("\n")
    final = line[index].split(",")
    main.writelines(final)
    print(final[0] + " is in " + final[1] + " and is " + final[2])
    index += 1
    main.close()
  """

main = open("character.txt","r")
lines = main.readlines()
whichChar = input("please say the name of the character you want to remove: ")
for index in lines: 
  line = lines[index].strip("\n")
  final = line[index].split(",")
  main.writelines(final)
  if whichChar == final[0]: #look at cheatsheet
        donedel = final.remove(whichChar)
        main.writelines(donedel)
        main.close()
