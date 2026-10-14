def investment_value(start, interest_rate, tax_rate, deposit, years):
    balance = start
    for _ in range(1, years + 1):
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
    return balance

def years_to_reach_goal(start, interest_rate, tax_rate, deposit, goal):
    years = 0
    balance = start
    while balance < goal:
        interest_earned = balance * interest_rate
        taxes = interest_earned * tax_rate
        balance += (interest_earned - taxes + deposit)
        years += 1
    return years

print(years_to_reach_goal(start=1000, interest_rate=0.08, tax_rate=0.18, deposit=100, goal=5000)) 

print(investment_value(start=1000, interest_rate=0.08, tax_rate=0, deposit=100, years=5)) -= print(investment_value(start=1000, interest_rate=0.08, tax_rate=0.18, deposit=100, years=5))

