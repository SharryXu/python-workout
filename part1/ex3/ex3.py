from decimal import Decimal


def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input("Enter 10 km run time: ")

        if not one_run:
            break

        number_of_runs += 1
        total_time += Decimal(one_run)

    average_time: Decimal = total_time / number_of_runs

    print(f"Average of {average_time}, over {number_of_runs} runs")


if __name__ == "__main__":
    run_timing()
