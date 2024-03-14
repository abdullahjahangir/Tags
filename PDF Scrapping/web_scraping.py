import requests
from bs4 import BeautifulSoup
import json
import os


URL = (
    "https://www.iscc-system.org/certification/certificate-database/valid-certificates/"
)
JSON_FILE_PATH = "certificates_data.json"


def extract_certificate_data(table_rows):
    """
    Extract Certificate Data from Html Table
    """
    print("Total Rows: ", len(table_rows))
    certificates_data = []
    for row in table_rows:
        tds = row.find_all("td")
        status = tds[0].find("span", class_="has-tip").get("title")
        certificate_id = tds[1].text.strip()
        certificate_holder = tds[2].find("span", class_="has-tip top").text.strip()
        raw_material = tds[4].text.strip()
        add_ons = tds[5].text.strip()
        products = tds[6].text.strip()
        valid_from = tds[7].text.strip()
        valid_until = tds[8].text.strip()
        issuing_cb = tds[10].text.strip()
        certificate_link = tds[12].find("a").get("href")

        certificate_data = {
            "status": status,
            "certificate_id": certificate_id,
            "certificate_holder": certificate_holder,
            "raw_material": raw_material,
            "add_ons": add_ons,
            "products": products,
            "valid_from": valid_from,
            "valid_until": valid_until,
            "issuing_cb": issuing_cb,
            "certificate_link": certificate_link,
        }
        certificates_data.append(certificate_data)
    return certificates_data


def get_certificates_data_from_web(url):
    """
    Get The Table having certificate data from website
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", id="table_1")
    table_rows = table.find_all("tbody")[0].find_all("tr")
    return table_rows


def download_certificates(json_file):
    """
    Read a JSON file containing certificate data and download the associated PDF files.
    """
    # Open the JSON file and load the certificate data
    with open(json_file, "r") as file:
        certificates = json.load(file)

    # Create a directory to store the PDF files if it doesn't exist
    if not os.path.exists("pdfs"):
        os.makedirs("pdfs")

    # Iterate over each certificate and download the associated PDF file
    for certificate in certificates:
        pdf_url = certificate["certificate_link"]
        certificate_id = certificate["certificate_id"]
        file_path = os.path.join("pdfs", certificate_id + ".pdf")
        download_pdf_file(pdf_url, file_path)


def download_pdf_file(pdf_url, file_path):
    """
    Download the PDF file from given pdf url and stores it in given file path
    """
    # Downloading the PDF file
    response = requests.get(pdf_url)
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(response.content)


def load_certificates_data(file_path, certificates_data):
    """
    Loads certificate data into json file
    """
    with open(file_path, "w") as json_file:
        json.dump(certificates_data, json_file, indent=4)


table_rows = get_certificates_data_from_web(URL)
certificates_data = extract_certificate_data(table_rows)
load_certificates_data(JSON_FILE_PATH, certificates_data)
download_certificates(JSON_FILE_PATH)
