#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.reader(sys.stdin)
    for line_num, row in enumerate(reader):
        if line_num == 0 and row[0] == "id":
            continue
        try:
            if len(row) < 8:
                continue
            fecha_hora = row[1]
            mes = fecha_hora[:7]
            categoria = row[3]
            cantidad = float(row[5])
            precio = float(row[6])
            ingreso = cantidad * precio
            print(f"{categoria}|{mes}\t{ingreso}")
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()
