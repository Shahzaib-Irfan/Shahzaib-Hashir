import random


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def main():
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))

    random_number = generate_random_number(min_value, max_value)

    print(
        f"The random number between {min_value} and {max_value} is: {random_number}")


if __name__ == "__main__":
    main()
    print("hello")
