# ============================================================
#  GENERADOR DE HASH SHA-256
#  Proyecto Derecho Informatico - Hash con Python
# ============================================================

import hashlib


# ============================================================
# PARTE 2: Función para generar el hash de un texto
# ============================================================
def generar_hash(texto):
    """
    Recibe un texto (string) y devuelve su hash SHA-256.
    
    ¿Qué hace SHA-256?
    - Convierte cualquier texto en una cadena fija de 64 caracteres hexadecimales
    - El mismo texto SIEMPRE produce el mismo hash
    - Es imposible (prácticamente) obtener el texto original desde el hash
    - Si cambias UNA sola letra del texto, el hash cambia completamente
    """

    # Paso 1: Convertir el texto a bytes usando UTF-8
    # SHA-256 no trabaja con texto directamente, necesita bytes
    texto_en_bytes = texto.encode('utf-8')

    # Paso 2: Crear el objeto hash SHA-256 con el texto en bytes
    objeto_hash = hashlib.sha256(texto_en_bytes)

    # Paso 3: Obtener el hash en formato hexadecimal (cadena legible)
    # hexdigest() devuelve una cadena de 64 caracteres hexadecimales
    hash_resultado = objeto_hash.hexdigest()

    return hash_resultado


# ============================================================
# PARTE 3: Función para hashear un archivo
# ============================================================
def generar_hash_archivo(ruta_archivo):
    """
    Lee un archivo y genera su hash SHA-256.
    Útil para verificar si un archivo fue modificado.
    """
    objeto_hash = hashlib.sha256()

    # Abrimos el archivo en modo binario ('rb')
    with open(ruta_archivo, 'rb') as archivo:
        # Leemos el archivo en bloques de 65536 bytes (64 KB)
        # Esto evita cargar archivos gigantes en memoria de golpe
        while bloque := archivo.read(65536):
            objeto_hash.update(bloque)

    return objeto_hash.hexdigest()


# ============================================================
# PARTE 4: Función para comparar dos textos por su hash
# ============================================================
def verificar_hash(texto_original, hash_conocido):
    """
    Compara el hash de un texto con un hash ya conocido.
    Devuelve True si coinciden, False si no.
    
    Caso de uso real: verificar contraseñas sin guardarlas en texto plano.
    """
    hash_generado = generar_hash(texto_original)
    return hash_generado == hash_conocido


# ============================================================
# PARTE 5: Programa principal - demostración
# ============================================================
if __name__ == "__main__":

    print("=" * 60)
    print("       GENERADOR DE HASH SHA-256")
    print("=" * 60)

    # --- PRUEBA 1: Hash de un texto simple ---
    print("\n📌 PRUEBA 1: Hash de textos")
    texto1 = "Hola mundo"
    texto2 = "hola mundo"   # Misma frase pero con minúscula
    texto3 = "Hola mundo"   # Idéntico a texto1

    hash1 = generar_hash(texto1)
    hash2 = generar_hash(texto2)
    hash3 = generar_hash(texto3)

    print(f"  Texto:  '{texto1}'")
    print(f"  Hash:    {hash1}")
    print()
    print(f"  Texto:  '{texto2}'  ← solo cambió la 'H' a 'h'")
    print(f"  Hash:    {hash2}")
    print()
    print(f"  Texto:  '{texto3}'  ← idéntico al primero")
    print(f"  Hash:    {hash3}")
    print()
    print(f"  ¿Hash1 == Hash2? {hash1 == hash2}  ← pequeño cambio = hash totalmente diferente")
    print(f"  ¿Hash1 == Hash3? {hash1 == hash3}  ← textos iguales = hash idéntico")

    # --- DEMO 2: Hash de una contraseña ---
    print("\n" + "=" * 60)
    print("📌 PRUEBA 2: Simulación de contraseña hasheada")
    contrasena = "MiContrasena123!"
    hash_contrasena = generar_hash(contrasena)
    print(f"  Contraseña original: {contrasena}")
    print(f"  Hash guardado:       {hash_contrasena}")
    print(f"  (Esto es lo que guardarías en una base de datos, nunca la contraseña directa)")

    # --- PRUEBA 3: Verificación ---
    print("\n" + "=" * 60)
    print("📌 PRUEBA 3: Verificar contraseña al iniciar sesión")
    intento_correcto = "MiContrasena123!"
    intento_incorrecto = "micontrasena123!"

    print(f"  Intento '{intento_correcto}': {'✅ ACCESO PERMITIDO' if verificar_hash(intento_correcto, hash_contrasena) else '❌ ACCESO DENEGADO'}")
    print(f"  Intento '{intento_incorrecto}': {'✅ ACCESO PERMITIDO' if verificar_hash(intento_incorrecto, hash_contrasena) else '❌ ACCESO DENEGADO'}")

    # --- PRUEBA 4: Ingreso manual ---
    print("\n" + "=" * 60)
    print("📌 PRUEBA 4: Genera tu propio hash")
    mi_texto = input("  Escribe un texto para hashear: ")
    print(f"  Tu hash SHA-256: {generar_hash(mi_texto)}")
    print("=" * 60)
