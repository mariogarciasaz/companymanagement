document.addEventListener("DOMContentLoaded", function () {
    const tablaResumen = document.getElementById("tabla-resumen");
    const subtotalElement = document.getElementById("subtotal");
    const vatElement = document.getElementById("vat");
    const descuentoElement = document.getElementById("descuento");
    const totalElement = document.getElementById("total");
    const agregarProductoBtn = document.getElementById("agregar-producto");

    let productos = [];
    let numeroFactura = 1;

    function actualizarTablaResumen() {
        tablaResumen.innerHTML = `
        <tr>
          <th>Cantidad</th>
          <th>Producto</th>
          <th>Precio Unidad</th>
          <th>Total</th>
        </tr>
      `;
        let subtotal = 0;

        productos.forEach((producto) => {
            const { cantidad, productoNombre, precioUnidad } = producto;
            const total = cantidad * precioUnidad;
            subtotal += total;
            tablaResumen.innerHTML += `
          <tr>
            <td>${cantidad}</td>
            <td>${productoNombre}</td>
            <td>$${precioUnidad}</td>
            <td>$${total}</td>
          </tr>
        `;
        });

        subtotalElement.innerText = subtotal.toFixed(2);
        calcularTotal(subtotal);
    }

    function calcularTotal(subtotal) {
        const vat = parseFloat(vatElement.value);
        const descuento = parseFloat(descuentoElement.value);
        const total = (subtotal * (1 + vat / 100)) - descuento;
        totalElement.innerText = total.toFixed(2);
    }

    function agregarProducto() {
        const cantidad = prompt("Ingrese la cantidad:");
        const productoNombre = prompt("Ingrese el nombre del producto:");
        const precioUnidad = prompt("Ingrese el precio unitario:");

        if (cantidad && productoNombre && precioUnidad) {
            productos.push({ cantidad, productoNombre, precioUnidad });
            actualizarTablaResumen();
        }
    }

    agregarProductoBtn.addEventListener("click", agregarProducto);

    // Llenar datos de la factura (pueden ser fijos o generarse dinámicamente)
    document.getElementById("fecha-factura").innerText = "2023-07-21";
    document.getElementById("numero-factura").innerText = numeroFactura++;
    document.getElementById("fecha-expiracion").innerText = "2023-08-21";

    // Actualizar el resumen inicialmente
    actualizarTablaResumen();

    // Escuchar cambios en los campos de VAT y Descuento para recalcular el total
    vatElement.addEventListener("input", () => calcularTotal(parseFloat(subtotalElement.innerText)));
    descuentoElement.addEventListener("input", () => calcularTotal(parseFloat(subtotalElement.innerText)));
});
