import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r"^<iframe(?: width=\"[0-9]+\" height=\"[0-9]+\")? src=\"https?://(?:www\.)?(youtu)(be)\.com/embed(/[a-zA-Z0-9]+)\"(?: title=\"[a-zA-Z]+ [a-zA-Z]+ [a-zA-Z]+\" frameborder=\"[0-9]\" allow=\"\w+; \w+; [a-z-]+; [a-z-]+; \w+; [a-z-]+\" allowfullscreen)?></iframe>$",
        s,
    ):
        return "https://" + matches.group(1) + "." + matches.group(2) + matches.group(3)
    else:
        return None


if __name__ == "__main__":
    main()
