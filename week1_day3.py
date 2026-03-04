def calculate_uptime_percentage(total_hours, downtime_hours):
    uptime_hours= total_hours - downtime_hours
    uptime_percentage= (uptime_hours/total_hours)*100
    return uptime_percentage
def classify_uptime(percentage):
    if percentage>= 99.99:
        return 'Tier IV (99.99%+)'
    elif percentage >= 99.9:
        return 'Tier III(99.9%+)'
    elif percentage >= 99.0:
        return 'Tier II(99.0%+)'
    else:
        return 'Below Standard'
    
hours_in_month = 730
downtime= 2
uptime = calculate_uptime_percentage(hours_in_month, downtime)
tier = classify_uptime(uptime)

print(f'Uptime: {uptime:.2f}%')
print(f'Classification: {tier}')
print(f'Downtime: {downtime} hours out of {hours_in_month}')