from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

def CLPrompt(user_data, job_desc, additional_note):
    sys_message = SystemMessage(content="Imagine you are a professional cover letter writer. Your task is to create a detailed CV based on the provided job description and the user's personal bio data.")
    hum_message = HumanMessage(content=f"User Bio: \n{user_data}\nJob description: {job_desc}")

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