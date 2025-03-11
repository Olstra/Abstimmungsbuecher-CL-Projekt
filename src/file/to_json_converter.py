import json

from src.common.data_paths import JSON_OUTPUT_DIR


def write_to_json(sentences: list[str], lang: str) -> None:
    output_list = []
    for i, content in enumerate(sentences, start=1):
        output_list.append({
            "id": i,
            "content": content
        })

    output_file = f"{JSON_OUTPUT_DIR}/output-test-{lang}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(output_list, file, ensure_ascii=False, indent=4)
