def test(name, *sec_name, child, **children):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Мать: {name}')
    print("Фамилия девичья, в замужестве", *sec_name)
    print('Имя первого ребенка', child)
    print('Имена последующих детей', children)

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test('Анна',  {'Девичья': 'Фролова', 'В замужестве': 'Власова'}, child='Антон',
         second='Светлана', third='Олег')

    print(fact(int(input("Введите целое число: "))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
