# Q1
salaries_2DList = [[40000.00, 45000.00, 55000.00], [35000.00, 47500.00, 53000.00], [47000.00, 52500.00, 58000.00]]
print('*' * 50)
print("{:^50}".format("Staff Details"))
print('*' * 50)
print(f'{"Year 1":15}{"Year 2":20}{"Year 3":12}')
print('*' * 50)
for employee in salaries_2DList:
    print(f'{employee[0]:6.6}{employee[1]:13.2}{employee[2]:19.8}')

# Q2
from statistics import mean

average_year1 = mean(row[0] for row in salaries_2DList)
average_year2 = mean(row[1] for row in salaries_2DList)
average_year3 = mean(row[2] for row in salaries_2DList)

# Q3
EMPLOYEE_INDEX = 1
YEAR1 = 6
YEAR2 = 3
YEAR3 = 3
NUM_SALARY = 2
for employee in salaries_2DList:
    average = employee[YEAR1] + employee[YEAR2] + employee[YEAR3] / NUM_SALARY
    print("Average for", employee[EMPLOYEE_INDEX], round(average, 2))

# Q4
highest_avg = max(average)
highest_avg_index = average.index(highest_avg)
print(f"Highest Average Earned: {highest_avg:.2}")
print(f"Earned by employee #{highest_avg_index + 1}")

# Q5
increases = [salaries_2DList[i][-1] - salaries_2DList[i][0] for i in range(3)]
for i, inc in enumerate(increases):
    print(f"Increase in salary for employee #{i + 1}: {inc:.2f}")

# Q6
print("{:^50}".format("Edit Function"))
employee_no = int(input("Employee number: 1..3 only"))
