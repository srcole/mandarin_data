from PIL import ImageFont
from constants import WORD_TYPES, PHRASE_TYPES, SENT_TYPES, PROPER_NOUN_TYPES, IDIOM_TYPES, ALL_TYPES

dict_recordings = [
    ### English first, with sent: P1, P2, P3, Known
    {
    'recording_id': 'ec_csent', 'filename_suffix': 'efirst_p1_k345',
    'min_priority': 1, 'max_priority': 1,
    'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': 'ec_csent', 'filename_suffix': 'efirst_p2_k345',
    'min_priority': 2, 'max_priority': 2,
    'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': 'ec_csent', 'filename_suffix': 'efirst_p3_k345',
    'min_priority': 3, 'max_priority': 3,
    'min_known_english_prompt': 3, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': 'ec_csent', 'filename_suffix': '_p123_k2',
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 2,
    },

    # Full: P1, P2, P3
    {
    'recording_id': 'ce_wordsent', 'filename_suffix': '_p1_k345',
    'min_priority': 1, 'max_priority': 1,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': 'ce_wordsent', 'filename_suffix': '_p2_k345',
    'min_priority': 2, 'max_priority': 2,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },
    {
    'recording_id': 'ce_wordsent', 'filename_suffix': '_p3_k345',
    'min_priority': 3, 'max_priority': 3,
    'min_known_pinyin_prompt': 3, 'max_known_pinyin_prompt': 5,
    },

    # English first, phrase only
    {
    'recording_id': '016', 'filename_suffix': '_phrase_p123',
    'types_allowed': PHRASE_TYPES,
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '016', 'filename_suffix': '_sent_p123',
    'types_allowed': SENT_TYPES,
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
    {
    'recording_id': '016', 'filename_suffix': '_propern_p123',
    'types_allowed': PROPER_NOUN_TYPES,
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },

    # Combos
    {
    'recording_id': '006', 'filename_suffix': '_goodcombos_p12_k2345',
    'min_combo_quality': 4,
    'min_priority': 1, 'max_priority': 2,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },

    # Chinese only, known
    {
    'recording_id': 'cn_only_sent', 'filename_suffix': '_known2',
    'min_priority': 1, 'max_priority': 2,
    'min_known_english_prompt': 1, 'max_known_english_prompt': 2,
    },

    # Special sets: recent
    {
    'recording_id': '001', 'filename_suffix': '_recentAug15',
    'min_date': '2025-08-15',
    'min_priority': 1, 'max_priority': 3,
    'min_known_english_prompt': 2, 'max_known_english_prompt': 5,
    },
]
