from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

def CLPrompt(user_data, job_desc):
    sys_message = SystemMessage(
    content=(
        "You are a professional cover letter writer.\n"
        "Create a cover letter using ONLY the provided user data and job description.\n"
        "Do NOT add, assume, or hallucinate any information.\n\n"
        "Output requirements:\n"
        "- Return ONLY valid JSON (no markdown, no explanations).\n"
        "- The response must be directly parseable using json.loads().\n"
        "- The output must follow this structure:\n\n"

        "{\n"
        "  \"applicant\": {\n"
        "    \"firstName\": string,\n"
        "    \"lastName\": string,\n"
        "    \"email\": string,\n"
        "    \"phone\": string,\n"
        "    \"location\": string\n"
        "  },\n"
        "  \"coverLetter\": {\n"
        "    \"subject\": string,\n"
        "    \"paragraphs\": [string(Do not need to mention Dear someone or ..), string, ...]\n"
        "  }\n"
        "}\n\n"

        "Rules:\n"
        "- Each paragraph must be a single string.\n"
        "- Do NOT include newline characters inside paragraph strings.\n"

        "Important Reminder: All response text and spellings must be written in British English ."
    )
)


    hum_message = HumanMessage(
        content=(
            f"User Bio:\n{user_data}\n\n"
            f"Job description:\n{job_desc}"
        )
    )

    temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'hum_message': hum_message.content,
            #'additional_note': additional_note
        }
    )

    return prompt.text
