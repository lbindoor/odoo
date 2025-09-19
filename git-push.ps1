# Agregar todos los cambios
git add .

# Pedir mensaje de commit
$mensaje = Read-Host "Mensaje del commit"
git commit -m "$mensaje"

# Subir cambios a la rama main
git push origin main
