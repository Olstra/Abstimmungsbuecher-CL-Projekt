from src.common.ch_languages import CH_LANG_CODES


def create_sentences_per_lang_container() -> dict:
    return { lang: [] for lang in CH_LANG_CODES.keys() }
