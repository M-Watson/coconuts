from datetime import *
from dateutil import rrule
import pandas as pd
import json
import matplotlib.pyplot as plt

def weeks_between(start_date, end_date,direction):
    if direction == 'until':
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    elif direction == 'from':
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=end_date, until=start_date)
    else: weeks = -1
    return weeks.count()

def off_goal(goal,current):
    difference = goal-current
    return difference

def required_hourly_rate(goal,current,bill_weekly_hours,weeks_left):
    diff = off_goal(goal,current)
    req_rate = diff/(bill_weekly_hours*weeks_left)
    return(req_rate)

# Date variables
today = date.today()
now = datetime.now()
end_of_year = date(now.year,12,31)
beginning_of_year = date(now.year,1,1)

profile = pd.read_csv('../data/profile')

goal_salary = profile['goal']
sched_vac = 10
sched_sick = 5

days_left = 0


total_week_hours = 0
cumulative_hours = 0
total_week_bill = 0
cumulative_bill = 0


current_week_index = 0

difference = off_goal(profile['goal'],profile['cumulative_bill'])

print('You are $%f off your goal'%(difference))

week_list = []
income_list = []
bill_rate = 40.00
bill_weekly_hours = 30





one_year = date(now.year+1,now.month,now.day)
current_week_index = weeks_between(today,beginning_of_year,'from')
weeks = weeks_between(today,end_of_year,'until')
weeks = weeks-1

req_rate = required_hourly_rate(profile['goal'],profile['cumulative_bill'],bill_weekly_hours,weeks)

print('We are in week: %s , there are %s weeks until the end of the year. \n This adds to %s'%(str(current_week_index),str(weeks),str(current_week_index+weeks)))

print("Todays date is %s, there are %s weeks until December 31, %s"%(str(today),str(weeks),str(now.year)))
previous_income = profile['cumulative_bill']

for i in range(weeks):
    cumulative_income = previous_income + (req_rate * bill_weekly_hours)
    week_count = i + current_week_index + 1
    print('\n----\nWeek: %s \nCumulative income: $%s\n----\n'%(str(week_count),str(cumulative_income)))
    income_list.append(cumulative_income)
    week_list.append(week_count)
    previous_income = cumulative_income




pay = bill_rate * bill_weekly_hours * weeks

print('%f'%round(req_rate,2))

plt.plot(week_list,income_list)
plt.plot('52',profile['goal'],'.')
plt.show()
