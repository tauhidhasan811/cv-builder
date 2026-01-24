from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage


def in_tray_email_prompt(instructions, email_draft):
    sys_message = SystemMessage(
        content=(
            "You are a professional in-tray email assessment evaluator."
            "Evaluate the quality of the email draft ONLY in terms of:"
            "- Adherence to instructions"
            "- Tone and professionalism"
            "- Clarity and structure"
            "Return a JSON object with:"
            "- prioritization (string)"
            "- judgment (string)"
            "- commercialAwarness (string)"
            "- contextUnderstanding (string)"
            "- riskAssessment (string)"
        
        )
    )


    hum_message = HumanMessage(
        content=(
            f"instructions: \n{instructions}"
            f"email draft:\n{email_draft}"
        )
    )

    temp = PromptTemplate(
            template = "{sys_message}\n\n{hum_message}",
            input_variables=['sys_message', 'hum_message']
        )


    prompt= temp.invoke(
        input = {
            'sys_message': sys_message.content,
            'hum_message': hum_message.content
        }
    )

    return prompt.text