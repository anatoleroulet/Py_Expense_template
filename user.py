from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"label",
        "message":"New user - Name: ",
    }
]

def add_user(*args):
    infos = prompt(user_questions)
    print(infos["label"])
    with open('users.csv', 'a', newline='') as csvfile:
        expensewriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        row = []
        row.append(infos["label"])
        expensewriter.writerow(row)
    csv.writer
    # This function should create a new user, asking for its name
    return