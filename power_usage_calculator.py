def add(x, y):
    return sum(x+y)

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x,y):
   if y==0:
       error = "Error: Undefined"
       return error
       
   else: 
       return x/y
def calculate_power_usage(servers, watts_per_server):
    total_watts = servers*watts_per_server
    total_kilowatts = total_watts/1000
    return total_kilowatts
def calculate_pue(total_facility_power, it_equipment_power):
    pue = total_facility_power/it_equipment_power

    if pue < 1.2:
        rating = "Excellent"
    elif pue < 1.5:
        rating = "Good"
    elif pue < 2.0:
        rating= "Average"
    else: 
        rating= "Needs Improvement"

    return pue, rating

def calculate_monthly_cost(kilowatts, hours_per_month, cost_per_kwh):
    kwh_used = kilowatts * hours_per_month
    total_cost = kwh_used * cost_per_kwh
    return kwh_used, total_cost

print("=== Data Center Power Calculator === \n")

print("--- Basic Calculator ---")
print(f"10+5 = {add(10, 5)}")
print(f"10-5 = {subtract(10,5)}")
print(f"10 x 5 = {multiply(10,5)}")
print(f"10/5 = {divide(10, 5)}\n")

print("--- Power Usage Calculator ---")
num_servers= 1000
watts_each= 500
total_kw= calculate_power_usage(num_servers, watts_each)
print(f"Servers: {num_servers}")
print(f"Watts Per Server: {watts_each}")
print(f"Total Power Consumption: {total_kw} kw\n")

print("--- PUE Calculation ---")
facility_power= 750
it_power= 500
pue_value, pue_rating = calculate_pue(facility_power, it_power)
print(f"Total Facility Power: {facility_power}kw")
print(f"IT Equipment Power: {it_power}kw")
print(f"PUE: {pue_value:.2f}")
print(f"Rating: {pue_rating}\n")

print("--- Monthly Cost Estimate ---")
hours_month= 730
cost_kwh= 0.12
kwh_used, monthly_cost = calculate_monthly_cost(total_kw, hours_month, cost_kwh)
print(f"Power Consumption: {total_kw}kW")
print(f"Hours Per Month: {hours_month}")
print(f"Cost Per kWh: ${cost_kwh}")
print(f"Monthly kWh used: {kwh_used:,.0f}kWh")
print(f"Monthly Cost: ${monthly_cost:,.2f}")
