from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value, PULP_CBC_CMD

# Введення даних
print("Введіть доступні ресурси:")
water = int(input("Вода (од.): "))
sugar = int(input("Цукор (од.): "))
lemon_juice = int(input("Лимонний сік (од.): "))
fruit_puree = int(input("Фруктове пюре (од.): "))

# Створення моделі
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні для кількості продуктів
lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')  # Лимонад
fruit_juice = LpVariable('Fruit_Juice', lowBound=0, cat='Integer')  # Фруктовий сік

# Цільова функція: максимізувати загальну кількість продуктів
model += lpSum([lemonade, fruit_juice])

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= water, "Water_Constraint"  # Вода
model += 1 * lemonade <= sugar, "Sugar_Constraint"  # Цукор
model += 1 * lemonade <= lemon_juice, "Lemon_Juice_Constraint"  # Лимонний сік
model += 2 * fruit_juice <= fruit_puree, "Fruit_Puree_Constraint"  # Фруктове пюре

# Розв'язання моделі
solver = PULP_CBC_CMD(msg=False)
model.solve(solver)

# Виведення результатів
print("\nРезультати оптимізації:")
print(f"Лимонад: {value(lemonade)}")
print(f"Фруктовий сік: {value(fruit_juice)}")
print(f"Загальна кількість продуктів: {value(model.objective)}")