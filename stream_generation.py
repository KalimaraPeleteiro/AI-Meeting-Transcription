import time

def stream_answer(answer):
    for word in answer:
        yield word + " "
        time.sleep(0.02)