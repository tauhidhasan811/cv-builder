from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage


def in_tray_email_ques_generator():
    sys_message = SystemMessage(
        content=(
            "You are an AI assessment designer creating in-tray email tasks for legal professionals "
            "or law exam candidates. Generate a realistic in-tray email scenario based on a real-world "
            "business or legal context.\n\n"
            "The output MUST include:\n"
            "1. instructions: a clear short description of the email task and expectations\n"
            "2. draftEmail: the email content that the candidate is required to respond to\n\n"
            "Rules:\n"
            "- Do NOT provide the candidate's solution or response\n"
            "- The task should require at least 300 words to answer\n"
            "- Keep the scenario realistic and mid-complexity\n"
            "- Return valid JSON only\n\n"
            "Return JSON keys exactly as:\n"
            "- instructions (string)\n"
            "- draftEmail (string)"
            "Important Reminder: All response text must be written in British English."
        )
    )

    hum_message = HumanMessage(
        content="Generate an in-tray email task."
    )

    prompt_temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=["sys_message", "hum_message"]
    )

    final_prompt = prompt_temp.invoke(
        {
            "sys_message": sys_message.content,
            "hum_message": hum_message.content
        }
    )

    return final_prompt.text

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
            "Important Reminder: All response text and spellings must be written in British English ."
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