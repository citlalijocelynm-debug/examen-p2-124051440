import os
import psycopg2

def cargar():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "datamart"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "secreto")
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS resultados_ingresos (
            categoria VARCHAR(50),
            mes VARCHAR(7),
            ingreso_total NUMERIC(15, 2),
            PRIMARY KEY (categoria, mes)
        );
    """)

    resultado_path = "resultado/part-00000"
    if os.path.exists(resultado_path):
        with open(resultado_path, "r") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 2:
                    key, ingreso = parts[0], float(parts[1])
                    categoria, mes = key.split("|")
                    cur.execute("""
                        INSERT INTO resultados_ingresos (categoria, mes, ingreso_total)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (categoria, mes) DO UPDATE SET ingreso_total = EXCLUDED.ingreso_total;
                    """, (categoria, mes, ingreso))
        conn.commit()
        print("Resultados cargados exitosamente a la BD.")
    else:
        print("No se encontró el archivo de salida de MapReduce.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    cargar()
