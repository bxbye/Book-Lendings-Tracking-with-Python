from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import subprocess
import platform

def create_pdf(text_lines):
    # Create a PDF file
    pdf_file = "output.pdf"

    c = canvas.Canvas(pdf_file, pagesize=letter)
    
    # add date top of the page
    
    # Set the starting y-coordinate for text
    y = 750
    # Write each line of text
    for line in text_lines:
        c.drawString(100, y, line)
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

