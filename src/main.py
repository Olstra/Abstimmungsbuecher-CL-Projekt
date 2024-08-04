import nltk
import pymupdf
import os


def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    try:
        doc = pymupdf.open(pdf_path)
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text


def convert_pdfs_to_text(input_folder: str, output_folder: str) -> None:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            text = extract_text_from_pdf(pdf_path)

            output_file = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_file)

            with open(output_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)


if __name__ == "__main__":
    input_data_path = "../data"
    output_data_path = "../results"

    convert_pdfs_to_text(input_data_path, output_data_path)

    nltk.sent_tokenize("TODO", language='german')
