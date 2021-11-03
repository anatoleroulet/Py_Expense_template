from PyInquirer import prompt, Separator
import csv

def get_users(answers):
    user_list = []
    with open('users.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            user_list.append(row[0])
    return user_list

def get_involved(answers):
    user_list = []
    with open('users.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            user_list.append({'name' : row[0]})
    return user_list

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        'type': 'list',
        "name":"spender",
        "message":"New Expense - Spender: ",
        'choices': get_users,
    },

    {
        'type': 'checkbox',
        "name":"people_involved",
        "message":"New Expense - People involved in the expense: ",
        'choices': get_involved
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)

    with open('expense_report.csv', 'a', newline='') as csvfile:
         expensewriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
         row = []
         row.append(infos["amount"])
         row.append(infos["label"])
         row.append(infos["spender"])
         for users in infos["people_involved"]:
            row.append(users)
         expensewriter.writerow(row)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True


