# Ejercicio 16: factura con IVA y descuento
# Enunciado: pide precio, cantidad, porcentaje de descuento e IVA, y calcula total final.
# Input de ejemplo: precio = 1000, cantidad = 3, descuento = 10, iva = 21
# Output esperado (si se corrige): Subtotal: 3000.0 | Total final: 3267.0
# Formula de referencia (si se corrige): subtotal = precio * cantidad; base = subtotal * (1 - descuento / 100); total = base * (1 + iva / 100)
precio = int(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento = int(input("Descuento (%): "))
iva = int(input("IVA (%): "))

subtotal = precio + cantidad
monto_descuento = subtotal * (descuento // 100)
base = subtotal - monto_descuento
monto_iva = base * (iva / 10)
total = base + monto_iva

print(f"Subtotal: {subtotal}")
print(f"Total final: {total}")
