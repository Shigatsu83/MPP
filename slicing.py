# Basic Slicing
text = "Simple Python Programming Language is Easy to Learn"
firstword = text[:6] #mengambil string dari index 0 sampai 6
secondword = text[7:13] #mengambil string dari index 7 sampai 13
print(firstword)
print(secondword)


# Mengambil value Dari 2D Array
gpu = [['Arc A310', 'Arc A380', 'Arc A580'],
       ['Radeon RX 550', 'Radeon RX 560', 'Radeon RX 570'],
       ['GeForce GTX 1050', 'GeForce GTX 1060', 'GeForce GTX 1070']]
print(gpu[0]) # Mengambil value dari array 2D index 0
# print(gpu)

# | Column 0 | Column 1 | Column 2 |
# |--------------------------------|
# | Arc A310 | Arc A380 | Arc A580 |                           
# | RX550    | RX560    | RX 570   |                                     
# | GTX 1050 | GTX 1060 | GTX 1070 |
# |          |          |          |                   
# |          |          |          |          
#Slice value semua row pada column tertentu(Contoh: Column 1)
sliceColumn = [row[1] for row in gpu] # Dari semua array yang ada, ambil masing-masing value array di index 1
print(sliceColumn)

# Print Semua Individual value dari array
for row in gpu:
       for value in row:
              print(value, end=" ")



# program untuk ekstraksi kata dari kalimat string

data = "Simple Python Programming Language is Easy to Learn\n"

def spliting(text):
       splitted = text.split() #mengubah string menjadi list
       senLength = len(splitted)
       print("\nTotal Words in Sentence: " + str(senLength))
       for word in splitted:
              length = len(word)
              print(word + " : " + str(length) + " characters\n")

spliting(data)
#      