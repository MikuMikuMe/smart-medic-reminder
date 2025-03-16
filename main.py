Creating a "Smart Medic Reminder" involves creating a console-based application with features to allow users to input medication schedules, set reminders, and track medication adherence. Below is a simple implementation using Python, featuring error handling and comments to help guide you through its functionality.

```python
import schedule
import time
from datetime import datetime
from threading import Thread
import sys

class Medication:
    def __init__(self, name, dosage, time):
        self.name = name
        self.dosage = dosage
        self.time = time

# Define a global list to store the medication schedule
medications = []

def add_medication():
    try:
        name = input("Enter medication name: ")
        dosage = input("Enter dosage: ")
        time_taken = input("Enter time to take medication (HH:MM): ")
        # Validate time format
        try:
            valid_time = datetime.strptime(time_taken, '%H:%M')
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
            return
        med = Medication(name, dosage, time_taken)
        medications.append(med)
        print(f"Added medication: {name} at {time_taken}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def reminder(med):
    print(f"Reminder: Time to take your medication - {med.name} ({med.dosage}).")

def schedule_reminders():
    for med in medications:
        schedule.every().day.at(med.time).do(reminder, med)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def track_medication():
    try:
        med_name = input("Enter medication name to track: ")
        med_found = False
        for med in medications:
            if med.name == med_name:
                med_found = True
                print(f"{med.name} ({med.dosage}) is scheduled at {med.time}.")
        if not med_found:
            print("Medication not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to Smart Medic Reminder")
    
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    while True:
        try:
            print("\nOptions:")
            print("1. Add medication")
            print("2. Track medication")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                add_medication()
                schedule_reminders()
            elif choice == '2':
                track_medication()
            elif choice == '3':
                print("Exiting the application.")
                sys.exit(0)
            else:
                print("Invalid option, please choose a valid option.")
        except KeyboardInterrupt:
            print("\nExiting the application.")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Explanation:
- **Medication Class**: Holds information about each medication, such as its name, dosage, and time to be taken.
- **Error Handling**: Uses `try` and `except` to catch and display errors, especially for time conversion and main menu options.
- **Scheduling**: Uses the `schedule` library to set up reminders based on the user-defined times. Each medication creates a daily reminder at its specified time.
- **Multithreading**: Utilizes a separate thread to run the scheduler concurrently with user input and interaction.
- **User Interaction**: Provides a text-based interface for users to add medications, check schedules, and manage reminders.

### Notes:
- This program is console-based and suitable for simple use. For more advanced features or a different interface, consider integrating with a GUI framework like Tkinter or a mobile notification service.