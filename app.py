from rich import print

from collector.windows import get_interfaces
from collector.parser import parse_interface


def main():

    raw = get_interfaces()

    wifi = parse_interface(raw)

    print(wifi)


if __name__ == "__main__":
    main()