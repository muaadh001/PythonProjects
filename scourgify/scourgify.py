import sys
import csv

def main():
    check_command_line_arg()
    output = []
    try:
        with open(sys.argv[1],"r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                splitname = row["name"].split(",")
                output.append({"first":splitname[1].lstrip(), "last":splitname[0], "house":row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("File is not CSV")

if __name__ == "__main__":
    main()
