from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def CVPrompt(user_data, additional_note):
    sys_message = SystemMessage(content="Imagine you are a professional CV writer. Your task is to create a detailed CV based on the provided job description and the user's personal bio data.")
    hum_message = HumanMessage(content=f"User Bio: \n{user_data}")

    temp = PromptTemplate(
        template="{sys_message}\n. {hum_message} \n. Additional User Input: {additional_note}",
        input_variables=['sys_message', 'hum_message', 'additional_note']
    )

    prompt = temp.invoke(input={
         'sys_message': sys_message.content,
         'hum_message': hum_message.content,
         'additional_note': additional_note
    })

    return prompt.text


def DescPrompt(job_summary, job_information):
    sys_message = SystemMessage(content="You are an expert and professional CV description writer. Your task is to refine and enhance the user-provided job summary strictly based on the given job experience information. The output will be used directly in a CV. Do not hallucinate, assume, or infer any information. Do not add, remove, or modify facts beyond the provided content. Improve clarity, professionalism, and impact while preserving the original meaning and accuracy.")
    hum_message = HumanMessage(content=f"Job expreance information: {job_information}\n\nUser written summary: {job_summary}")

    temp = PromptTemplate(
        template="{sys_message}.\n {hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(input={
        'sys_message': sys_message.content,
        'hum_message': hum_message.content
    }).text
    print('--------------------------------------')
    print(prompt)
    return prompt

def SummPrompt(user_summary, user_data):

    sys_message = SystemMessage(content="You are a professional and expert CV objective writer. Your task is to write or refine a CV objective strictly based on the user’s pre-written objective (if provided) and the supplied biography data. Apply formatting and stylistic improvements only if explicitly instructed by the user. Do not hallucinate, infer, or introduce any new information. Do not add any words, facts, or claims outside the provided content. Ensure the objective is concise, professional, and suitable for a CV. And objective will be within 80 to 100 words")
    hum_message = HumanMessage(content=f"user Written objective : {user_summary}User Biography data: {user_data}")

    temp = PromptTemplate(
        template="{sys_message}.\n {hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(input={
        'sys_message': sys_message.content,
        'hum_message': hum_message.content
    }).text
    print('--------------------------------------')
    print(prompt)
    return prompt