task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"{task} is a high priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"{task} is a high priority task. Consider completing it as soon as possible.")
        else:
            print('invalid response')
    case 'low':
        if time_bound == 'no':
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
        elif time_bound == 'yes':
            print(f"{task} is LOW priority but has a deadline. Fit it into your schedule when possible.")
        else:
            print('invalid response')
    case 'medium':
        if time_bound == 'yes':
            print(f"{task} has MEDIUM priority but is time-bound. Schedule it for today or very soon.")
        elif time_bound == 'no':
            print(f"{task} has MEDIUM priority. Plan to work on it when you’re done with urgent tasks.")
        else:
            print("Invalid response")
            