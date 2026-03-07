import asyncio
from dotenv import load_dotenv
from component.core.video_to_audio import ExtractAudio
from component.config.audio_model import OpenAIAudio

load_dotenv()

async def main():
    path = "Download (2).mp4"
    aud_pth = "zzzz.mp3"

    audio_model = OpenAIAudio()

    ExtractAudio(path, aud_pth)

    written_submission = await asyncio.to_thread(
        audio_model.ConvertToText, aud_pth
    )

    print(written_submission)


asyncio.run(main())