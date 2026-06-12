import cv2
import pytesseract
import re

image_path = "datasets/invoices/invoice1.png"

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)

invoice_number = re.search(
    r"INV-\d+",
    text
)

issue_date = re.search(
    r"\d{2}\.\d{2}\.\d{4}",
    text
)

#print(issue_date)

total_amount = re.search(
    r"Total\s*£?(\d+[.,]\d+)",
    text,
    re.IGNORECASE
)

if invoice_number:
    print("Invoice Number:", invoice_number.group())

if issue_date:
    print("Issue Date:", issue_date.group())

if total_amount:
    print("Total Amount:", total_amount.group())