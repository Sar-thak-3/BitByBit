from htmldocx import HtmlToDocx
import os

def convert_file():
    new_parser = HtmlToDocx()
    new_parser.parse_html_file("media/input.html", "media/output.docx")