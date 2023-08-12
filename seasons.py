from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birth_date = validate_date(input("Date of Birth: "))
    today_date = date.today()
    diff = today_date - birth_date

    calcue = diff.days * 24 * 60
    calcue_inflect = p.number_to_words(calcue, andword="")
    print(f"{calcue_inflect.capitalize()} minutes")


def validate_date(birthdate):
    try:
        _ = date.fromisoformat(birthdate)
    except Exception:
        sys.exit("Invalid Date")
    else:
        return _

if __name__ == "__main__":
    main()
