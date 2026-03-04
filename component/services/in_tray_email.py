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
def in_tray_email_prompt(instructions, draft_email, answer_email):
    sys_message = SystemMessage(
        content=(
            "You are a professional in-tray email assessment evaluator. "
            "You will be given: "
            "1. The task instructions the candidate was given. "
            "2. The original draft email the candidate was asked to respond to. "
            "3. The candidate's reply email. "

            "Evaluate the candidate's reply ONLY in terms of the following criteria: "
            "1. Adherence to instructions. "
            "2. Tone and professionalism. "
            "3. Clarity and structure. "
            "4. Contextual understanding of the original email. "
            "5. Commercial awareness and risk assessment. "

            "Return a VALID JSON object with EXACTLY the following fields: "
            "{"
            "\"prioritization\": string, "
            "\"judgment\": string, "
            "\"commercialAwareness\": string, "
            "\"contextUnderstanding\": string, "
            "\"riskAssessment\": string, "
            "\"contentScore\": integer from 0 to 100 "
            "} "

            "The 'contentScore' should reflect the overall quality based on the above criteria. "
            "Do not add any additional fields or explanations. "
            "All text must be written in British English."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Task Instructions:\n{instructions}\n\n"
            f"Original Draft Email:\n{draft_email}\n\n"        
            f"Candidate's Reply Email:\n{answer_email}"
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
    )

    return prompt.text