from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LAParams, LTChar


def extract_headers_and_paragraphs(pdf_path: str) -> (list[str], list[str]):
    laparams = LAParams()
    headers = []
    paragraphs = []

    for page_layout in extract_pages(pdf_path, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                paragraph = ""
                header = ""

                for line in element:
                    if isinstance(line, LTTextLine):
                        for char in line:
                            if isinstance(char, LTChar):
                                current_font_name = char.fontname

                        if current_font_name is not None and 'Bold' in current_font_name:
                            header += line.get_text()
                        else:
                            paragraph += line.get_text()

                headers.append(header)
                paragraphs.append(paragraph)

    return headers, paragraphs


if __name__ == "__main__":
    input_data_path = "../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_RM_web.pdf"
    output_json_path = "results/result.json"
    headers, paragraphs = extract_headers_and_paragraphs(input_data_path)

    print("Headers:")
    for header in headers:
        header.strip()
    print(list(filter(None, headers)))

    print("\nParagraphs:")
    new_paragraphs = []
    for paragraph in paragraphs:
        paragraph.strip()
        # if paragraph.strip() is not None:
        #     print("+++",paragraph)
    print(list(filter(None, paragraphs)))