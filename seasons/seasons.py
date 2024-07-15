from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birthdate)
    except:
        sys.exit("Invalid Date")
    dateofbirth = date(int(year), int(month), int(day))
    dateoftoday = date.today()
    difference = dateoftoday - dateofbirth
    totalminutes = difference.days * 24 * 60
    output = p.number_to_words(totalminutes, andword="")
    print(output.capitalize() + " minutes")


def check_birthday(birthdate):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthdate):
        year, month, day = birthdate.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
