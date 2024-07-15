def main():
    fuel = input("Fraction: ")
    fuel_convert = convert(fuel)
    output = gauge(fuel_convert)
    print(output)

def convert(fuel):
    while True:
        try:
            numerator, denominator = fuel.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)

            f = new_numerator / new_denominator
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fuel = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            pass

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return int(p) + "%"

if __name__ == "__main__":
    main()
