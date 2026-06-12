import json
import os

FILE_NAME = "data.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_subject(data):
    subject = input("Enter subject name: ")

    if subject in data:
        print("Subject already exists.")
        return

    data[subject] = {
        "attended": 0,
        "conducted": 0,
        "assignments": 0
    }

    print("Subject added successfully.")


def mark_attendance(data):
    subject = input("Enter subject name: ")

    if subject not in data:
        print("Subject not found.")
        return

    status = input("Present or Absent? (P/A): ").upper()

    data[subject]["conducted"] += 1

    if status == "P":
        data[subject]["attended"] += 1

    print("Attendance updated.")


def update_assignments(data):
    subject = input("Enter subject name: ")

    if subject not in data:
        print("Subject not found.")
        return

    try:
        completed = int(input("Assignments completed (0-4): "))

        if 0 <= completed <= 4:
            data[subject]["assignments"] = completed
            print("Assignments updated.")
        else:
            print("Enter a number between 0 and 4.")

    except ValueError:
        print("Invalid input.")


def view_dashboard(data):

    if len(data) == 0:
        print("\nNo subjects added yet.")
        return

    print("\n===== ATTENDX DASHBOARD =====")

    for subject, details in data.items():

        conducted = details["conducted"]
        attended = details["attended"]

        if conducted == 0:
            percentage = 0
        else:
            percentage = (attended / conducted) * 100

        print("\nSubject:", subject)
        print("Attendance:", f"{percentage:.2f}%")
        print(
            "Assignments:",
            f"{details['assignments']}/4"
        )


def main():

    data = load_data()

    while True:

        print("\n===== ATTENDX =====")
        print("1. Add Subject")
        print("2. Mark Attendance")
        print("3. Update Assignments")
        print("4. View Dashboard")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_subject(data)

        elif choice == "2":
            mark_attendance(data)

        elif choice == "3":
            update_assignments(data)

        elif choice == "4":
            view_dashboard(data)

        elif choice == "5":
            save_data(data)
            print("Data saved.")
            print("Exiting AttendX...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()