import json

from src.text_segmentation.font_difference_segmentation import extract_by_font_difference
from src.text_segmentation.space_between_lines_segmentation import extract_paragraphs_by_line_spacing
from src.text_segmentation.textbox_segmentation import extract_text_boxes

if __name__ == "__main__":
    language = "IT"  # DE, RM, FR, IT
    input_data_path = f"../test_data/five_pagers/Seiten_24_bis_28-Erlaeuterungen_Juni_{language}_web.pdf"
    result = extract_paragraphs_by_line_spacing(input_data_path)

    output_list = []
    for idx, content in enumerate(result, start=1):
        output_list.append({
            "id": idx,
            "language": language,
            "content": content
        })

    output_file = f"../results/line_spacing/Seiten_24_bis_28-{language}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_list, f, ensure_ascii=False, indent=4)
