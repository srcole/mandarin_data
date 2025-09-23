import pandas as pd
from collections import defaultdict
import os
from gtts import gTTS
from moviepy import AudioFileClip
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
from collections import defaultdict
import time
from utils_data import pinyin_to_tones


def create_tts_file(tts_type, content_str, lang_name, last_timestamp, chinese_char, recording_id):
    if tts_type == 'zh_slow':
        slow_mode = True
    else:
        slow_mode = False

    new_file_path = f"audio_files/{tts_type}/{content_str}.mp3"
    if not os.path.exists(new_file_path):
        # Delete final row file, if exists, since will have to rewrite it
        row_file_path = f"audio_files/rows/{recording_id}/{chinese_char}.mp3"
        if os.path.exists(row_file_path):
            os.remove(row_file_path)
        
        try:
            gTTS(content_str, lang=lang_name, slow=slow_mode).save(new_file_path)
        except:
            # Wait 60 seconds and try again
            print(f"!!!!!!! FAILURE, wait 52 seconds, {tts_type}, {content_str} !!!!!!!")
            time.sleep(52)
            try:
                gTTS(content_str, lang=lang_name, slow=slow_mode).save(new_file_path)
            except:
                # Wait 60 seconds and try again
                print(f"!!!!!!!!!! FAILURE AGAIN, wait 278 seconds, {tts_type}, {content_str} !!!!!!!!!!")
                time.sleep(278)
                gTTS(content_str, lang=lang_name, slow=slow_mode).save(new_file_path)
        print(f"{(time.time()-last_timestamp):.3f}s, {tts_type}, {content_str}")
    else:
        print(f"{(time.time()-last_timestamp):.3f}s, ALREADY EXISTS, {tts_type}, {content_str}")


