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


def DescPrompt(additional_note, user_data, job_desc = None):

    sys_message = SystemMessage(content='You are a professional and expert on english and cv writer. Your task to write description for cv based on the user biography data and job description (if any). And formate and other changes based on additional user instraction')
    hum_message = HumanMessage(content=f"Additional instraction from user : {additional_note}User Biography data: {user_data}\n\nJob Description: {job_desc}")

    temp = PromptTemplate(
        template="{sys_message}.\n {hum_message}",
        input_types=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(input={
        'sys_message': sys_message,
        'hum_message': hum_message
    }).text


    return prompt