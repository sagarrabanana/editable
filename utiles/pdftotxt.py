import pdfminer.high_level
from pdfminer.layout import LAParams

def convert_pdf_to_html(pdf_path, html_path):
    laparams = LAParams()
    with open(html_path, 'wb') as html_file:
        with open(pdf_path, 'rb') as pdf_file:
            pdfminer.high_level.extract_text_to_fp(pdf_file, html_file, laparams=laparams, output_type='html')

convert_pdf_to_html('pdf input path', 'html output path')