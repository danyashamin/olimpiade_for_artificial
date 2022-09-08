from chardet import detect

with open('ProgramSecond.py', 'rb') as f1:
    print(detect(f1.read()))