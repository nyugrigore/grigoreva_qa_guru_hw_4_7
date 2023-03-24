import os
from zipfile import ZipFile
import pytest


@pytest.fixture()
def zip_files():
    csv_file = "SampleCSVFile_2kb.csv"
    xlsx_file = "file_example_XLSX_50.xlsx"
    pdf_file = "file-sample_150kB.pdf"
    res_path = os.path.abspath("resources")
    csv_path = os.path.join(res_path, csv_file)
    xlsx_path = os.path.join(res_path, xlsx_file)
    pdf_path = os.path.join(res_path, pdf_file)

    with ZipFile("resources/archive.zip", "w") as arch:
        arch.write(f'{csv_path}', csv_file)
        arch.write(f'{pdf_path}', pdf_file)
        arch.write(f'{xlsx_path}', xlsx_file)

