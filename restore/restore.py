import subprocess

# === Configuración ===
BACKUP_FILE = r"C:\Users\lbadilla\Desktop\docker\odoo\restore\restore.tar.gz"

CONTAINER_ODOO = "odoo"
CONTAINER_DB   = "odoo-db"

DB_DISPLAY_NAME = "Barca"   # Nombre REAL de la BD en Postgres (con mayúscula)
DB_FILE_NAME    = "barca"   # Prefijo de los archivos del backup (en minúscula)

DB_USER = "odoo"
TMP_DIR = "/tmp/restore"


def run(cmd):
    print(f"→ Ejecutando: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print("❌ Error:", (res.stderr or res.stdout).strip())
        raise SystemExit(1)
    return (res.stdout or "").strip()


def main():
    # 1) Parar Odoo para liberar conexiones
    print("=== [1/8] Deteniendo Odoo para liberar conexiones ===")
    run(f"docker stop {CONTAINER_ODOO}")

    # 2) Preparar en Postgres y extraer SOLO para la BD
    print("=== [2/8] Preparando y extrayendo backup en contenedor Postgres ===")
    run(f"docker cp \"{BACKUP_FILE}\" {CONTAINER_DB}:/tmp/restore.tar.gz")
    run(f"docker exec {CONTAINER_DB} rm -rf {TMP_DIR}")
    run(f"docker exec {CONTAINER_DB} mkdir -p {TMP_DIR}")
    run(f"docker exec {CONTAINER_DB} tar -xzf /tmp/restore.tar.gz -C {TMP_DIR}")

    # 3) Drop/Create de la BD "Barca" (con comillas escapadas) y matar conexiones residuales
    print(f"=== [3/8] Reemplazando base de datos {DB_DISPLAY_NAME} ===")
    # matar conexiones a ambas variantes por seguridad
    run(f"docker exec -i {CONTAINER_DB} psql -U {DB_USER} -d postgres -c \"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='{DB_FILE_NAME}';\"")
    run(f"docker exec -i {CONTAINER_DB} psql -U {DB_USER} -d postgres -c \"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname='{DB_DISPLAY_NAME}';\"")

    run(f"docker exec -i {CONTAINER_DB} psql -U {DB_USER} -d postgres -c \"DROP DATABASE IF EXISTS \\\"{DB_DISPLAY_NAME}\\\";\"")
    run(f"docker exec -i {CONTAINER_DB} psql -U {DB_USER} -d postgres -c \"CREATE DATABASE \\\"{DB_DISPLAY_NAME}\\\";\"")

    # 4) Restaurar dump SQL (archivo en minúscula) dentro de "Barca"
    print("=== [4/8] Restaurando dump SQL en Postgres ===")
    run(
        f"docker exec {CONTAINER_DB} bash -c "
        f"\"gunzip -c {TMP_DIR}/db_{DB_FILE_NAME}.sql.gz | psql -U {DB_USER} \\\"{DB_DISPLAY_NAME}\\\"\""
    )

    # 5) Arrancar Odoo
    print("=== [5/8] Arrancando Odoo ===")
    run(f"docker start {CONTAINER_ODOO}")

    # 6) Preparar en Odoo y extraer TODO para filestore + addons
    print("=== [6/8] Copiando y extrayendo backup en contenedor Odoo ===")
    run(f"docker exec {CONTAINER_ODOO} rm -rf {TMP_DIR}")
    run(f"docker exec {CONTAINER_ODOO} mkdir -p {TMP_DIR}")
    run(f"docker cp \"{BACKUP_FILE}\" {CONTAINER_ODOO}:{TMP_DIR}/restore.tar.gz")
    run(f"docker exec {CONTAINER_ODOO} tar -xzf {TMP_DIR}/restore.tar.gz -C {TMP_DIR}")

    # 7) Restaurar filestore (archivo en minúscula, carpeta de destino con mayúscula)
    print("=== [7/8] Restaurando filestore y corrigiendo permisos ===")
    run(f"docker exec {CONTAINER_ODOO} rm -rf /var/lib/odoo/filestore/{DB_DISPLAY_NAME}")
    run(f"docker exec {CONTAINER_ODOO} mkdir -p /var/lib/odoo/filestore/{DB_DISPLAY_NAME}")
    run(f"docker exec {CONTAINER_ODOO} tar -xzf {TMP_DIR}/filestore_{DB_FILE_NAME}.tar.gz -C /var/lib/odoo/filestore/{DB_DISPLAY_NAME}")
    # Permisos
    run(f"docker exec {CONTAINER_ODOO} chown -R odoo:odoo /var/lib/odoo/filestore/{DB_DISPLAY_NAME}")

    # 8) Restaurar addons
    print("=== [8/8] Restaurando addons ===")
    run(f"docker exec {CONTAINER_ODOO} tar -xzf {TMP_DIR}/addons.tar.gz -C /mnt/extra-addons")

    print("✅ Listo: BD restaurada en \"{DB_DISPLAY_NAME}\", filestore cargado y addons desplegados.")


if __name__ == "__main__":
    main()
