#money_owed = float(input("Money owed in dollars \n"))
#apr = float(input("what is your apr \n"))
#monthly_interest_rate = float (apr /12)
#loan_duration = float (input ("Enter the loan duration \n"))
#total_no_of_payments = float (loan_duration * 12)

#p = float(input("Money owed in dollars \n"))
#apr = float(input("what is your apr \n"))
#i = float (apr /1200)
#loan_duration = float (input ("Enter the loan duration \n"))
#n = float (loan_duration * 12)

#print ("loan duration is", loan_duration , "total_no_of_payments is", total_no_of_payments)
p = 680000
i = float (2.75/1200)
n = float (30 * 12)
after_months = 21

print ("P is", p, "i is", i, "n is", n )

### refer to https://www.mtgprofessor.com/formulas.htm  for formulas

top = (i * ((1+i)**n))
bot = ((1+i)**n)-1
Monthly_Payment = p * top / bot

Loan_balance = p * ((1+i)**n - (1+i)**after_months)/bot



#M = p * ((i*(1+i)**n)/((1+i)**(n-1)))
print ("top is", top, "bot is", bot, "M is", Monthly_Payment, "Loan Balance is ", Loan_balance)
#monthly_mortgage_payment = float (money_owed * ((monthly_interest_rate * (1+monthly_interest_rate)**total_no_of_payments)/(1 + monthly_interest_rate)** (total_no_of_payments-1)))