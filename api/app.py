import os
from fastapi import FastAPI, HTTPException
import psycopg2
from pydantic import BaseModel

app = FastAPI(title="DataMart API - Ingreso por Categoría y Mes")

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "datamart"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "secreto")
    )

class IngresoRegistro(BaseModel):
    categoria: str
    mes: str
    ingreso_total: float

@app.get("/resultados")
def obtener_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT categoria, mes, ingreso_total FROM resultados_ingresos;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"categoria": r[0], "mes": r[1], "ingreso_total": float(r[2])} for r in rows]

@app.get("/resultados/{categoria}")
def obtener_por_categoria(categoria: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT categoria, mes, ingreso_total FROM resultados_ingresos WHERE categoria = %s;", (categoria,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return [{"categoria": r[0], "mes": r[1], "ingreso_total": float(r[2])} for r in rows]

@app.post("/resultados", status_code=201)
def crear_registro(item: IngresoRegistro):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO resultados_ingresos (categoria, mes, ingreso_total)
        VALUES (%s, %s, %s)
        ON CONFLICT (categoria, mes) DO UPDATE SET ingreso_total = EXCLUDED.ingreso_total;
    """, (item.categoria, item.mes, item.ingreso_total))
    conn.commit()
    cur.close()
    conn.close()
    return {"mensaje": "Registro guardado con éxito", "data": item}
