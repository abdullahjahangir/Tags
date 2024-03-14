from bs4 import BeautifulSoup


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
