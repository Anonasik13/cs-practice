import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()

    valid_records = read_valid(lines)
    empty_count = sum(1 for line in lines if not line.strip())
    error_count = len(lines) - len(valid_records) - empty_count

    print(len(valid_records))
    print(error_count)

    warmest = warmest_city(valid_records)
    if warmest == "":
        print("0.0")
    else:
        averages = average_by_city(valid_records)
        print(f"{averages[warmest]:.1f}")


if __name__ == "__main__":
    main()
# 1
