import io
import os

LINE = "I'm sorry the bug shipped \u2014 the compiler warned me twice, I told it to stop being negative, and now production is down and the compiler is saying 'I told you so' in the logs."


def main():
    target = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with io.open(target, "w", encoding="utf-8") as stream:
        stream.write(LINE)


if __name__ == "__main__":
    main()
