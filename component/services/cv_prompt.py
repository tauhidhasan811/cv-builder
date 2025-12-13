from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def CVPrompt(user_text, user_data):
    sys_message = SystemMessage(content="Imagine you are a professional CV writer. Your task is to create a detailed CV based on the provided job description and the user's personal bio data.")
    hum_message = HumanMessage(content=f"User Bio: \n{user_data}")

    temp = PromptTemplate(
        template="{sys_message}\n. {hum_message} \n. Additional User Input: {user_text}",
        input_variables=['sys_message', 'hum_message', 'user_text']
    )

    prompt = temp.invoke(input={
         'sys_message': sys_message.content,
         'hum_message': hum_message.content,
         'user_text': user_text
    })

    return prompt.text
