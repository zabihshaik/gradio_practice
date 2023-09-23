# !pip install SpeechRecognition
# !pip install PyAudio

import speech_recognition as sr


class Audio2Text:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def process(self, audio_file_path):
        with sr.AudioFile(audio_file_path) as source:
            # read the entire audio file
            audio = self.recognizer.record(source)

        try:
            transcription = self.recognizer.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return "We could not understand the audio."
        except sr.RequestError as e:
            return "Could not request results; {0}".format(e)


# Example usage
if __name__ == "__main__":
    audio2text = Audio2Text()
    # Replace with your actual WAV file path
    result = audio2text.process("recorded_audio.wav")
    print("Transcription:", result)
