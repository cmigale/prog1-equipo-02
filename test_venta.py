from logica_ventas_prueba import finalizar_venta


def test_efectivo_con_descuento_y_vuelto():
    venta_actual = [{"subtotal": 1500.0}]

    resultado = finalizar_venta(
        venta_actual=venta_actual,
        opcion_pago="Efectivo",
        cuotas=None,
        monto_cliente=2000.0,
    )

    assert resultado["ok"] is True
    assert resultado["total_base"] == 1500.0
    assert resultado["total_final"] == 1350.0    
    assert resultado["vuelto"] == 650.0          
    assert "Descuento efectivo" in resultado["mensaje_recargo"]


def test_billetera_virtual():
    venta_actual = [{"subtotal": 1500.0}]

    resultado = finalizar_venta(
        venta_actual=venta_actual,
        opcion_pago="Billetera virtual",
        cuotas=None,
        monto_cliente=None,
    )

    assert resultado["ok"] is True
    assert resultado["total_base"] == 1500.0
    assert resultado["total_final"] == 1350.0   
    assert "B. virtual" in resultado["mensaje_recargo"]
    assert resultado["vuelto"] == 0.0             


def test_debito_sin_recargo():
    venta_actual = [{"subtotal": 1500.0}]

    resultado = finalizar_venta(
        venta_actual=venta_actual,
        opcion_pago="Débito",
        cuotas=None,
        monto_cliente=None,
    )

    assert resultado["ok"] is True
    assert resultado["total_base"] == 1500.0
    assert resultado["total_final"] == 1500.0    # sin recargo
    assert "débito" in resultado["mensaje_recargo"].lower()
    assert resultado["vuelto"] == 0.0


def test_credito_6_cuotas():
    venta_actual = [{"subtotal": 1500.0}]

    resultado = finalizar_venta(
        venta_actual=venta_actual,
        opcion_pago="Tarjeta de crédito",
        cuotas=6,
        monto_cliente=None,
    )

    assert resultado["ok"] is True
    assert resultado["total_base"] == 1500.0
    assert resultado["total_final"] == 1575.0        # 1500 + 5%
    assert resultado["pago_cuota"] == 262.5          # 1575 / 6
    assert "6 cuotas" in resultado["mensaje_recargo"]
