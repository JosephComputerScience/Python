def print_report(report,day):

    for ls in report:
        print 'Day', day
        for key, value in sorted(ls.items()):
            print key, "${:.2f}".format(value)
        print ""

day = 0
cost_per_minute = 0.10
report = []
guest_time_spent = {}
amt_guest_owe = {}

while True:
    try:
        user_input = raw_input()
        if user_input == 'OPEN':
            day += 1
            report = []
            amt_guest_owe.clear()
        if user_input == 'CLOSE':
            report.append(amt_guest_owe)
            print_report(report, day)
        ls = user_input.split()
        if ls[0] == 'ENTER':
            guest_time_spent[ls[1]] = float(ls[2])
        if ls[0] == 'EXIT':
            temp_guest = ls[1]
            time_spent = float(ls[2]) - guest_time_spent.pop(ls[1])
            guest_owe = time_spent * cost_per_minute
            if not temp_guest in amt_guest_owe:
                amt_guest_owe[temp_guest] = guest_owe
            else:
                new_debt = guest_owe + amt_guest_owe[temp_guest]
                amt_guest_owe[temp_guest] = new_debt
    except EOFError:
        break;
