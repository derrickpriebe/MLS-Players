import pandas as pd 
 
# Data setup
salary_table = pd.read_csv("salaries.csv")
salary_table.fillna('', inplace=True)
salary_headings = list(salary_table.columns)
print(salary_headings)
salary_data = list(salary_table.values)
print(salary_data)

