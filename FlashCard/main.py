import openai
import GETconteudo
import GETmateria

openai.api_key = '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'

def criar_flashcard(materia, conteudo):
    prompt = f"Matéria: {materia}\nConteúdo: {conteudo}\nFlashcard:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    flashcard = response.choices[0].text.strip()
    return flashcard

def criar_pergunta_resposta(pergunta, resposta):
    prompt = f"Pergunta: {pergunta}\nResposta:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    resposta_completa = response.choices[0].text.strip()
    return resposta_completa

def criar_plano_de_estudos(materias):
    prompt = "Plano de Estudos:\n"
    for i, materia in enumerate(materias, start=1):
        prompt += f"\n{i}. {materia}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    plano_de_estudos = response.choices[0].text.strip()
    return plano_de_estudos

def main():
    print("Começando os Estudos...\n")
    materia = input("Digite a matéria que deseja estudar hoje: ")
    conteudo = input("Digite o conteúdo da matéria: ")

    flashcard = criar_flashcard(materia, conteudo)
    print("Flashcard:", flashcard)

    pergunta = input("Digite uma pergunta: ")
    resposta = criar_pergunta_resposta(pergunta, "")
    print("Pergunta:", pergunta)
    print("Resposta:", resposta)

    num_materias = int(input("Digite o número de matérias para o plano de estudos: "))
    materias = []
    for i in range(num_materias):
        materia = input(f"Digite a matéria {i+1}: ")
        materias.append(materia)
    plano_de_estudos = criar_plano_de_estudos(materias)
    print("Plano de Estudos:", plano_de_estudos)


main()