from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import subprocess
import platform

def create_pdf(records, user_info, creation_date):
    # Create a PDF file
    pdf_file = "output.pdf"

    c = canvas.Canvas(pdf_file, pagesize=letter)
    # add date to page
    c.setFont("Helvetica", 10)
    c.drawString(500, 750, creation_date)
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, f"Ad Soyad: {user_info.get('ad')} {user_info.get('soyad')}")
    c.drawString(50, 730, f"Sicil No: {user_info.get('sicil')}")
    # add date top of the page
    # title of the page
    c.setFont("Helvetica", 16)
    c.drawString(250, 700, "Kitap Teslimat Raporu")
    # headers of the table of data.
    c.setFont("Helvetica", 12)
    c.drawString(50, 650, 'Kitap Adi')
    c.drawString(250, 650, 'Durumu')
    c.drawString(350, 650, 'Teslim Tarihi')
    c.drawString(500, 650, 'Iade Tarihi')
    c.setFont("Helvetica", 10)
    y = 630 # max height size is 800
    for line in records: 
        x = 50
        c.drawString(x, y, line.get('title'))
        x += 200
        c.drawString(x, y, line.get('status'))
        x += 100
        c.drawString(x, y, line.get('lent_date'))
        x += 150
        c.drawString(x, y, line.get('returned_date'))
        y -= 20  # Adjust the y-coordinate for the next line
    
    c.showPage()
    c.save()

    # Open the PDF file for printing based on the platform
    current_platform = platform.system()
    if current_platform == "Windows":
        subprocess.Popen(["start", "", pdf_file], shell=True)
    elif current_platform == "Darwin":
        subprocess.Popen(["open", pdf_file])
    else:
        print("Printing on this platform is not supported by this script. Please open the PDF manually.")

