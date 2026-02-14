from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

def written_presentation_ques_generator():

    sys_message = SystemMessage(
        content=(
            "You are an AI assessment designer creating written presentation tasks "
            "for professional candidates."

            "Generate a realistic case study based on a real-world business or technical scenario."

            "The output MUST include:"
            "1. A caseStudy section describing the situation and problem"
            "2. An instructions section explaining what the candidate must write"
            "3. A proTips section giving guidance on structure and tone"

            "Rules:"
            "- Do NOT provide solutions"
            "- Do NOT include evaluation criteria"
            "- The task should require at least 300 words to answer"
            "- Keep the scenario realistic and mid-complexity"

            "Return valid JSON only with keys:"
            "- caseStudy (string)"
            "- instructions (array of strings)"
            "- proTips (array of strings)"
            'Important Reminder: All response text and spellings must be written in British English .'
        )
    )

    hum_message = HumanMessage(
        content="Generate a written presentation task."
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



def Written_presentation_prompt(case_study, instructions, pro_tips, written_submission):
    sys_message = SystemMessage(
        content=(
            "You are a professional written presentation task evaluator. "
            "You will be provided with a case study, instructions, pro tips, and the user's written submission. "
            "Evaluate the quality of the written presentation based on:\n"
            "- How well it addresses the case study requirements\n"
            "- Adherence to the provided instructions\n"
            "- Clarity and structure\n"
            "- Professional tone and language\n"
            "- Completeness and depth of analysis\n"
            "Word count should be at least 300 words.\n\n"
            "Return a JSON object with:\n"
            "- contentScore (integer 0–100)\n"
            "- feedback (string with specific strengths and areas for improvement)\n"
            "Return valid JSON only, no additional text."
            'Important Reminder: All response text and spellings must be written in British English .'
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Case Study:\n{case_study}\n\n"
            f"Instructions:\n{instructions}\n\n"
            f"Pro Tips:\n{pro_tips}\n\n"
            f"User's Written Submission:\n{written_submission}\n\n"
            "Please evaluate this submission based on the criteria provided."
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