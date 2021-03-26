electricity_bill = float(input('How much was the electricity bill? '))
heat_bill = float(input('How much was the heat bill? '))
total_bill_amount = electricity_bill + heat_bill

person_1_name = input('What is the first person\'s name? ')
person_2_name = input('What is the second person\'s name? ')

person_1_days_in_the_home = int(input('How many days was %s in the home? ' % person_1_name))
person_2_days_in_the_home = int(input('How many days was %s in the home? ' % person_2_name))

total_person_days_in_the_home = person_1_days_in_the_home + person_2_days_in_the_home
print('Total number of person days are: %d day/s' % total_person_days_in_the_home)

bill_amount_per_person_day = total_bill_amount / total_person_days_in_the_home

person_1_amount_owed = bill_amount_per_person_day * person_1_days_in_the_home
person_2_amount_owed = bill_amount_per_person_day * person_2_days_in_the_home

print('%s owes $%.2f' % (person_1_name, person_1_amount_owed))
print('%s owes $%.2f' % (person_2_name, person_2_amount_owed))