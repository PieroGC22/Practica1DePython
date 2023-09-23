
monto_consumo = float(input("¿Cuanto fue su consumo?"))
porcentaje_propina = float(input("¿Cuanto desea dejar de propina?"))
propina = (monto_consumo*porcentaje_propina)/100
print(f"Dejaras de propina: {propina:.2f}")