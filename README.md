# Examen Segundo Parcial - Pipeline de datos contenerizado

- Alumno: Citlali Jocelyn Martínez
- Matrícula: 124051440
- Pregunta de negocio: Ingreso total (cantidad x precio_unitario) por categoría y mes (Dígito: 0 o 1).

## Pasos para reproducir
1. Clona el repositorio.
2. Configura tu archivo .env basado en .env.example.
3. Levanta todo el ambiente con el comando: docker compose up --build
4. Ejecuta el procesamiento de Hadoop y la carga a la base de datos.

## Comparativa de rendimiento
El script secuencial fue más rápido en este escenario de 400 MB debido a que evita el overhead de inicialización de la máquina virtual Java (JVM) y la fase de shuffle de MapReduce, la cual está diseñada para clústeres distribuidos masivos.

## Parte E: Respuestas Teóricas
1. Modos de Hadoop: Standalone (un proceso Java local), Pseudo-distribuido (todos los demonios en una máquina con HDFS) y Totalmente distribuido (clúster multi-nodo). HDFS se usa en los modos pseudo-distribuido y totalmente distribuido.
2. Volumen vs COPY: Evita inflar el tamaño de la imagen Docker con 400 MB y permite desacoplar los datos para procesar distintos archivos sin recompilar.
3. docker compose down vs down -v: down elimina contenedores y red manteniendo los datos en el volumen; down -v elimina también el volumen causando pérdida permanente de datos.
4. MapReduce vs Secuencial: MapReduce genera sobrecarga en archivos pequeños (como 400 MB). Conviene cuando los datos superan la RAM de un solo nodo.
5. CMD vs ENTRYPOINT y COPY vs ADD: ENTRYPOINT fija el comando principal, CMD da argumentos por defecto. COPY copia localmente y ADD extrae comprimidos o descarga URLs.
