from types import SimpleNamespace

CH_LANG_CODES = {
    'DE': 'de_CH',
    'FR': 'fr_CH',
    'IT': 'it_CH',
    'RM': 'rm_CH'
}

# ch_langs = SimpleNamespace(**{
#     'DE': 'de_CH',
#     'FR': 'fr_CH',
#     'IT': 'it_CH',
#     'RM': 'rm_CH'
# })

# TODO:
# # Example dictionary
# my_dict = {'de': [], 'fr': [], 'it': []}
#
# # Convert dictionary to SimpleNamespace
# my_namespace = SimpleNamespace(**my_dict)

if __name__ == '__main__':
    print(CH_LANG_CODES['DE'])
    for lang, lang_code in CH_LANG_CODES.items():
        print(lang, lang_code)
