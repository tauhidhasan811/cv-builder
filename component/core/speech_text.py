from component.config.hug_model import HugModel

model = HugModel()

def SpeechToText(audio_path):
    output = model.automatic_speech_recognition(audio_path)
    text = output.text
    return text