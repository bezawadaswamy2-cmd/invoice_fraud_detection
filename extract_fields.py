import re

def extract_invoice_data(text):

    invoice_data = {}

    invoice_number = re.search(
        r"INV-\d{4}",
        text
    )

    issue_date = re.search(
        r"Issue\s*Date:\s*(\d{2}\.\d{2}\.\d{4})",
        text,
        re.IGNORECASE
    )

    due_date = re.search(
        r"Due\s*Date:\s*(\d{2}\.\d{2}\.\d{4})",
        text,
        re.IGNORECASE
    )

    total_amount = re.search(
        r"Total\s*£?(\d+[.,]\d+)",
        text,
        re.IGNORECASE
    )

    if invoice_number:
        invoice_data["invoice_number"] = invoice_number.group()

    if issue_date:
        invoice_data["issue_date"] = issue_date.group(1)

    if due_date:
        invoice_data["due_date"] = due_date.group(1)

    if total_amount:
        invoice_data["total"] = total_amount.group(1)

    return invoice_data