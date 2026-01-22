from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

def Written_presentation_prompt(text):

    sys_message = SystemMessage(
        content=(
            "You are a professional written presentation evaluator."
            "Evaluate the quality of the written presentation ONLY in terms of:"
            "- Clarity and structure"
            "- Professional tone"
            "word count should be at least 300 words."
            "Return a JSON object with:"
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Here is the written presentation to evaluate:\n\n{text}"
        )
    )

    prompt_temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=["sys_message", "hum_message"]
    )

    final_prompt = prompt_temp.invoke(
        input={
            "sys_message": sys_message.content,
            "hum_message": hum_message.content
        }
    )

    return final_prompt.text