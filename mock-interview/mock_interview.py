"""
Date 05.06.2026
0900 - 0950
Interviewer Tomer Asulyn
Onboarding Process
Description:

Given a list of employees, return a list of employee names who have completed the onboarding process.

An employee is considered to have completed onboarding if their status is “active” and they have
completed at least 3 required training modules.

Test Data:

employees = [

    {"name": "Darin", "status": "active", "modules_completed": 3},

    {"name": "Bob", "status": "inactive", "modules_completed": 2},

    {"name": "Charlie", "status": "active", "modules_completed": 4},

    {"name": "Lil", "status": "active", "modules_completed": 0}

]

# Expected output: ['Darin', 'Charlie']
Assume the list filled. No edge cases
"""

def find_active_employees(employees: list) -> list:
    active_empl = []
    for employee in employees:
        if employee.get("status") == "active" and employee.get("modules_completed") >= 3:
            active_empl.append(employee["name"])
    return active_empl

def main():
    employees = [

        {"name": "Darin", "status": "active", "modules_completed": 3},

        {"name": "Bob", "status": "inactive", "modules_completed": 2},

        {"name": "Charlie", "status": "active", "modules_completed": 4},

        {"name": "Lil", "status": "active", "modules_completed": 0}

    ]
    active_employees = find_active_employees(employees)
    print(active_employees)

if __name__ == "__main__":
    main()