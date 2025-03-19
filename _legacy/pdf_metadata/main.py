import json

from src.nlp.splitter.pdf_metadata_analysis.space_between_lines_segmentation import extract_paragraphs_by_line_spacing

if __name__ == "__main__":
    language = "IT"  # DE, RM, FR, IT
    input_data_path = f"../test_data/Erlaeuterungen_Juni_{language}_web.pdf"
    result = extract_paragraphs_by_line_spacing(input_data_path)

    output_list = []
    for idx, content in enumerate(result, start=1):
        output_list.append({
            "id": idx,
            "language": language,
            "content": content
        })

    output_file = f"../results/line_spacing/01-Full-{language}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_list, f, ensure_ascii=False, indent=4)
