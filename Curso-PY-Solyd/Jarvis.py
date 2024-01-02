# IMPORTE O PACOTE DE RECONHECIMENTO DE FALA
import speech_recognition as sr  # pip install SpeechRecognition
# IMPORTA O PACOTE QUE FALA O QUE ESTA ESCRITO
import pyttsx3  # pip install pyttsx3

# EXECUTA A FUNÇÃO DE RECONHECIMENTO COM O PACOTE SR
r = sr.Recognizer()

# EXECUTA A FUNÇÃO DO MICROFONE COM O PACOTE SR
mic = sr.Microphone()

# COM O MICROFONE COMO FONTE
with mic as fonte:
    # CALLIBRAÇÃO PARA O RUÍDO AMBIENTE
    r.adjust_for_ambient_noise(fonte)
    print("Fale alguma coisa")
    # EXECUTA A FUNÇÃO DE ESCUTAR JÁ COM O RUIDO FILTRADO
    audio = r.listen(fonte)
    print("Enviando para reconhecimento")

    # A ideia do try except é testar pontos críticos do código, ou seja,
    # lugares que onde há grande possibilidade de erros.
    try:
        # transcrevendo fala em texto com api da Google
        text = r.recognize_google(audio, language="pt-BR")
        # IMPRIMI NA TELA O TEXTO RECONHECIDO
        print("Você disse: {}".format(text))

        # O PACOTE PYTTSX3 CAHAMA A FUNÇAÕ INIT PARA INICIAR O CODIGO COM UM PADRÃO
        engine = pyttsx3.init()
        # ORGANIZA EM FILA O AUDIO QUE SERÁ EXECUTADO
        engine.say("Você disse: {}".format(text))
        # ORGANIZA A FILA E VAI EXECUTANDO O AUDIO ATÉ A LISTA ESTA VAZIA
        engine.runAndWait()
        # PARA A REPRODUÇÃO E LIMPA A FILA
        engine.stop()
    # EXCEÇÃO
    except:
        engine = pyttsx3.init()
        engine.say("Desculpa, não entendi o que você disse, pode repetir?")
        engine.runAndWait()
        engine.stop()
        print("Não entendi o que você disse")