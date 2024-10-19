"""
Extract different paragraphs by dividing text into sub-elements that have the same font attributes.
TODO: what to do if a paragraphs encompasses multiple pages?
"""

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LAParams, LTChar


def extract_by_font_difference(pdf_path: str) -> list[str]:
    laparams = LAParams()
    paragraphs = []
    current_paragraph = []
    previous_font = None
    previous_size = None

    for page_layout in extract_pages(pdf_path, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                for line in element:
                    if isinstance(line, LTTextLine):
                        first_char_font = None
                        first_char_size = None

                        for char in line:
                            if isinstance(char, LTChar):
                                first_char_font = char.fontname
                                first_char_size = char.size
                                break

                        if (previous_font is None or first_char_font == previous_font) and \
                                (previous_size is None or first_char_size == previous_size):
                            current_paragraph.append(line.get_text().strip())
                        else:
                            if current_paragraph:
                                paragraphs.append(" ".join(current_paragraph))
                            current_paragraph = [line.get_text().strip()]

                        previous_font = first_char_font
                        previous_size = first_char_size

        if current_paragraph:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    return paragraphs


if __name__ == "__main__":
    input_data_path = "../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_DE_web.pdf"
    output_json_path = "../results/result.json"
    output = extract_by_font_difference(input_data_path)

    print(output)
