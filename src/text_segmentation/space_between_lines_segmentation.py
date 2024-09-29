"""
Segment paragraphs through looking at the space between the lines.
Assumption: If there's more space it's probably a new paragraph.

TODO: fix bug - last paragraphs are not being separated.
"""

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LTChar, LAParams


def extract_paragraphs_by_line_spacing(pdf_path: str, spacing_multiplier=1.5) -> list[str]:
    laparams = LAParams()
    paragraphs = []
    current_paragraph = []
    previous_bottom = None
    previous_font_size = None

    for page_layout in extract_pages(pdf_path, laparams=laparams):
        for element in page_layout:
            if isinstance(element, LTTextBox):
                for line in element:
                    if isinstance(line, LTTextLine):
                        first_char_font_size = get_font_size(line)

                        current_top = line.y1
                        current_bottom = line.y0

                        if previous_bottom is not None and previous_font_size is not None:
                            line_spacing = previous_bottom - current_top
                            dynamic_threshold = spacing_multiplier * previous_font_size

                            if line_spacing > dynamic_threshold:
                                if current_paragraph:
                                    paragraphs.append(" ".join(current_paragraph))
                                    current_paragraph = []

                        current_paragraph.append(line.get_text().strip())

                        previous_bottom = current_bottom
                        previous_font_size = first_char_font_size

        if current_paragraph:
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    return paragraphs


def get_font_size(line: LTTextLine) -> float or None:
    # TODO: refactor and remove loop, only check first char
    for char in line:
        if isinstance(char, LTChar):
            return char.size
    return None


if __name__ == "__main__":
    pdf_path = '../../test_data/five_pagers/Seiten_14_bis_18-Erlaeuterungen_Juni_DE_web.pdf'
    paragraphs = extract_paragraphs_by_line_spacing(pdf_path)

    for idx, paragraph in enumerate(paragraphs, start=1):
        print(f"Paragraph {idx}: {paragraph}\n")
