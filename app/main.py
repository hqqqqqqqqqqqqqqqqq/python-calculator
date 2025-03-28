from calculator import Calculator

def main():
    calc = Calculator()
    
    print("\nКалькулятор на Python")

    while True:
        print("\n")
        print("Список операций:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Завершение работы калькулятора")
        
        try:
            choice = input("Выберите операцию (1-5): ")
            
            if choice == '5':
                print("\nРабота калькулятора завершена.")
                break
                
            if choice not in ('1', '2', '3', '4'):
                print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
                continue
                
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            if choice == '1':
                print("\n", f"Результат операции: {calc.add(num1, num2)}")
            elif choice == '2':
                print("\n", f"Результат операции: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print("\n", f"Результат операции: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print("\n", f"Результат операции: {calc.divide(num1, num2)}")
                
        except ValueError as e:
            print("\n", f"Ошибка: {e}")
        except Exception as e:
            print("\n", f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()