from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"label",
        "message":"New user - Name: ",
    }
]

#add a user to the CSV users.csv with his label
def add_user(*args):
    infos = prompt(user_questions)
    with open('users.csv', 'a', newline='') as csvfile:
        expensewriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        row = []
        row.append(infos["label"])
        expensewriter.writerow(row)

    # This function should create a new user, asking for its name
    return