def main():

#Declaring the global variables for tasks 3 and 4, so we can output the solutions separately and use these variables in both functions.

    split_test = 'This is a split test'
    splited_test = split_test.split(" ")
    string_join = " ".join(splited_test)

#Declaring the global variables for tasks 6 and 7, so we can output the solutions separately and use these variables in both functions.

    list_extend = [4, 5, 6]
    list_extend.extend([7, 8, 9])

#Declaring the dictionary as global variable for tasks 9, 10, and 7, so we can output the solutions separately and use these variables in both functions.

    dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}


    def task1():

        num_str = 125
        num_str_as_str = str(num_str)
        print(num_str)
        print('\nSolution for the first task is: ', type(num_str_as_str))


    def task2():

        message = 'Hi, my name is Python!'
        result = message.replace('y', 'o').replace('i', '1')
        print("\nSolution for the second task is: ", result)


    def task3():

        print(splited_test)
        print("\nThe Solution for the third task is: ", string_join)


    def task4():

        print('\nThe length of the string is: ', len(string_join))


    def task5():

        list_append = [1, 2, 3]

        list_append.append(4)
        list_append.append(5)
        print("\nThe solution for the fifth task is: ", list_append)


    def task6():

        print('\nThe solution for the sixth task is: ', list_extend)


    def task7():

        print('\nThe Solution for the seventh task is: ', list_extend.index(6))


    def task8():

        print("\nThe length of array is: ", len(list_extend))


    def task9():

        print('\n', dict_test['car'], dict_test['where'])


    def task10():

        print("\nKeys: ", dict_test.keys(),"\nValues: ", dict_test.values())


    def task11():
        print("\nThe values of the keys are: ", dict_test.items())



    while True:

            print('\n Hello! Welcome to the second Home Work', '\n', 'Navigate from tasks using the buttons 1-9')
            print('\n1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()')
            print('2. Cтворити зміну message = Hi, my name is Python! За допомогою функції replace() замінити усі букви y на 0 та i на 1')
            print('3. Cтворити зміну split_test = This is a split test і розділити її по пробілах за допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join')
            print('4. Визначити довжину рядку string_join за допомогою функції len()')
            print('5. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5')
            print('6. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()')
            print('7. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()')
            print('8. Визначити довжину списку list_append за допомогою функції len()')
            print('9. Cтворити змінну ', dict_test, ' та вивести на екран дані, які знаходяться в ключах car та where')
            print('10. За допомогою функцій keys() і values() вивести на екран ключі та їх значення')
            print('11. За допомогою функції items() вивести на екран пари ключ - значення')
            print('///////////////////////////////////////////////')
            print('0. Exit')



            choice = input("\n Choose the task: ")
            if choice == '1':
                task1()

            elif choice == '2':
                task2()

            elif choice == '3':
                task3()

            elif choice == '4':
                task4()

            elif choice == '5':
                task5()

            elif choice == '6':
                task6()

            elif choice == '7':
                task7()

            elif choice == '8':
                task8()

            elif choice == '9':
                task9()

            elif choice == '10':
                task10()

            elif choice == '11':
                task11()

            elif choice == '0':
                break
            else:
                print("\n Invalid choice, folks, try again")


main()




