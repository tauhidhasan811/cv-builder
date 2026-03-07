# from openai import OpenAI

# class OpenAIAudio:
#     def __init__(self, model_name = "whisper-1"):
#         self.client = OpenAI()
#         self.model = model_name

#     def ConvertToText(self, audio_path):
#         """
#         audion_file = open(audio_path, 'rb')
#         result = self.client.audio.transcriptions.create(
#             model=self.model,
#             file=audion_file
#         )
#         """

#         with open(audio_path, 'rb') as audion_file:
#             result = self.client.audio.transcriptions.create(
#                 model=self.model,
#                 file=audion_file
#             )
#         return result.text

from openai import OpenAI

class OpenAIAudio:
    def __init__(self, model_name="whisper-1"):
        self.client = OpenAI()
        self.model = model_name

    def ConvertToText(self, audio_path):

        with open(audio_path, "rb") as audio_file:
            result = self.client.audio.transcriptions.create(
                model=self.model,
                file=audio_file,
                response_format="verbose_json"
            )

        segments = []
        for seg in result.segments:
            segments.append({
                "start": seg.start,
                "end": seg.end,
                "text": seg.text
            })

        return segments