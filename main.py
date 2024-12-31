import argparse
from employee import Employee

def parse_args():
    parser = argparse.ArgumentParser(description="Employee Information")
    parser.add_argument("name", help="Name of the employee")
    parser.add_argument("age", type=int, help="Age of the employee")
    parser.add_argument("salary", type=float, help="Salary of the employee")
    
    # Optional args and kwargs can be passed as a list of strings
    parser.add_argument("-a", "--additional_info", nargs='*', help="Additional information (e.g. hobbies)", default=[])
    parser.add_argument("-d", "--details", nargs='*', help="Details (e.g. department=IT position=Developer)", default=[])

    return parser.parse_args()

def main():
    args = parse_args()

    # Convert details into a dictionary of key-value pairs
    details = {}
    if args.details:
        for detail in args.details:
            key, value = detail.split('=')
            details[key] = value

    # Create an Employee instance
    emp = Employee(
        name=args.name,
        age=args.age,
        salary=args.salary,
        *args.additional_info,  # Pass additional_info as *args
        **details  # Pass details as **kwargs
    )

    # Display employee information
    emp.display_info()

if __name__ == "__main__":
    main()