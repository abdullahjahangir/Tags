import requests
from bs4 import BeautifulSoup
import json
import os


URL = (
    "https://www.iscc-system.org/wp-admin/admin-ajax.php?action=get_wdtable&table_id=4"
)
JSON_FILE_PATH = "certificates_data.json"

form_data = {
    "columns[0][data]": "0",
    "columns[0][name]": "cert_ikon",
    "columns[0][searchable]": "true",
    "columns[0][orderable]": "true",
    "columns[0][search][value]": "",
    "columns[0][search][regex]": "false",
    "columns[1][data]": "1",
    "columns[1][name]": "cert_number",
    "columns[1][searchable]": "true",
    "columns[1][orderable]": "true",
    "columns[1][search][value]": "",
    "columns[1][search][regex]": "false",
    "columns[2][data]": "2",
    "columns[2][name]": "cert_owner",
    "columns[2][searchable]": "true",
    "columns[2][orderable]": "true",
    "columns[2][search][value]": "",
    "columns[2][search][regex]": "false",
    "columns[3][data]": "3",
    "columns[3][name]": "cert_certified_as",
    "columns[3][searchable]": "true",
    "columns[3][orderable]": "true",
    "columns[3][search][value]": "",
    "columns[3][search][regex]": "false",
    "columns[4][data]": "4",
    "columns[4][name]": "cert_in_put",
    "columns[4][searchable]": "true",
    "columns[4][orderable]": "true",
    "columns[4][search][value]": "",
    "columns[4][search][regex]": "false",
    "columns[5][data]": "5",
    "columns[5][name]": "cert_add_on",
    "columns[5][searchable]": "true",
    "columns[5][orderable]": "true",
    "columns[5][search][value]": "",
    "columns[5][search][regex]": "false",
    "columns[6][data]": "6",
    "columns[6][name]": "cert_products",
    "columns[6][searchable]": "true",
    "columns[6][orderable]": "true",
    "columns[6][search][value]": "",
    "columns[6][search][regex]": "false",
    "columns[7][data]": "7",
    "columns[7][name]": "cert_valid_from",
    "columns[7][searchable]": "true",
    "columns[7][orderable]": "true",
    "columns[7][search][value]": "",
    "columns[7][search][regex]": "false",
    "columns[8][data]": "8",
    "columns[8][name]": "cert_valid_until",
    "columns[8][searchable]": "true",
    "columns[8][orderable]": "true",
    "columns[8][search][value]": "",
    "columns[8][search][regex]": "false",
    "columns[9][data]": "9",
    "columns[9][name]": "cert_suspended_date",
    "columns[9][searchable]": "true",
    "columns[9][orderable]": "true",
    "columns[9][search][value]": "",
    "columns[9][search][regex]": "false",
    "columns[10][data]": "10",
    "columns[10][name]": "cert_issuer",
    "columns[10][searchable]": "true",
    "columns[10][orderable]": "true",
    "columns[10][search][value]": "",
    "columns[10][search][regex]": "false",
    "columns[11][data]": "11",
    "columns[11][name]": "cert_map",
    "columns[11][searchable]": "true",
    "columns[11][orderable]": "true",
    "columns[11][search][value]": "",
    "columns[11][search][regex]": "false",
    "columns[12][data]": "12",
    "columns[12][name]": "cert_file",
    "columns[12][searchable]": "true",
    "columns[12][orderable]": "true",
    "columns[12][search][value]": "",
    "columns[12][search][regex]": "false",
    "columns[13][data]": "13",
    "columns[13][name]": "cert_audit",
    "columns[13][searchable]": "true",
    "columns[13][orderable]": "true",
    "columns[13][search][value]": "",
    "columns[13][search][regex]": "false",
    "columns[14][data]": "14",
    "columns[14][name]": "cert_status",
    "columns[14][searchable]": "true",
    "columns[14][orderable]": "true",
    "columns[14][search][value]": "",
    "columns[14][search][regex]": "false",
    "order[0][column]": "8",
    "order[0][dir]": "desc",
    "start": "10",
    "length": "10",
    "search[value]": "",
    "search[regex]": "false",
    "wdtNonce": "2ea7ba4970",
    "sRangeSeparator": "|",
}


