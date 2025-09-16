from datetime import date

recording_id_codes = {
    '001': 'full_word_sent',
    '004': 'word_only',
    '012': 'efirst_csent',
    '006': 'ecombo',
    '013': 'ccombo_sent',
    '014': 'cinna_sent',
    '015': 'conly_sent',
    '016': 'efirst_word_only',
}
WORD_TYPES = ['combo', 'no combo', 'two word', 'prefix', 'single char', 'suffix', 'abbreviation']
PHRASE_TYPES = ['phrase', 'part sent', 'phrase_save', 'speak_phrase', 'saying', 'idiom', 'slang', 'signs', 'signs_uncommon']
SENT_TYPES = ['sentence']
PROPER_NOUN_TYPES = ['proper noun']
IDIOM_TYPES = ['idiom']
ALL_TYPES = WORD_TYPES + PHRASE_TYPES + SENT_TYPES + PROPER_NOUN_TYPES + IDIOM_TYPES
categories_allowed_map = {'animal': ['animal'], 'food': ['food'], '': None}
date_string = date.today().strftime("%m%d")
default_settings = {
    'min_priority': 1, 'max_priority': 4,
    'min_known_english_prompt': 1, 'max_known_english_prompt': 6,
    'min_known_pinyin_prompt': 1, 'max_known_pinyin_prompt': 6,
    'sort_keys': ['category1', 'category2', 'pinyin'],
    'sort_asc': [True, True, True],
    'types_allowed': WORD_TYPES,
    'min_combo_quality': 6,
    'category_type': '',
    'cat1_values_allowed': None,
    'types_allowed_str': '',
    'min_adu': 1,
    'min_per': 1,
    'min_date': '2025-01-01',
    'filename_suffix': '',
    'contains_character': None,
    'exclude_words': None,
}

# All previous recordings
dict_recordings = [
    ### youtube
    # {
    # 'recording_id': '013', 'filename_suffix': 'food_yt',
    # 'category_type': 'animal',
    # 'min_combo_quality': 2,
    # },

    ### Refresh on Sep 1, 3
    # {
    # 'recording_id': '012', # efirst p1
    # 'min_priority': 1, 'max_priority': 1,
    # 'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '012', # efirst p2
    # 'min_priority': 2, 'max_priority': 2,
    # 'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '012', # efirst p3
    # 'min_priority': 3, 'max_priority': 3,
    # 'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '012', 'filename_suffix': '_known2', # efirst known2 p1-3
    # 'min_priority': 1, 'max_priority': 3,
    # 'min_known_english_prompt': 2, 'max_known_english_prompt': 2,
    # },
    # {
    # 'recording_id': '001', # fulle p1
    # 'min_priority': 1, 'max_priority': 1,
    # 'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '001', # fulle p2
    # 'min_priority': 2, 'max_priority': 2,
    # 'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '001', # fulle p3
    # 'min_priority': 3, 'max_priority': 3,
    # 'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '004', # wordonly p1
    # 'min_priority': 1, 'max_priority': 1,
    # 'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '004', # wordonly p2
    # 'min_priority': 2, 'max_priority': 2,
    # 'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '004', 'filename_suffix': '_phrase', # phrases p1-2
    # 'types_allowed': PHRASE_TYPES,
    # 'min_priority': 1, 'max_priority': 2,
    # 'min_known_pinyin_prompt': 2, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '004', 'filename_suffix': '_phrase', # phrases p3
    # 'types_allowed': PHRASE_TYPES,
    # 'min_priority': 3, 'max_priority': 3,
    # 'min_known_pinyin_prompt': 2, 'max_known_pinyin_prompt': 5,
    # },
    # {
    # 'recording_id': '016', 'filename_suffix': '_phrase_p1-3',
    # 'types_allowed': PHRASE_TYPES,
    # 'min_priority': 1, 'max_priority': 3,
    # 'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '016', 'filename_suffix': '_sent_p1-3',
    # 'types_allowed': SENT_TYPES,
    # 'min_priority': 1, 'max_priority': 3,
    # 'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '016', 'filename_suffix': '_propern_p1-3',
    # 'types_allowed': PROPER_NOUN_TYPES,
    # 'min_priority': 1, 'max_priority': 3,
    # 'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '013', 'filename_suffix': '_shortcombos', # for testing
    # 'min_combo_quality': 2,
    # 'min_priority': 1, 'max_priority': 1,
    # 'min_known_english_prompt': 5, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '013', 'filename_suffix': '_food_yt', # for testing
    # 'category_type': 'food',
    # 'min_combo_quality': 2,
    # 'min_priority': 1, 'max_priority': 4,
    # 'min_known_english_prompt': 1, 'max_known_english_prompt': 5,
    # 'min_adu': 3, 'min_per': 3,
    # },
    # {
    # 'recording_id': '013', 'filename_suffix': '_animal_yt', # for testing
    # 'category_type': 'animal',
    # 'min_combo_quality': 3,
    # 'min_priority': 1, 'max_priority': 4,
    # 'min_known_english_prompt': 1, 'max_known_english_prompt': 5,
    # 'min_adu': 3, 'min_per': 3,
    # },
    # {
    # 'recording_id': '006', # combos only
    # 'min_combo_quality': 4,
    # 'min_priority': 1, 'max_priority': 2,
    # 'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    # },
    # {
    # 'recording_id': '015', 'filename_suffix': '_known2', # chinese only
    # 'min_priority': 1, 'max_priority': 2,
    # 'min_known_english_prompt': 1, 'max_known_english_prompt': 2,
    # },
    # {
    # 'recording_id': '001', 'filename_suffix': '_recentAug15',
    # 'min_date': '2025-08-15',
    # 'min_priority': 1, 'max_priority': 3,
    # 'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    # },

    ### Refresh TODO
    # pinyin p1
    # TODO - finish

    ###  OLD: not planning to make regularly
    # {
    # 'recording_id': '013',
    # 'min_priority': 1,
    # 'max_priority': 4,
    # 'min_known_english_prompt': 1,
    # 'max_known_english_prompt': 5,
    # 'types_allowed_str': '',
    # 'min_combo_quality': 2,
    # 'category_type': 'animal',
    # 'sort_keys': ['category2', 'quality', 'pinyin'],
    # 'sort_asc': [True, True, True],
    # },
    # {
    # 'recording_id': '014',
    # 'types_allowed_str': '_sent',
    # 'cat1_values_allowed': ['cinna'],
    # 'sort_keys': ['id'],
    # 'sort_asc': [True],
    # },
]
