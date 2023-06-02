#найти сумму двух чисел, если они в одной строке
A = int(input("Введите A: ")) #вводим два числа
B = int(input("Введите B: "))


#привязываемся к дескриптору
with open("input.txt", "w") as input_file:
    input_file.write(str(A))    #записываем A
    input_file.write(str(" ")) # записываем пробел
    input_file.write(str(B))    # записываем B
input_file.close()              #закрываем файл

summ =0 #сумма

#декриптор №2
with open("input.txt", "r") as output_file:
    string = output_file.read().split() #считываем единственную строку и
                                        #превращаем ее в список строковых значений
    A = int(string[1])					# ["n1", "n2"] - то, что лежит в string
	#меняем местами
    B = int(string[0])
output_file.close()

#дескриптор №3
with open("output.txt", "w") as input_file:
    input_file.write(str(A))     #записываем число A в файл
    input_file.write(str(" "))   # записываем пробел
    input_file.write(str(B))	 #записываем число B в файл
input_file.close()
