from pyscript import document


def create_order(e):

    burger = document.getElementById("burger")
    fries = document.getElementById("fries")
    soda = document.getElementById("soda")
    iceCream = document.getElementById("iceCream")

    subtotal = (
        float(burger.value) * burger.checked
        + float(fries.value) * fries.checked
        + float(soda.value) * soda.checked
        + float(iceCream.value) * iceCream.checked
    )

    vat = subtotal * 0.12

    total = subtotal + vat

    document.getElementById("displaySubtotal").innerText = f"₱{subtotal:.2f}"
    document.getElementById("displayVat").innerText = f"₱{vat:.2f}"
    document.getElementById("displayTotal").innerText = f"₱{total:.2f}"