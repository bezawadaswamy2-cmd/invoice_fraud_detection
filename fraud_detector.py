def check_fraud(invoice_data):

    subtotal = float(invoice_data["subtotal"])
    vat = float(invoice_data["vat"])
    discount = float(invoice_data["discount"])
    total = float(invoice_data["total"])

    calculated_total = subtotal + vat - discount

    if calculated_total == total:
        print("Invoice Valid")
    else:
        print("Possible Fraud Detected")

        print("Expected Total:", calculated_total)
        print("Invoice Total:", total)