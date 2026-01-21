from langchain.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

def JobRecommondationPrompt(cv_data):
    temp = {
        'job_posts': ['list of job post names only']
    }
    sys_message = SystemMessage(
            content=(
            "You are a professional career advisor. "
            "Based on the provided CV data, recommend suitable job postings that align with the candidate's skills and experience. "
            "Return the output strictly in the following dictionary format and include only job titles:\n"
            f"{temp}"
        )
    )

    hum_message = HumanMessage(
        content=f"CV Data:\n{cv_data}"
    )

    temp = PromptTemplate(
        template="System Instraction: {sys_message}. Human Input: {hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke({
        'sys_message': sys_message.content,
        'hum_message': hum_message.content
    }).text

    return prompt