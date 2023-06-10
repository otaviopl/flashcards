import openai


openai.api_key = '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'

def criar_flashcards(materia, conteudo):
    prompt = f"Matéria: {materia}\nConteúdo: {conteudo}\nFlashcard:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    flashcard = response.choices[0].text.strip()
    return flashcard

def criar_pergunta_resposta(pergunta, resposta):
    prompt = f"Pergunta: {pergunta}\nResposta:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    resposta_completa = response.choices[0].text.strip()
    return resposta_completa

def criar_plano_de_estudos(materias):
    prompt = "Plano de Estudos:\n"
    for i, materia in enumerate(materias, start=1):
        prompt += f"\n{i}. {materia}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    plano_de_estudos = response.choices[0].text.strip()
    return plano_de_estudos