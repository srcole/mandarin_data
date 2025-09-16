from PIL import ImageFont

# Basic video info
making_video = True
video_number = '2'
subtitle_1 = {'chinese': '词汇细分', 'pinyin': 'Cíhuì xìfēn', 'english': 'Vocabulary breakdown'}
subtitle_2 = {'chinese': '动物', 'pinyin': 'Dòngwù', 'english': 'Animals'}

# Video configs
hanzi_font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
TEXT_COLOR = 'black'
BG_COLOR = 'white'
BG_SIZE = (1280, 720)
TEXT_SPACING = 30
TEXT_SPACING_COMPONENTS = 15
MAX_LINE_LENGTH_CONSTANT = 60
FONT_SIZES_BY_TYPE = {
    'words': 50,
    'components': 40,
    'sent_chinese': 50,
    'sent': 45
}

NONVOCAB_AUDIO_TEXT_FONT_SIZE = 22
NONVOCAB_AUDIO_TEXT_FONT = ImageFont.truetype(hanzi_font_path, NONVOCAB_AUDIO_TEXT_FONT_SIZE)
NONVOCAB_AUDIO_TEXT_FILL = 'black'
NONVOCAB_AUDIO_TEXT_SPACING = 20
NONVOCAB_AUDIO_TEXT_ALIGN = 'center'
NONVOCAB_AUDIO_TEXT_Y = 600

# Intro slide
CHANNEL_TITLE = ('My Mandarin Database', '我的普通话数据库')
VIDEO_NUMBER = (f'Video #{video_number}', f'视频#{video_number}')
VIDEO_NAME = (f"{subtitle_1['english']}: {subtitle_2['english']}", f"{subtitle_1['chinese']}: {subtitle_2['chinese']}")
VIDEO_STRUCTURE = ('Chinese first, English second\nExample sentences', '先中文，后英文\n并附例句')
INTR_COUNT_STR = ("{n_vocab_words} words", "{n_vocab_words}个词汇")
INTRO_DURATION_STR = ('{audio_duration_minutes:.0f} minutes', '{audio_duration_minutes:.0f}分钟')
FEEDBACK = ('If you have any questions, suggestions, or feedback\nplease leave a comment', '如果你有任何问题、建议或反馈\n请留言')

# nonvocab slides
nonvocab_audio_path = 'audio_files/nonvocab/'
nonvocab_slides = {
    'intro': {
        'chinese': f"欢迎观看我的普通话数据库视频 {video_number}: {subtitle_1['chinese']}: {subtitle_2['chinese']}",
        'pinyin': f"Huānyíng guānkàn wǒ de pǔtōnghuà shùjùkù shìpín {video_number}: {subtitle_1['pinyin']}: {subtitle_2['pinyin']}",
        'english': f"Welcome to my Mandarin Chinese Database Video {video_number}: {subtitle_1['english']}: {subtitle_2['english']}",
        'clip_index': 0,
        'change_index': -2,
        'pause_ms': 500,
    },
    'word_list': {
        'chinese_unfill': '这些是将在接下来的{audio_duration_minutes:.0f}分钟内复习的{n_vocab}个单词',
        'pinyin_unfill': 'Zhèxiē shì jiàng zài jiē xiàlái de {audio_duration_minutes:.0f} fēnzhōng nèi fùxí de {n_vocab} gè dāncí',
        'english_unfill': 'These are the {n_vocab} words that will be reviewed over the next {audio_duration_minutes:.0f} minutes',
        'clip_index': 1,
        'change_index': -1,
        'pause_ms': 500,
    },
    'end': {
        'chinese': '如果你有任何问题、建议或反馈，请留言。请点赞并订阅。',
        'pinyin': 'Rúguǒ nǐ yǒu rènhé wèntí, jiànyì huò fǎnkuì, qǐng liúyán. Qǐng diǎn zàn bìng dìngyuè.',
        'english': 'If you have any questions, suggestions, or feedback, please leave a comment. Please like and subscribe.',
        'clip_index': -1,
        'change_index': None,
        'pause_ms': 500,
    },
}

# audio
dict_recordings = [
    {
    'recording_id': '013', 'filename_suffix': '_animal_yt',
    'category_type': 'animal',
    'min_combo_quality': 3,
    'min_priority': 1, 'max_priority': 4,
    'min_known_english_prompt': 1, 'max_known_english_prompt': 5,
    'min_adu': 3, 'min_per': 3,
    },
]