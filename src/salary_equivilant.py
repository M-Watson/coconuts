from datetime import *
from dateutil import rrule
import pandas as pd
import matplotlib.pyplot as plt

def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()
now = datetime.now()
week_list = []
income_list = []
bill_rate = 40.00
bill_weekly_hours = 30


today = date.today()
future = date(now.year,12,31)
one_year = date(now.year+1,now.month,now.day)
weeks = weeks_between(today,one_year)


print("Todays date is %s, there are %s weeks until December 31, %s"%(str(today),str(weeks),str(now.year)))
previous_income = 0.00

for i in range(weeks):
    cumulative_income = previous_income + (bill_rate * bill_weekly_hours)
    print('\n----\nWeek: %s \nCumulative income: $%s\n----\n'%(str(i+1),str(cumulative_income)))
    income_list.append(cumulative_income)
    week_list.append(i+1)
    previous_income = cumulative_income




pay = bill_rate * bill_weekly_hours * weeks

print(pay)

plt.plot(week_list,income_list)
plt.show()
