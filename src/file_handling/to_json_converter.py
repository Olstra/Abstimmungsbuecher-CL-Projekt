from datetime import datetime

import pandas as pd

from src.common.data_paths import JSON_OUTPUT_DIR


def write_to_json(sentences: list[str], lang: str) -> None:
    df = pd.DataFrame({
        "id": range(1, len(sentences) + 1),
        "content": sentences
    })

    output_file = f"{JSON_OUTPUT_DIR}/{datetime.now():%m.%d-%H:%M:%S}-output-test-{lang}.json"

    df.to_json(output_file, orient="records", lines=False, force_ascii=False, indent=4)
