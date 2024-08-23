import whisper


def transcribe_audio(path, model_type):
    model = whisper.load_model(model_type)

    result = model.transcribe(path)
    return result["text"]