# emplyee salary data analysis 
# import important library for data analysis as 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# loading the csv file
df=pd.read_csv("employee_salary_dataset.csv")
#display first 5 rows
print("first five rows are :",df.head())
print("\nlast five rows are:",df.tail())
#basic data analysis 
print("\nDataset information :")
print(df.info())
# for mean mode basic stats
print("\nStatistical summary",df.describe())

# for avarage salary
average_salary=df["Monthly_Salary"].mean()
print("\nAverage Monthly_Salary:",average_salary)
#avg salary by department 
salary_by_department=df.groupby("Department")["Monthly_Salary"].mean()
print("\nAverage Salary By Department",salary_by_department)

# Bar Chart : Average Salary By Department 
salary_by_department.plot(kind="bar")
plt.title("Average Monthly Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average monthly salary")
plt.show()
#scatter plot : Average Salary by expereince 
plt.scatter(df["Experience_Years"],
df["Monthly_Salary"])
plt.title("Experience vs Monthly Salary")
plt.xlabel("Experience(Years)")
plt.ylabel("Monthly Salary")
plt.show()
# 7. Heatmap: Correlation Analysis
# -------------------------------
numeric_data = df[["Age", "Experience_Years", "Monthly_Salary"]]
correlation_matrix = numeric_data.corr()

plt.imshow(correlation_matrix)
plt.colorbar()
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.title("Correlation Heatmap")
plt.show()
#Gender wise Average salary
gender_salary=df.groupby("Gender")["Monthly_Salary"].mean()
print("\nAverage Salary by Gender:",gender_salary)
