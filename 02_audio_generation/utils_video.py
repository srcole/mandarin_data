import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, CompositeVideoClip, AudioFileClip

def create_component_words_text(row):
    component_words_text = f"{row['word1']}: {row['word1_english']}\n{row['word2']}: {row['word2_english']}"
    if not pd.isna(row['word3']):
        component_words_text += f"\n{row['word3']}: {row['word3_english']}"
    if not pd.isna(row['word4']):
        component_words_text += f"\n{row['word4']}: {row['word4_english']}"
    return component_words_text


def get_wrapped_text(text: str, font: ImageFont.ImageFont, line_length: int):
    """OLD function"""
    new_lines = ['']
    for original_line in text.split('\n'):
        # Make sure no words are longer than line_length in original line
        # if so, divide it into multiple words to make a new line
        words_split = original_line.split(' ')
        no_long_words_line = ''
        for word in words_split:
            if font.getlength(word) > line_length:
                print(font.getlength(word), word)
                # Split the word into characters
                long_word_chars = list(word)
                new_long_word = ''
                tmp_long_word = ''
                for char in long_word_chars:
                    test_word = f'{tmp_long_word}{char}'
                    if font.getlength(test_word) <= line_length:
                        tmp_long_word = f'{tmp_long_word}{char}'
                    else:
                        new_long_word += f'{tmp_long_word} '
                        tmp_long_word = ''
                no_long_words_line += f'{new_long_word}{tmp_long_word}'
            else:
                no_long_words_line += f'{word} '

        words_split = no_long_words_line.split(' ')
        for word_idx, word in enumerate(words_split):
            test_line = f'{new_lines[-1]} {word}'.strip()
            if word_idx == 0 and new_lines[-1] != '':
                new_lines.append(word)
            elif font.getlength(test_line) <= line_length:
                new_lines[-1] = test_line
            else:
                new_lines.append(word)
    return '\n'.join(new_lines)


def create_text_clip(
        text, duration, timestamp_start, image_file_name
        , hanzi_font_path='/System/Library/Fonts/STHeiti Medium.ttc'
        , size=(1280, 720)
        , bg_color='white'
        , text_color='black'
        ):
    """Old function before better youtube format"""
    # Use textcip
    # clip_c = TextClip(text=f"{chinese}\n{pinyin}", font='Marker Felt', font_size=70, color=text_color, bg_color=bg_color, size=size, method='label', duration=duration_text_c)
    font = ImageFont.truetype(hanzi_font_path, 50)
    wrapped_text = get_wrapped_text(text, font, line_length=size[0]-60)

    img = Image.new("RGB", size, color=bg_color)
    draw = ImageDraw.Draw(img)
    draw.multiline_text(
        xy=(30, 50), text=wrapped_text, font=font
        , fill=text_color, spacing=30, align='center'
        )

    img_file_path = f"audio_files/img_for_video/{image_file_name}.png"
    img.save(img_file_path)
    return ImageClip(img_file_path, duration=duration).with_start(timestamp_start)

def determine_if_text_size_too_big(text: str, font: ImageFont.ImageFont, line_length: int):
    new_lines = ['']
    for original_line in text.split('\n'):
        words_split = original_line.split(' ')
        for word_idx, word in enumerate(words_split):
            test_line = f'{new_lines[-1]} {word}'.strip()
            if word_idx == 0 and new_lines[-1] != '':
                new_lines.append(word)
            elif font.getlength(test_line) <= line_length:
                new_lines[-1] = test_line
            else:
                return True
    return False


def add_text_and_save_clip(text_settings, img, draw, clips, rrow, bg_size, max_line_length, current_image_file_path, save_clip=True):
    new_font_size = text_settings['font_size']
    font = ImageFont.truetype(text_settings['font_path'], new_font_size)
    font_size_too_big = determine_if_text_size_too_big(text_settings['text'], font, line_length=bg_size[0]-max_line_length)
    while font_size_too_big:
        new_font_size -= 5
        print(f'reduced font size to {new_font_size}')
        font = ImageFont.truetype(text_settings['font_path'], new_font_size)
        font_size_too_big = determine_if_text_size_too_big(text_settings['text'], font, line_length=bg_size[0]-max_line_length)

    longest_length = max([font.getlength(x) for x in text_settings['text'].split('\n')])
    draw.multiline_text(
        xy=(bg_size[0]/2 - longest_length/2, text_settings['y_pos'])
        , text=text_settings['text'], font=font
        , fill=text_settings['fill'], spacing=text_settings['spacing'], align=text_settings['align']
        )
    if save_clip:
        img_file_path = f"{current_image_file_path}_{text_settings['img_file_suffix']}.png"
        img.save(img_file_path)
        my_img = ImageClip(img_file_path, duration=text_settings['duration']).with_start(text_settings['timestamp_start'])
        clips[rrow['recording_name']].append(my_img)
    return img, draw, clips


def create_full_video_file(clips_all, rrow):
    video_file_name = f"audio_files/products/videos/{rrow['recording_name']}_video.mp4"
    if os.path.exists(video_file_name):
        print(f"Video already exists: {video_file_name}, skipping...")
    else:
        video = CompositeVideoClip(clips_all, size=(1280,720))
        audio = AudioFileClip(f"audio_files/products/{rrow['recording_name']}.mp3")
        video.audio = audio
        video.duration = audio.duration
        video.write_videofile(video_file_name, fps=24)
