from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
import random 
from component.services.constants import PRECEDENT_CASES
def generate_case_law_summary_question():
    precedent, legal_area, industry = random.choice(PRECEDENT_CASES)
    sys_message = SystemMessage(
        content=(
            "You are an AI legal assessment content generator creating case law summary tasks "
            "for law students or early-career legal professionals.\n\n"
            f"This task MUST be based on the legal area: {legal_area}\n"
            f"The precedent case MUST be: {precedent}\n"
            f"The pretendCase MUST be set in the {industry} industry.\n\n"
            "The output MUST include:\n"
            "1. precedentSummary: an accurate and detailed summary of the specified precedent case\n"
            "2. pretendCase: a brand new fictional case the candidate must relate to the precedent. "
            "The fictional case must involve completely different parties, facts, and context "
            "from the precedent — do not mirror the original facts too closely.\n\n"
            "Rules:\n"
            "- Do NOT provide the candidate's solution or response\n"
            "- The task should require at least 200 words to answer\n"
            "- Keep the scenario realistic and mid-complexity\n"
            "- The pretendCase must feel genuinely distinct from the precedent facts\n"
            "- Return valid JSON only\n\n"
            "Return JSON keys exactly as:\n"
            "- precedentSummary (string)\n"
            "- pretendCase (string)\n\n"
            "Important Reminder: All response text must be written in British English."
        )
    )
    hum_message = HumanMessage(
        content=(
            f"Generate a case law summary task for {legal_area} "
            f"using {precedent}, set in the {industry} industry."
        )
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
    "You are a professional legal case law summary evaluator. "

    "Evaluate the student's summary ONLY in terms of: "
    "1. Accuracy in reflecting the precedent summary. "
    "2. Relevance to the pretend case. "
    "3. Clarity and conciseness. "

    "Return a VALID JSON object with EXACTLY the following fields: "
    "{ "
     "- contentScore:integer from 0 to 100\n"
    "\"legalIssue\": string, "
    "\"caseLinking\": string, "
    "\"summaryQuality\": array of EXACTLY 4 strings "
    "} "

    "The 'summaryQuality' field must contain concise evaluation points. "
    "Do not return markdown. Do not add extra fields. "

    "Important Reminder: All response text and spellings must be written in British English."
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
    # print("Precendent Summary:", precedent_summary)
    # print("Pretend Case:", pretend_case)
    # print("Your Summary:", your_summary)

    return final_prompt.text
