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
    sys_message = SystemMessage(
        content=(
            "You are an expert and professional job description writer. "
            "Your task is to refine and enhance the user-provided job summary strictly "
            "based on the supplied job experience information. The output will be used "
            "directly in a CV. Do not hallucinate, assume, infer, or add any information "
            "not present in the provided data. Do not remove or alter facts beyond the "
            "original content. Focus on improving clarity, readability, professionalism, "
            "and impact while preserving the original meaning and accuracy."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Job experience information: {job_information}\n\n"
            f"User written summary: {job_summary}"
        )
    )

    temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'hum_message': hum_message.content
        }
    ).text

    return prompt


def SummPrompt(user_summary, user_data):

    summary_temp = (
        "Professional summary covering my educational background, relevant work "
        "experience, core skills, key achievements, and career objectives."
        "Reminder if any information is missing no warry just use those information avaiable and make objective "
    )

    sys_message = SystemMessage(
        content=(
            "You are a professional and expert CV objective writer. The CV objective must "
            f"cover the following areas: {summary_temp} "
            "Your task is to write or refine a CV objective strictly based on the user’s "
            "pre-written objective (if provided) and the supplied biography data. "
            "Do not hallucinate, infer, assume, or introduce any new information. "
            "Do not add any words, facts, achievements, or claims that are not explicitly "
            "present in the provided content. Improve clarity, structure, grammar, and "
            "professional tone only, unless the user explicitly requests stylistic changes. "
            "Ensure the final CV objective is concise, professional, and suitable for a CV. "
            "The length must be between 80 and 100 words, unless the user specifies a "
            "different maximum length."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"User written objective: {user_summary}\n\n"
            f"User biography data: {user_data}"
        )
    )

    temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=["sys_message", "hum_message"]
    )

    prompt = temp.invoke(
        input={
            "sys_message": sys_message.content,
            "hum_message": hum_message.content
        }
    ).text

    return prompt
