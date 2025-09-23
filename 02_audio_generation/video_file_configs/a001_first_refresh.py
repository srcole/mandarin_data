from PIL import ImageFont
from constants import WORD_TYPES, PHRASE_TYPES, SENT_TYPES, PROPER_NOUN_TYPES, IDIOM_TYPES, ALL_TYPES

dict_recordings = [
    ### English first: P1, P2, P3, Known
    {
    'recording_id': '012', # efirst p1
    'min_priority': 1, 'max_priority': 1,
    'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '012', # efirst p2
    'min_priority': 2, 'max_priority': 2,
    'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '012', # efirst p3
    'min_priority': 3, 'max_priority': 3,
    'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '012', 'filename_suffix': '_known2', # efirst known2 p1-3
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 2,
    },

    # Full: P1, P2, P3
    {
    'recording_id': '001', # fulle p1
    'min_priority': 1, 'max_priority': 1,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '001', # fulle p2
    'min_priority': 2, 'max_priority': 2,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '001', # fulle p3
    'min_priority': 3, 'max_priority': 3,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '004', # wordonly p1
    'min_priority': 1, 'max_priority': 1,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '004', # wordonly p2
    'min_priority': 2, 'max_priority': 2,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '004', 'filename_suffix': '_phrase', # phrases p1-2
    'types_allowed': PHRASE_TYPES,
    'min_priority': 1, 'max_priority': 2,
    'min_known_pinyin_prompt': 2, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '004', 'filename_suffix': '_phrase', # phrases p3
    'types_allowed': PHRASE_TYPES,
    'min_priority': 3, 'max_priority': 3,
    'min_known_pinyin_prompt': 2, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': '016', 'filename_suffix': '_phrase_p1-3',
    'types_allowed': PHRASE_TYPES,
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '016', 'filename_suffix': '_sent_p1-3',
    'types_allowed': SENT_TYPES,
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '016', 'filename_suffix': '_propern_p1-3',
    'types_allowed': PROPER_NOUN_TYPES,
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '006', # combos only
    'min_combo_quality': 4,
    'min_priority': 1, 'max_priority': 2,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '015', 'filename_suffix': '_known2', # chinese only
    'min_priority': 1, 'max_priority': 2,
    'min_known_english_prompt': 1, 'max_known_english_prompt': 2,
    },
    {
    'recording_id': '001', 'filename_suffix': '_recentAug15',
    'min_date': '2025-08-15',
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },

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