def create_tts_files_for_one_vocab_word(row, rrow):
    create_tts_file(tts_type='zh', content_str=row['chinese'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
    create_tts_file(tts_type='zh_slow', content_str=row['chinese'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
    create_tts_file(tts_type='english', content_str=row['english'], lang_name='en', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
    
    if rrow['recording_id'] in ['001', '007', '009', '013', 'ce_wordsent']:
        create_tts_file(tts_type='zh', content_str=row['sentence'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
        create_tts_file(tts_type='english', content_str=row['sentence_english'], lang_name='en', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
    
    if rrow['recording_id'] in ['002', '011', '012', '015', 'cn_only_sent', 'ec_csent']:
        create_tts_file(tts_type='zh', content_str=row['sentence'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
    
    if rrow['recording_id'] in ['006', '013']:
        create_tts_file(tts_type='zh', content_str=row['word1'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
        create_tts_file(tts_type='zh', content_str=row['word2'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
        create_tts_file(tts_type='english', content_str=row['word1_english'], lang_name='en', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
        create_tts_file(tts_type='english', content_str=row['word2_english'], lang_name='en', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
        if not pd.isna(row['word3']):
            create_tts_file(tts_type='zh', content_str=row['word3'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
            create_tts_file(tts_type='english', content_str=row['word3_english'], lang_name='en', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
        if not pd.isna(row['word4']):
            create_tts_file(tts_type='zh', content_str=row['word4'], lang_name='zh-cn', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
            create_tts_file(tts_type='english', content_str=row['word4_english'], lang_name='en', last_timestamp=time.time(), chinese_char=row['chinese'], recording_id=rrow['recording_id'])
    

def compute_pinyin_and_create_recordings(df_words):
    # Make pinyin audio, if needed
    pinyin_tones = ['1', '2', '3', '4']
    for tone_str in pinyin_tones:
        gTTS(tone_str, lang='en').save(f"audio_files/english/{tone_str}.mp3")

    # Compute pinyin tones for each character
    df_words['pinyin_tones'] = df_words['pinyin'].apply(pinyin_to_tones)
    return df_words


def load_one_audio_from_path(mp3_path):
    try:
        audio = AudioSegment.from_mp3(mp3_path)
    except CouldntDecodeError:
        os.remove(mp3_path)
        print(f"!!!!!!! DELETED CORRUPTED FILE {mp3_path} !!!!!!!")
        raise ValueError(f"Corrupted file {mp3_path}, deleted. Please rerun the cell above to regenerate it.")
    return audio


def load_audio(recording_id, row):
    pause_100ms = AudioSegment.silent(duration=100)
    pause_300ms = AudioSegment.silent(duration=300)
    pause_500ms = AudioSegment.silent(duration=500)
    pause_800ms = AudioSegment.silent(duration=800)
    pause_1000ms = AudioSegment.silent(duration=1000)

    dict_audio_durations = defaultdict(list)
    chinese_audio = load_one_audio_from_path(f"audio_files/zh/{row['chinese']}.mp3")
    chinese_slow_audio = load_one_audio_from_path(f"audio_files/zh_slow/{row['chinese']}.mp3")
    english_audio = load_one_audio_from_path(f"audio_files/english/{row['english']}.mp3")
    
    if recording_id in ['001', '007', '009', 'ce_wordsent']:
        sent_audio = load_one_audio_from_path(f"audio_files/zh/{row['sentence']}.mp3")
        sent_english_audio = load_one_audio_from_path(f"audio_files/english/{row['sentence_english']}.mp3")
        combined = chinese_audio + pause_500ms + chinese_slow_audio + pause_500ms + english_audio + pause_500ms + sent_audio + pause_500ms + sent_english_audio + pause_500ms + sent_audio + pause_1000ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['sentence'].append(row['sentence'])
        dict_audio_durations['sentence_pinyin'].append(row['sentence_pinyin'])
        dict_audio_durations['sentence_english'].append(row['sentence_english'])

        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_chinese_slow'].append(chinese_slow_audio.duration_seconds)
        dict_audio_durations['d_english'].append(english_audio.duration_seconds)
        dict_audio_durations['d_sent'].append(sent_audio.duration_seconds)
        dict_audio_durations['d_sent_english'].append(sent_english_audio.duration_seconds)

        dict_audio_durations['rel_start_chinese'].append(0)
        dict_audio_durations['rel_start_english'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + dict_audio_durations['d_chinese_slow'][-1] + 1)
        dict_audio_durations['rel_start_sent'].append(dict_audio_durations['rel_start_english'][-1] + dict_audio_durations['d_english'][-1] + 0.5)
        dict_audio_durations['rel_start_sent_english'].append(dict_audio_durations['rel_start_sent'][-1] + dict_audio_durations['d_sent'][-1] + 0.5)

        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_sent_english'][-1] + dict_audio_durations['d_sent_english'][-1] + dict_audio_durations['d_sent'][-1] + 1.5)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id in ['002', '011']:
        sent_audio = load_one_audio_from_path(f"audio_files/zh/{row['sentence']}.mp3")
        combined = chinese_audio + pause_500ms + chinese_slow_audio + pause_500ms + english_audio + pause_500ms + sent_audio + pause_500ms + sent_audio + pause_1000ms

    elif recording_id in ['004', '008', '010', '014']:
        combined = chinese_audio + pause_500ms + chinese_slow_audio + pause_500ms + english_audio + pause_1000ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_chinese_slow'].append(chinese_slow_audio.duration_seconds)
        dict_audio_durations['d_english'].append(english_audio.duration_seconds)

        dict_audio_durations['rel_start_chinese'].append(0)
        dict_audio_durations['rel_start_english'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + dict_audio_durations['d_chinese_slow'][-1] + 1)
        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_english'][-1] + dict_audio_durations['d_english'][-1] + 1)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id in ['016']:
        combined = english_audio + pause_500ms + chinese_audio + pause_300ms + chinese_slow_audio + pause_1000ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_chinese_slow'].append(chinese_slow_audio.duration_seconds)
        dict_audio_durations['d_english'].append(english_audio.duration_seconds)

        dict_audio_durations['rel_start_english'].append(0)
        dict_audio_durations['rel_start_chinese'].append(dict_audio_durations['rel_start_english'][-1] + dict_audio_durations['d_english'][-1] + .5)
        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + dict_audio_durations['d_chinese_slow'][-1] + 1.3)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id == '005':
        tones_audio = AudioSegment.silent(duration=0)
        for pinyin_tone in row['pinyin_tones']:
            tones_audio += load_one_audio_from_path(f"audio_files/english/{pinyin_tone}.mp3")
            tones_audio += pause_100ms

        combined = chinese_audio + pause_500ms + tones_audio + pause_500ms + chinese_slow_audio + pause_500ms + english_audio + pause_1000ms

    elif recording_id == '006':
        word1_audio = load_one_audio_from_path(f"audio_files/zh/{row['word1']}.mp3")
        word1e_audio = load_one_audio_from_path(f"audio_files/english/{row['word1_english']}.mp3")
        word2_audio = load_one_audio_from_path(f"audio_files/zh/{row['word2']}.mp3")
        word2e_audio = load_one_audio_from_path(f"audio_files/english/{row['word2_english']}.mp3")
        if not pd.isna(row['word3']):
            word3_audio = load_one_audio_from_path(f"audio_files/zh/{row['word3']}.mp3")
            word3e_audio = load_one_audio_from_path(f"audio_files/english/{row['word3_english']}.mp3")
        if not pd.isna(row['word4']):
            word4_audio = load_one_audio_from_path(f"audio_files/zh/{row['word4']}.mp3")
            word4e_audio = load_one_audio_from_path(f"audio_files/english/{row['word4_english']}.mp3")

        component_words_audio = word1_audio + pause_100ms + word1e_audio + pause_500ms + word2_audio + pause_100ms + word2e_audio
        if not pd.isna(row['word3']):
            component_words_audio += pause_500ms + word3_audio + pause_100ms + word3e_audio
        if not pd.isna(row['word4']):
            component_words_audio += pause_500ms + word4_audio + pause_100ms + word4e_audio
        combined = chinese_audio + pause_500ms + component_words_audio + pause_500ms + chinese_slow_audio + pause_500ms + english_audio + pause_500ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['word1'].append(row['word1'] if not pd.isna(row['word1']) else '')
        dict_audio_durations['word1_english'].append(row['word1_english'] if not pd.isna(row['word1_english']) else '')
        dict_audio_durations['word2'].append(row['word2'] if not pd.isna(row['word2']) else '')
        dict_audio_durations['word2_english'].append(row['word2_english'] if not pd.isna(row['word2_english']) else '')
        dict_audio_durations['word3'].append(row['word3'] if not pd.isna(row['word3']) else '')
        dict_audio_durations['word3_english'].append(row['word3_english'] if not pd.isna(row['word3_english']) else '')
        dict_audio_durations['word4'].append(row['word4'] if not pd.isna(row['word4']) else '')
        dict_audio_durations['word4_english'].append(row['word4_english'] if not pd.isna(row['word4_english']) else '')
        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_component_words'].append(component_words_audio.duration_seconds)
        dict_audio_durations['d_chinese_slow'].append(chinese_slow_audio.duration_seconds)
        dict_audio_durations['d_english'].append(english_audio.duration_seconds)

        dict_audio_durations['rel_start_chinese'].append(0)
        dict_audio_durations['rel_start_component_words'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + 0.5)
        dict_audio_durations['rel_start_english'].append(dict_audio_durations['rel_start_component_words'][-1] + dict_audio_durations['d_component_words'][-1] + dict_audio_durations['d_chinese_slow'][-1] + 1)

        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_english'][-1] + dict_audio_durations['d_english'][-1] + 0.5)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id == '013':
        sent_audio = load_one_audio_from_path(f"audio_files/zh/{row['sentence']}.mp3")
        sent_english_audio = load_one_audio_from_path(f"audio_files/english/{row['sentence_english']}.mp3")
        word1_audio = load_one_audio_from_path(f"audio_files/zh/{row['word1']}.mp3")
        word1e_audio = load_one_audio_from_path(f"audio_files/english/{row['word1_english']}.mp3")
        word2_audio = load_one_audio_from_path(f"audio_files/zh/{row['word2']}.mp3")
        word2e_audio = load_one_audio_from_path(f"audio_files/english/{row['word2_english']}.mp3")
        if not pd.isna(row['word3']):
            word3_audio = load_one_audio_from_path(f"audio_files/zh/{row['word3']}.mp3")
            word3e_audio = load_one_audio_from_path(f"audio_files/english/{row['word3_english']}.mp3")
        if not pd.isna(row['word4']):
            word4_audio = load_one_audio_from_path(f"audio_files/zh/{row['word4']}.mp3")
            word4e_audio = load_one_audio_from_path(f"audio_files/english/{row['word4_english']}.mp3")

        component_words_audio = word1_audio + pause_100ms + word1e_audio + pause_500ms + word2_audio + pause_100ms + word2e_audio
        if not pd.isna(row['word3']):
            component_words_audio += pause_500ms + word3_audio + pause_100ms + word3e_audio
        if not pd.isna(row['word4']):
            component_words_audio += pause_500ms + word4_audio + pause_100ms + word4e_audio
        combined = chinese_audio + pause_500ms + component_words_audio + pause_500ms + chinese_slow_audio + pause_500ms + english_audio + pause_500ms + sent_audio + pause_500ms + sent_english_audio + pause_1000ms


        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['sentence'].append(row['sentence'])
        dict_audio_durations['sentence_pinyin'].append(row['sentence_pinyin'])
        dict_audio_durations['sentence_english'].append(row['sentence_english'])
        dict_audio_durations['word1'].append(row['word1'] if not pd.isna(row['word1']) else '')
        dict_audio_durations['word1_english'].append(row['word1_english'] if not pd.isna(row['word1_english']) else '')
        dict_audio_durations['word2'].append(row['word2'] if not pd.isna(row['word2']) else '')
        dict_audio_durations['word2_english'].append(row['word2_english'] if not pd.isna(row['word2_english']) else '')
        dict_audio_durations['word3'].append(row['word3'] if not pd.isna(row['word3']) else '')
        dict_audio_durations['word3_english'].append(row['word3_english'] if not pd.isna(row['word3_english']) else '')
        dict_audio_durations['word4'].append(row['word4'] if not pd.isna(row['word4']) else '')
        dict_audio_durations['word4_english'].append(row['word4_english'] if not pd.isna(row['word4_english']) else '')
        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_component_words'].append(component_words_audio.duration_seconds)
        dict_audio_durations['d_chinese_slow'].append(chinese_slow_audio.duration_seconds)
        dict_audio_durations['d_english'].append(english_audio.duration_seconds)
        dict_audio_durations['d_sent'].append(sent_audio.duration_seconds)
        dict_audio_durations['d_sent_english'].append(sent_english_audio.duration_seconds)

        dict_audio_durations['rel_start_chinese'].append(0)
        dict_audio_durations['rel_start_component_words'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + 0.5)
        dict_audio_durations['rel_start_english'].append(dict_audio_durations['rel_start_component_words'][-1] + dict_audio_durations['d_component_words'][-1] + dict_audio_durations['d_chinese_slow'][-1] + 1)
        dict_audio_durations['rel_start_sent'].append(dict_audio_durations['rel_start_english'][-1] + dict_audio_durations['d_english'][-1] + 0.5)
        dict_audio_durations['rel_start_sent_english'].append(dict_audio_durations['rel_start_sent'][-1] + dict_audio_durations['d_sent'][-1] + 0.5)

        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_sent_english'][-1] + dict_audio_durations['d_sent_english'][-1] + 1)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id in ['012', 'ec_csent']:
        sent_audio = AudioSegment.from_mp3(f"audio_files/zh/{row['sentence']}.mp3")
        combined = english_audio + pause_500ms + chinese_audio + pause_500ms + sent_audio + pause_1000ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['sentence'].append(row['sentence'])
        dict_audio_durations['sentence_pinyin'].append(row['sentence_pinyin'])
        dict_audio_durations['sentence_english'].append(row['sentence_english'])

        dict_audio_durations['d_english'].append(english_audio.duration_seconds)
        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_sent'].append(sent_audio.duration_seconds)

        dict_audio_durations['rel_start_english'].append(0)
        dict_audio_durations['rel_start_chinese'].append(dict_audio_durations['rel_start_english'][-1] + dict_audio_durations['d_english'][-1] + 0.5)
        dict_audio_durations['rel_start_sent'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + 0.5)
        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_sent'][-1] + dict_audio_durations['d_sent'][-1] + 1)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id in ['015', 'cn_only_sent']:
        sent_audio = AudioSegment.from_mp3(f"audio_files/zh/{row['sentence']}.mp3")
        combined = chinese_audio + pause_300ms + sent_audio + pause_1000ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])
        dict_audio_durations['sentence'].append(row['sentence'])
        dict_audio_durations['sentence_pinyin'].append(row['sentence_pinyin'])
        dict_audio_durations['sentence_english'].append(row['sentence_english'])

        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds)
        dict_audio_durations['d_sent'].append(sent_audio.duration_seconds)

        dict_audio_durations['rel_start_chinese'].append(0)
        dict_audio_durations['rel_start_sent'].append(dict_audio_durations['rel_start_chinese'][-1] + dict_audio_durations['d_chinese'][-1] + 0.3)
        dict_audio_durations['sum_theory'].append(dict_audio_durations['rel_start_sent'][-1] + dict_audio_durations['d_sent'][-1] + 1)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    elif recording_id == 'chinese_only_word_twice':
        sent_audio = AudioSegment.from_mp3(f"audio_files/zh/{row['sentence']}.mp3")
        combined = chinese_audio + pause_300ms + chinese_slow_audio + pause_1000ms

        dict_audio_durations['chinese'].append(row['chinese'])
        dict_audio_durations['pinyin'].append(row['pinyin'])
        dict_audio_durations['english'].append(row['english'])

        dict_audio_durations['d_chinese'].append(chinese_audio.duration_seconds + chinese_slow_audio.duration_seconds + 0.3)

        dict_audio_durations['rel_start_chinese'].append(0)
        dict_audio_durations['sum_theory'].append(dict_audio_durations['d_chinese'][-1] + 1)
        dict_audio_durations['combined'].append(combined.duration_seconds)

    else:
        raise ValueError(f"Invalid recording_id: {recording_id}")
    
    df_audio_durations = pd.DataFrame(dict_audio_durations)
    return combined, df_audio_durations


def compute_start_times_for_clips(df_durations, recording_settings):
    # Compute columns for video timestamps
    df_durations['end'] = df_durations['combined'].cumsum()
    df_durations['start'] = df_durations['end'] - df_durations['combined']
    if recording_settings['recording_id'] in ['004', '008', '010', '014', '016']:
        df_durations['start_chinese'] = df_durations['start'] + df_durations['rel_start_chinese']
        df_durations['start_english'] = df_durations['start'] + df_durations['rel_start_english']
    elif recording_settings['recording_id'] == '013':
        df_durations['start_chinese'] = df_durations['start'] + df_durations['rel_start_chinese']
        df_durations['start_component_words'] = df_durations['start'] + df_durations['rel_start_component_words']
        df_durations['start_english'] = df_durations['start'] + df_durations['rel_start_english']
        df_durations['start_sent'] = df_durations['start'] + df_durations['rel_start_sent']
        df_durations['start_sent_english'] = df_durations['start'] + df_durations['rel_start_sent_english']
    elif recording_settings['recording_id'] == '006':
        df_durations['start_chinese'] = df_durations['start'] + df_durations['rel_start_chinese']
        df_durations['start_component_words'] = df_durations['start'] + df_durations['rel_start_component_words']
        df_durations['start_english'] = df_durations['start'] + df_durations['rel_start_english']
    elif recording_settings['recording_id'] in ['001', 'ce_wordsent']:
        df_durations['start_chinese'] = df_durations['start'] + df_durations['rel_start_chinese']
        df_durations['start_english'] = df_durations['start'] + df_durations['rel_start_english']
        df_durations['start_sent'] = df_durations['start'] + df_durations['rel_start_sent']
        df_durations['start_sent_english'] = df_durations['start'] + df_durations['rel_start_sent_english']
    elif recording_settings['recording_id'] in ['012', 'ec_csent']:
        df_durations['start_english'] = df_durations['start'] + df_durations['rel_start_english']
        df_durations['start_chinese'] = df_durations['start'] + df_durations['rel_start_chinese']
        df_durations['start_sent'] = df_durations['start'] + df_durations['rel_start_sent']
    elif recording_settings['recording_id'] in ['015', 'cn_only_sent']:
        df_durations['start_sent'] = df_durations['start'] + df_durations['rel_start_sent']
    else:
        print('VIDEO NOT MADE FOR RECORDING ID', recording_settings['recording_id'])
    return df_durations


def combine_audio_files_and_compute_durations(df_words, recording_settings, making_video=True):
    dfs_audio_durations = []
    for i_row, row in df_words.iterrows():
        start_time = time.time()
        new_folder_path = f"audio_files/rows/{recording_settings['recording_id']}"
        new_file_path = f"{new_folder_path}/{row['chinese']}.mp3"
        os.makedirs(new_folder_path, exist_ok=True)

        # Only compute if making video or does not exist
        if making_video or (not os.path.exists(new_file_path)):
            combined, df_audio_durations_onerow = load_audio(recording_settings['recording_id'], row)
            dfs_audio_durations.append(df_audio_durations_onerow)
            combined.export(new_file_path, format="mp3")
            print(f"{(time.time()-start_time):.2f} seconds, recid{recording_settings['recording_name']}, row {i_row}, {row['chinese']}")
        else:
            print(f"{(time.time()-start_time):.2f} seconds, recid{recording_settings['recording_name']}, row {i_row}, {row['chinese']} ALREADY EXISTS")

    # Add in static slide audio into dataframe of audio durations
    df_durations = pd.concat(dfs_audio_durations, ignore_index=True)
    return df_durations
