import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Transcription
from .serializers import TranscriptionSerializer
from Pyannite import SpeakerDiarization, SpeechRecognition

class TranscribeVideo(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        video_file = request.FILES['video']
        transcription = Transcription(video=video_file)
        transcription.save()

        # Realizar transcrição e identificação do orador
        speaker_diarization = SpeakerDiarization(video_file)
        speech_recognition = SpeechRecognition(video_file)
        transcription_json = []

        for segment in speaker_diarization.segments:
            speech_text = speech_recognition.recognize(segment.audio)
            transcription_json.append({
                'speaker': segment.speaker,
                'start_time': segment.start_time,
                'end_time': segment.end_time,
                'text': speech_text
            })

        transcription.transcription_json = json.dumps(transcription_json)
        transcription.save()

        return Response({"transcription": transcription.transcription_json})
