from finance import FinanceTracker

def main():
    tracker = FinanceTracker()
    print("💼 Личный финансовый калькулятор")
    while True:
        print("\n1. Добавить доход")
        print("2. Добавить расход")
        print("3. Показать баланс")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                amt = float(input("Сумма дохода: "))
                tracker.add_income(amt)
                print(f"✅ Доход {amt} добавлен")
            except ValueError as e:
                print(f"❌ Ошибка: {e}")
        elif choice == "2":
            try:
                amt = float(input("Сумма расхода: "))
                tracker.add_expense(amt)
                print(f"✅ Расход {amt} добавлен")
            except ValueError as e:
                print(f"❌ Ошибка: {e}")
        elif choice == "3":
            print(f"📊 Общий доход: {tracker.total_income()}")
            print(f"📉 Общий расход: {tracker.total_expenses()}")
            print(f"💰 Баланс: {tracker.balance()}")
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("⚠️ Неверныйq выбор")

if __name__ == "__main__":
    main()
