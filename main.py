import random


def yeah_producer(name):
    return f"Yeah {name}"


def main():
    print("This is my cool app")
    names = ['Alice', 'Bob', 'Carol']
    for i in range(100):
        print(yeah_producer(random.choice(names)))


if __name__ == '__main__':
    main()
