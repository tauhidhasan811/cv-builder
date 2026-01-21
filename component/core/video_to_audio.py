import moviepy

def ExtractAudio(vdo_path, audio_path):
    video = moviepy.VideoFileClip(vdo_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    video.close()
    return True