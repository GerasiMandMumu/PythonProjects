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
    int_string = list(map(int, string)) #строковые значения превращаем в целые
    summ = sum(int_string)              #находим сумму
output_file.close()
print(summ)

#дескриптор №3
with open("output.txt", "w") as input_file:
    input_file.write(str(summ))     #записываем сумму в файл
