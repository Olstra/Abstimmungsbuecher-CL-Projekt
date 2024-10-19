import json


def extract_to_json(input: list):
    lang1_sentences = []
    lang2_sentences = []

    for e in input:
        lang1 = e[0]
        lang2 = e[1]

        lang1_sentences.append(lang1)
        lang2_sentences.append(lang2)

    write_to_json(lang1_sentences, 'lang1')
    write_to_json(lang2_sentences, 'lang2')


def write_to_json(input: list, lang: str) -> None:
    output_list = []
    for idx, content in enumerate(input, start=1):
        output_list.append({
            "id": idx,
            "language": "TODO",
            "content": content
        })

    output_file = f"../results/output-test-{lang}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_list, f, ensure_ascii=False, indent=4)
