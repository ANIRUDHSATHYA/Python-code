'''Predict agent availability
You have the following data for issues.

Issue

start_time
abandoned/resolved
answer_time	(time an agent started working on the issue)
resolved_time (the time an issue was resolved)
abandoned_time (if a customer left before the issue was assigned to an agent)

Now when a  new issue comes in we need to predict the time the issue will be assigned to an
agent. Use your best judgement to solve the above problem. You may/may not want to use all fields.'''


#AGENT AVAILABILITY

import time
import datetime

import random
import pandas as pd

name = input('Enter your Name: ')
gender = input("SELECT YOUR GENDER M OR F: ")

def details():
    if gender == 'M':
        print("WELCOME",f"Mr.{name}")
    elif gender == 'F':
        print(f"WELCOME",f"Ms.{name}")
    else:
        print("Try again!")
        quit()


if __name__ == '__main__':

    def issues():
        # display Menu
        choice = 0
        while choice < 4:
            print("ISSUES")
            print('1. Assingned Issue to an AGENT')
            # print('2. Answer Time')
            # print('3. Resolved time')
            # print('4. Abondoned time')
            print('2. Start Time')
            print('3. EXIT')
            choice = int(input('YOUR CHOICES: '))

            if choice == 1:
                agents_prediction()

                
            elif choice == 2:

                start_time = time.asctime(time.localtime())
                print('Your Start Time: ', start_time)

                agents_prediction()
                print('Your Start Time: ', start_time)


            else:
                break

    def agents_prediction():
        start_date = datetime.date(2020, 6, 1)
        end_date = datetime.date(2020, 7, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        agent= {"Agents": ["AGENT 1", "AGENT 2"],
                "Date":[random_date,random_date]
                }
        df = pd.DataFrame(agent)

        print("Available Agents")
        print(df)


details()
issues()
