import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day")
    args = parser.parse_args()

    day = args.day
    if len(day) == 1:
        day = f"0{day}"

    with open(f"data/{day}.txt", "w+") as f:
        f.write("")

    with open("template.py", "r") as template_script_file:
        with open(f"{day}.py", "w+") as script_file:
            script_file.write(template_script_file.read())


if __name__ == "__main__":
    main()
