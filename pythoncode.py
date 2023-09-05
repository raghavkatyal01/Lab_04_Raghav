import pandas as pd
DataValue= {
    'Employee ID': ['161E90', '161F91', '161F99', '171E20', '171G30'],
    'Name': ['Raman', 'Himadri', 'Jaya', 'Tejas', 'Ajay'],
    'Age': [41, 38, 51, 30, 45],
    'Salary (PM)': [56000, 67500, 82100, 55000, 44000]
}
df=pd.DataFrame(DataValue)
class EmployeeDetails:


    def displayData(self):
  
        a=int(input(("Enter the age")))
        age=df[df['Age']==a]
        if not age.empty:
            print("Matching Rows:")
            print(age)
        b=str(input(("Enter the Name")))
        n=df[df['Name']==b]
        if not n.empty:
            print("Matching Rows:")
            print(n)
        c=str(input(("Enter the Salary")))
        t=df[df['Salary (PM)']==c]
        if not t.empty:
            print("Matching Rows:")
            print(t)
obj=EmployeeDetails()        
obj.displayData()