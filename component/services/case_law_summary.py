from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

def generate_case_law_summary_question():
    sys_message = SystemMessage(
        content=(
            "You are an AI legal assessment content generator creating case law summary tasks "
            "for law students or early-career legal professionals. Generate a realistic case law summary "
            "scenario based on a real-world legal context.\n\n"
            "The output MUST include:\n"
            "1. precedentSummary: a summary of a relevant legal precedent\n"
            "2. pretendCase: a new legal case that the candidate must relate to the precedent\n\n"
            "Rules:\n"
            "- Do NOT provide the candidate's solution or response\n"
            "- The task should require at least 200 words to answer\n"
            "- Keep the scenario realistic and mid-complexity\n"
            "- Return valid JSON only\n\n"
            "Return JSON keys exactly as:\n"
            "- precedentSummary (string)\n"
            "- pretendCase (string)"
            "Important Reminder: All response text must be written in British English."
        )
    )
    hum_message = HumanMessage(
        content="Generate a case law summary task."
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




def case_law_summary_prompt(precedent_summary, pretend_case, your_summary):
    sys_message = SystemMessage(
        content=(
            "You are a professional legal case law summary evaluator."
            "Evaluate the quality of the case law summary ONLY in terms of:"
            "- Accuracy in reflecting the precedent summary"
            "- Relevance to the pretend case"
            "- Clarity and conciseness"

            "Return a JSON object with:"
            "- identification of the legal issue as 'legalIssue' (string)"
            "- ability to link precedent summary to a new case as as 'caseLinking' (string)"
            "- quality of their summary as 'summaryQuality' (string)"
            "Return valid JSON only."
            "Important Reminder: All response text must be written in British English."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Precedent Summary:\n{precedent_summary}\n\n"
            f"Pretend Case:\n{pretend_case}\n\n"
            f"Your Case Law Summary:\n{your_summary}"
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
