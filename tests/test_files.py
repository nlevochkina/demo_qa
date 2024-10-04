import os
import zipfile
import unittest
import openpyxl
import pandas as pd

from pypdf import PdfReader

path = os.path.dirname(os.path.abspath(__file__))
path_to_tmp = os.path.abspath(os.path.join(path, '..', 'tmp'))
path_to_archive = os.path.abspath(os.path.join(path_to_tmp, 'files_zip.zip'))


class TestsFiles(unittest.TestCase):

    def test_add_files_to_zip(self):
        with zipfile.ZipFile(path_to_archive, 'w') as zf:
            files_to_add = ['pdf_file.pdf', 'xlsx_file.xlsx', 'csv_file.csv']
            for file in files_to_add:
                add_file = os.path.join(path_to_tmp, file)
                if os.path.exists(add_file):
                    zf.write(add_file, os.path.basename(add_file))
                print(add_file)

    def test_read_csv_file(self):
        with zipfile.ZipFile(path_to_archive, 'r') as zf:
            with zf.open('csv_file.csv') as csv_file:
                content = csv_file.read().decode('utf-8-sig')
                print(content)

    def test_read_pdf_file(self):
        with zipfile.ZipFile(path_to_archive, 'r') as zf:
            with zf.open('pdf_file.pdf') as pdf_file:
                reader = PdfReader(pdf_file)
                print(reader.pages[0].extract_text())

    def test_read_xlsx_file(self):
        with zipfile.ZipFile(path_to_archive, 'r') as zf:
            with zf.open('xlsx_file.xlsx') as xlsx:
                xlsx_file = pd.read_excel(xlsx)
                print(xlsx_file)

    if test_add_files_to_zip == '__main__':
        unittest.main()
