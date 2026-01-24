from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage


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
