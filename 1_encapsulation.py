class BudgetCategory():
#  Task1 - Initialize these attributes in the constructor.
    def __init__(self, category_name, allocated_budget, expense):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
# Task 3 - Add another attribute 'expense' to track how much you have spent towards a category
        self.__expense = 0


# Task 2 - Write getter and setter methods for both the category name and the allocated budget

    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_category_name(self, new_category):
        self.__category_name = new_category

    def set_allocated_budget(self, new_budget):
        self.__allocated_budget = new_budget

    def set_expense(self, add_expense):
        self.__expense = add_expense


# Task 3 - Implement a method to add expenses.

    def expense(self, new_expense):
        self.expense = new_expense
    
    def get_expense(self):
        return self.__expense

    def set_expense(self, add_expense):
        self.__expense = add_expense


# Task 4 - Display budget category, and remaining budget after expenses (budget-expenses)

    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expense
        print(self.__category_name)
        print(remaining_budget)


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()