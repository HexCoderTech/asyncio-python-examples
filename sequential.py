import time

def make_coffee():
    print("Making coffee")
    time.sleep(3)
    print("Coffee is ready")


def make_toast():
    print("Making toast")
    time.sleep(2)
    print("Toast is ready")


def apply_butter():
    print("Applying butter")
    time.sleep(1)
    print("Butter is applied")


def make_eggs():
    print("Making eggs")
    time.sleep(2)
    print("Eggs are ready")


def main():
    make_coffee()
    make_toast()
    apply_butter()
    make_eggs()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time taken: {(end - start):2f}")