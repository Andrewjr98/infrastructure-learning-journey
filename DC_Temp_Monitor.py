def check_temperature(temp):
    if temp < 65:
        status = ' TOO COLD- Risk of condensation'
        severity= 'WARNING'
    elif temp > 80:
        status = 'TOO HOT- Cooling system may be failing'
        severity = 'CRITICAL'
    else:
        status = 'Temperature Normal'
        severity= 'NORMAL'
    return status,severity

def farenheit_to_celsius(f):
    celsius =(f-32)*5/9
    return round(celsius, 1)

def main():
    print("=== Data Center Temperature Monitor ===\n")
    #Test with known value
    current_temp= 42
    print(f'Current Temperature: {current_temp}F({farenheit_to_celsius(current_temp)}C)')
    status, severity=check_temperature(current_temp)
    print(f'Status{status}')
    print(f'Severity Level: {severity}\n')
    #Interactive Mode
    print('---Interactive Mode ---')
    user_temp = float(input('Enter current data center temperature (F): '))
    status, severity = check_temperature(user_temp)
    print(f'\nTemperature: {user_temp} F ({farenheit_to_celsius(user_temp)} C)')
    print(f'Status{status}')
    print(f'Severity: {severity}')

if __name__ == '__main__':
    main()