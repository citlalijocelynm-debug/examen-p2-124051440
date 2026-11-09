#!/usr/bin/env python3
import sys

def main():
    current_key = None
    total_ingreso = 0.0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            key, ingreso_str = line.split('\t', 1)
            ingreso = float(ingreso_str)

            if current_key == key:
                total_ingreso += ingreso
            else:
                if current_key:
                    print(f"{current_key}\t{total_ingreso:.2f}")
                current_key = key
                total_ingreso = ingreso
        except (ValueError, IndexError):
            continue

    if current_key:
        print(f"{current_key}\t{total_ingreso:.2f}")

if __name__ == "__main__":
    main()
