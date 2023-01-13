import argparse
import csv
import datetime

def create_weekly_roster(names_file, start_date, num_people, num_weeks):
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
    for i in range(0, len(names), num_people):
        if i + num_people > len(names):
            roster.append((week_num, start_date, names[i:]))
            roster[week_num-1][2].append(names[0])
            names.pop(0)
        else:
            roster.append((week_num, start_date, names[i:i+num_people]))
        week_num += 1
        if week_num > num_weeks:
            break
        start_date += datetime.timedelta(days=7)

    return roster

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("names_file", help="the file path of the CSV file containing the names to be added to the roster.")
    parser.add_argument("start_date", help="the starting date for the weekly roster in the format DD-MM-YYYY.")
    parser.add_argument("-n", "--num_people", type=int, default=2, help="the number of people to assign per week.")
    parser.add_argument("-w", "--num_weeks", type=int, help="the number of weeks to generate the roster for.")
    args = parser.parse_args()
    
    #parse the start_date
    start_date = datetime.datetime.strptime(args.start_date, "%d-%m-%Y")

    # test the function
    try:
        roster = create_weekly_roster(args.names_file, start_date, args.num_people, args.num_weeks)
    except FileNotFoundError:
        print("The file path provided does not exist.")
        return
    except ValueError:
        print("The CSV file is empty.")
        return
    # print the roster in a table format
    print("Week | Date       | Names")
    print("-----|------------|------")
    for week, date, names in roster:
        date_str = date.strftime("%d/%m/%Y")
        names_str = " and ".join(names)
        print(f"{week:4d} | {date_str:10s} | {names_str}")

if __name__ == '__main__':
    main()