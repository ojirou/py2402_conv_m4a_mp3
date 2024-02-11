import os
from pydub import AudioSegment
def convert_m4a_to_mp3(input_file, output_file):
    # 音声ファイルを読み込み
    audio = AudioSegment.from_file(input_file)
    # mp3 に変換して保存
    audio.export(output_file, format="mp3")
def process_files_in_folder(folder_path):
    # フォルダ内のすべてのファイルに対して処理
    for filename in os.listdir(folder_path):
        if filename.endswith(".m4a"):
            input_file = os.path.join(folder_path, filename)
            # 出力ファイル名を設定
            output_file = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.mp3")
            convert_m4a_to_mp3(input_file, output_file)
if __name__ == "__main__":
    folder_path = "C:\Users\user\git\github\\py2402_conv_m4a_mp3\\"
    process_files_in_folder(folder_path)