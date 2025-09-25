from PIL import ImageFont
from constants import WORD_TYPES, PHRASE_TYPES, SENT_TYPES, PROPER_NOUN_TYPES, IDIOM_TYPES, ALL_TYPES

# TODO - change the script so that it is more reproducible; won't change (e.g. functions that can be versioned for different intros)

# Basic video info
video_name = '100 words in 6 minutes - Chinese vocabulary'
video_description = '''
This video was made for quickly reviewing Chinese vocabulary, practicing both listening comprehension and character recognition.
A variety of 100 common words are presented, each spoken twice in succession.
Words may come from HSK1, HSK2, HSK3, HSK4, HSK5, or above.
Because these videos are programmatically generated, the format is customizable to quickly produce alternate formats with different vocabulary categories.
If you have any corrections, suggestions, feedback, or questions, please leave a comment.
'''
video_number = '5'
subtitle_1 = {'chinese': '100 常用词', 'pinyin': '100 chángyòng cí', 'english': '100 common words'}
subtitle_2 = {'chinese': '6 分钟', 'pinyin': '6 fēnzhōng', 'english': '6 minutes'}

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
nonvocab_audio_path = 'audio_files/files_by_video/'
nonvocab_slides = {
    'intro': {
        'chinese': f"欢迎观看我的普通话数据库视频 {video_number}: {subtitle_1['chinese']}: {subtitle_2['chinese']}",
        'pinyin': f"Huānyíng guānkàn wǒ de pǔtōnghuà shùjùkù shìpín {video_number}: {subtitle_1['pinyin']}: {subtitle_2['pinyin']}",
        'english': f"Welcome to my Mandarin Chinese Database Video {video_number}: {subtitle_1['english']}: {subtitle_2['english']}",
        'clip_index': 0,
        'change_index': -2,
        'pause_ms': 300,
    },
    'end': {
        'chinese': '如果你有任何问题、建议或反馈，请留言。',
        'pinyin': 'Rúguǒ nǐ yǒu rènhé wèntí, jiànyì huò fǎnkuì, qǐng liúyán.',
        'english': 'If you have any questions, suggestions, or feedback, please leave a comment.',
        'clip_index': -1,
        'change_index': None,
        'pause_ms': 300,
    },
}

# audio
dict_recordings = [
    {
    'recording_id': 'chinese_only_word_twice', 'filename_suffix': '_one_hundred_words',
    'min_adu': 3, 'min_per': 3,
    'min_priority': 1, 'max_priority': 1,
    'types_allowed': WORD_TYPES + PROPER_NOUN_TYPES,
    'exclude_words': ['最大的弱点', '大二', '大三', '大一', '台湾', '孔子', '普通话', '人民币', '随地吐痰', '被黑', '高考',
                      '大陆人', '长城', '长江', '牛马', '程序员', '亿', '多少', '升', '平常', '用户', '账户', '不在乎', '持怀疑态度'],
    'max_count': 100,
    },
]