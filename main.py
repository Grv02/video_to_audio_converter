import os
import subprocess

def _convert_video_to_audio_ffmpeg(video_file, output_dir, output_ext="wav"):
    filename, _ = os.path.splitext(os.path.basename(video_file))
    audio_file_name = f"{filename}.{output_ext}"
    audio_file_path = os.path.join(output_dir, audio_file_name)
    subprocess.call(["ffmpeg", "-i", video_file, "-vn", "-ac", "2", "-ar", "44100", "-ab", "320k", "-f", "wav", audio_file_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    return audio_file_path

if __name__ == '__main__':
    video_path = 'dir/'
    output_dir = 'output_audio/'  # Specify the output directory
    os.makedirs(output_dir, exist_ok=True)

    files = os.listdir(video_path)
    for f in files:
        if f.endswith('.mp4'):
            video_file_path = os.path.join(video_path, f)
            _convert_video_to_audio_ffmpeg(video_file_path, output_dir)
