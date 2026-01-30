from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage


def psycho_test_prompt(raw_insights):
    sys_message = SystemMessage(
        content=(
            "You are a psychometric assessment summarization expert.\n"
            "Your task is to rewrite the given formatted psychometric test data into concise, clear natural language.\n\n"
            "Rules:\n"
            "- Follow the output format EXACTLY\n"
            "- Do not add explanations, headings, or extra text\n"
            "- Keep language neutral, professional, and non-clinical\n"
            "- Be direct and concise\n\n"
            "Output JSON format:\n"
            "{\n"
            '  "keyStrength": "5–7 words",\n'
            '  "areaImprovement": "5–7 words",\n'
            '  "feedback": "1–2 short lines"\n'
            "}"
        )
    )
    # hum_message = f"Psychometric insights to rewrite:\n{raw_insights}"

    # Return simple string prompt
    # return f"{sys_message}\n\n{hum_message}"

    hum_message = HumanMessage(
        content=(
            "Psychometric insights to rewrite:\n"
            f"{raw_insights}"
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