def load_certificates_data(file_path, certificates_data):
    """
    Loads certificate data into json file
    """
    print("Total Count: ", len(certificates_data))
    with open(file_path, "w") as json_file:
        json.dump(certificates_data, json_file, indent=4)


def download_pdf_file(pdf_url, file_path):
    """
    Download the PDF file from given pdf url and stores it in given file path
    """
    # Downloading the PDF file
    response = requests.get(pdf_url)
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(response.content)


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


def call_api(max_draw):
    certificates_data = []
    # Form data
    for i in range(1, max_draw + 1):

        print("Page#: ", i)
        form_data["draw"] = str(i)
        response = requests.post(URL, data=form_data)

        # Checking if the request was successful
        if response.status_code == 200:
            print("\t*** Request successful! ***")
            print(
                "response.text: ",
                response,
                response.headers["content-type"],
                response.headers["content-length"],
                form_data,
            )
            parsed_data = get_parsed_content(response.text)
            print("\t*** Page Length: ", len(parsed_data["data"]), " ***")
            for row in parsed_data["data"]:
                certificate_data = get_certificate_data(row)
                certificates_data.append(certificate_data)
        else:
            print("Request failed with status code:", response.status_code)
    return certificates_data


def get_certificate_data(row):
    status = get_status(row[0])
    certificate_id = get_text(row[1])
    certificate_holder = get_certificate_holder(row[2])
    scope = get_text(row[3])
    raw_material = get_text(row[4])
    adds_on = get_text(row[5])
    product = get_text(row[6])
    valid_from = get_text(row[7])
    valid_until = get_text(row[8])
    suspend = get_suspend(row[9])
    issuing_cb = get_text(row[10])
    map = get_href(row[11])
    certificate_link = get_href(row[12])
    audit_link = get_href(row[13])
    certificate_data = {
        "status": status,
        "certificate_id": certificate_id,
        "certificate_holder": certificate_holder,
        "scope": scope,
        "raw_material": raw_material,
        "adds_on": adds_on,
        "product": product,
        "valid_from": valid_from,
        "valid_until": valid_until,
        "suspend": suspend,
        "issuing_cb": issuing_cb,
        "map": map,
        "certificate_link": certificate_link,
        "audit_link": audit_link,
    }
    return certificate_data


def get_parsed_content(html_content):
    start_index = html_content.find("{")
    end_index = html_content.rfind("}") + 1

    # Extract the JSON data from the HTML content
    json_data = html_content[start_index:end_index]

    # Parse the JSON data
    parsed_data = json.loads(json_data)
    return parsed_data


def get_href(html):
    href = None
    if isinstance(html, str):
        try:
            href = BeautifulSoup(html, "html.parser").find("a")["href"]
        except:
            href = html
    return href


def get_status(html):
    status = None
    if isinstance(html, str):
        soup = BeautifulSoup(html, "html.parser")
        span_tags = soup.find_all("span")

        if len(span_tags) >= 2:
            last_span = span_tags[-1]
            status = last_span.get("title")
        elif len(span_tags) == 1:
            status = span_tags[0].get("title")

    return status


def get_certificate_holder(html):
    certificate_holder = None
    if isinstance(html, str):
        try:
            certificate_holder = (
                BeautifulSoup(html, "html.parser")
                .find("span", class_="has-tip top")
                .text.strip()
            )
        except:
            certificate_holder = html
    return certificate_holder


def get_text(html):
    valid_from = None
    if isinstance(html, str):
        try:
            valid_from = BeautifulSoup(html, "html.parser").text.strip()
        except:
            valid_from = html
    return valid_from


def get_suspend(html):
    valid_from = None
    if isinstance(html, str):
        _from, _until = "", ""
        try:
            _from = (
                BeautifulSoup(html, "html.parser")
                .find("span", class_="cert_suspended_from")
                .text.strip()
            )
            _until = (
                BeautifulSoup(html, "html.parser")
                .find("span", class_="cert_suspended_until")
                .text.strip()
            )
            valid_from = _from + _until
        except:
            valid_from = html
    return valid_from


if __name__ == "__main__":
    certificates_data = call_api(10)
    load_certificates_data(JSON_FILE_PATH, certificates_data)
    # download_cerztificates(JSON_FILE_PATH)
