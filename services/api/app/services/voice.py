from app.services.ai_engine import AIEngine


class VoiceService:
    @staticmethod
    def transcribe(audio_url: str, lang: str) -> tuple[str, float]:
        # Placeholder for STT provider integration
        transcript = f'Transcribed ({lang}) from: {audio_url}'
        return transcript, 0.81

    @staticmethod
    def answer_from_voice(transcript: str, lang: str) -> tuple[str, float]:
        return AIEngine.answer_question(transcript, lang)
