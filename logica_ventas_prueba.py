from datetime import datetime
import random

def finalizar_venta(
    venta_actual,
    opcion_pago,
    cuotas=None,
    monto_cliente=None
):

    if not venta_actual:
        return {
            "ok": False,
            "error": "Venta vacía"
        }

    total_base = sum(p["subtotal"] for p in venta_actual)
    total_final = total_base
    mensaje_recargo = "No se aplicaron modificaciones."
    error = None
    pago_cuota = None 
    vuelto = 0.0



    if opcion_pago == "Efectivo":
        try:
            f=open("descuento_efectivo.txt","r")
            porcentaje=f.read().strip()
            descuento = total_base* float(porcentaje)
            total_final = total_base - descuento
            mensaje_recargo = f"Descuento efectivo (10%): -${descuento:.2f}"
        except FileNotFoundError:
            mensaje_error="Error, comuniquese con soporte"
        f.close()

    elif opcion_pago == "Billetera virtual":
        descuento = total_base * 0.10
        total_final = total_base - descuento
        mensaje_recargo = f"Descuento B. virtual (10%): -${descuento:.2f}"

    elif opcion_pago == "Tarjeta de crédito":
        try:
            cuotas = int(cuotas)
            interes = 0.0
            if cuotas == 3:
                interes = 0.03
            elif cuotas == 6:
                interes = 0.05
            elif cuotas == 12:
                interes = 0.08
            else:
                raise ValueError

            recargo = total_base * interes
            total_final = total_base + recargo
            porcentaje = int(interes * 100)
            pago_cuota = round(total_final / cuotas, 2)
            mensaje_recargo = (
                f"Recargo {cuotas} cuotas ({porcentaje}%): +${recargo:.2f}\n"
                f"Pago en {cuotas} cuotas de ${pago_cuota:.2f}"
            )
        except (ValueError, TypeError):
            # Igual que en tu original: si las cuotas son inválidas,
            # se vuelve al total base sin recargos.
            total_final = total_base
            mensaje_recargo = "No se aplicaron recargos (Cuotas inválidas)."

    elif opcion_pago == "Débito":
        mensaje_recargo = "Pago con débito. Sin recargos."

    # --- Gestión de vuelto / monto del cliente ---

    vuelto = 0.0

    if opcion_pago == "Efectivo":
        if monto_cliente is None:
            return {
                "ok": False,
                "error": "Monto no informado",
                "total_base": total_base,
                "total_final": total_final,
            }

        try:
            monto = float(monto_cliente)
            if monto < total_final:
                return {
                    "ok": False,
                    "error": "Monto insuficiente",
                    "total_base": total_base,
                    "total_final": total_final,
                    "monto_cliente": monto,
                }
            else:
                vuelto = monto - total_final
        except (ValueError, TypeError):
            return {
                "ok": False,
                "error": "Monto ingresado no válido",
                "total_base": total_base,
                "total_final": total_final,
            }

    else:
        monto = total_final
        vuelto = 0.0


    nueva_venta_dict = {
        "id_venta": datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(100, 999)),
        "fecha_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "productos": list(venta_actual),  # copia
        "total_base": total_base,
        "total_final": total_final,
        "metodo_pago": opcion_pago,
        "monto_cliente": monto,
        "vuelto": vuelto,
        "mensaje_recargo": mensaje_recargo,
    }

    return {
        "ok": True,
        "error": error,
        "total_base": total_base,
        "total_final": total_final,
        "monto_cliente": monto,
        "vuelto": vuelto,
        "pago_cuota": pago_cuota,
        "mensaje_recargo": mensaje_recargo,
        "venta_dict": nueva_venta_dict,
    }
