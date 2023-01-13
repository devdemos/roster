import argparse
import csv
import datetime

def create_weekly_roster(names_file, start_date):
    #create an empty roster list
    roster = []

    # open the names file and read in the names
    with open(names_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        names = [row[0] for row in reader]

    # shuffle the names to create a random roster
    import random
    random.shuffle(names)

    # create the weekly roster
    week_num = 1
    for i in range(0, len(names), 2):
        if i + 2 > len(names):
            roster.append((week_num, start_date, names[i:]))
            roster[week_num-1][2].append(names[0])
            names.pop(0)
        else:
            roster.append((week_num, start_date, names[i:i+2]))
        week_num += 1
        start_date += datetime.timedelta(days=7)

    return roster

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("names_file", help="the file path of the CSV file containing the names to be added to the roster.")
    parser.add_argument("start_date", help="the starting date for the weekly roster in the format DD-MM-YYYY.")
    args = parser.parse_args()

    #parse the start_date
    start_date = datetime.datetime.strptime(args.start_date, "%d-%m-%Y")

    # test the function
    roster = create_weekly_roster(args.names_file, start_date)

    # print the roster in a table format
    print("Week | Date       | Names")
    print("-----|------------|------")
    for week, date, names in roster:
        date_str = date.strftime("%d/%m/%Y")
        names_str = " and ".join(names)
        print(f"{week:4d} | {date_str:10s} | {names_str}")

if __name__ == '__main__':
    main()