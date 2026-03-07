from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from .constants import PRECEDENT_CASES
import random

PRESENTATION_SCENARIOS = [
    ("employment law", "unfair dismissal and workplace disputes"),
    ("contract law", "breach of contract in commercial agreements"),
    ("company law", "director's duties and corporate governance"),
    ("tort law", "negligence and duty of care"),
    ("criminal law", "mens rea and criminal liability"),
    ("land law", "landlord and tenant disputes"),
    ("equity and trusts", "breach of fiduciary duty"),
    ("consumer law", "product liability and consumer rights"),
    ("employment law", "workplace discrimination"),
    ("administrative law", "judicial review of public authority decisions"),
    ("intellectual property", "copyright and trademark disputes"),
    ("commercial law", "agency and commercial contracts"),
    ("family law", "child custody and financial remedies"),
    ("criminal law", "defences and mitigation"),
    ("company law", "shareholder disputes and minority protection")
]

def written_presentation_ques_generator():
    legal_area, scenario_type = random.choice(PRESENTATION_SCENARIOS)

    sys_message = SystemMessage(
        content=(
            "You are an AI assessment designer creating verbal presentation tasks "
            "for law students and early-career legal professionals.\n\n"
            f"This task MUST be based on the legal area: {legal_area}\n"
            f"The scenario MUST involve: {scenario_type}\n\n"
            "Generate a realistic legal case study that the candidate must address "
            "in a spoken verbal presentation.\n\n"
            "The output MUST include:\n"
            "1. caseStudy: a detailed description of a realistic legal situation and problem "
            "the candidate must analyse and present on verbally\n"
            "2. instructions: clear guidance on what the candidate must cover in their spoken presentation\n"
            "3. proTips: helpful advice on how to structure and deliver an effective verbal presentation\n\n"
            "Rules:\n"
            "- Do NOT provide solutions or sample answers\n"
            "- Do NOT include evaluation criteria\n"
            "- The task should require at least 300 words to answer verbally\n"
            "- Keep the scenario realistic, legally grounded, and mid-complexity\n"
            "- The caseStudy must involve specific fictional parties, facts, and legal issues\n"
            "- Instructions and proTips should be tailored to the legal scenario\n\n"
            "Return valid JSON only with EXACTLY these keys:\n"
            "- caseStudy (string)\n"
            "- instructions (array of strings)\n"
            "- proTips (array of strings)\n\n"
            "Important Reminder: All response text and spellings must be written in British English."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Generate a verbal presentation task for {legal_area} "
            f"involving {scenario_type}."
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



def Written_presentation_prompt(case_study, instructions, pro_tips, written_submission):
    sys_message = SystemMessage(
        content=(
            "You are a professional verbal presentation evaluator assessing law students "
            "and early-career legal professionals.\n\n"
            "The candidate was given a case study and asked to deliver a spoken presentation. "
            "Their speech has been recorded, transcribed via speech-to-text, and provided to you below. "
            "Note: As this is a transcription of spoken language, minor grammatical informalities, "
            "filler words, or incomplete sentences should be taken into account and not penalised heavily.\n\n"
            "You will be provided with:\n"
            "1. A case study the candidate was asked to address verbally\n"
            "2. Instructions the candidate was given\n"
            "3. Pro tips provided to the candidate\n"
            "4. A transcription of the candidate's spoken presentation\n\n"
            "Evaluate the transcription based on the following criteria:\n"
            "- How well the spoken content addresses the case study requirements\n"
            "- Adherence to the provided instructions\n"
            "- Logical flow and organisation of spoken arguments\n"
            "- Clarity of verbal communication and legal reasoning\n"
            "- Depth and quality of legal analysis delivered verbally\n"
            "- Whether the transcription suggests sufficient spoken content (minimum 300 words)\n\n"
            "The 'contentScore' should reflect the overall quality of the spoken presentation "
            "based on all of the above criteria combined. "
            "A score of 0–49 reflects poor quality, 50–69 satisfactory, "
            "70–84 good, and 85–100 excellent.\n\n"
            "Return a VALID JSON object with EXACTLY the following fields:\n"
            "{\n"
            "  \"contentScore\": integer from 0 to 100,\n"
            "  \"feedback\": {\n"
            "    \"strengths\": string,\n"
            "    \"areasForImprovement\": string,\n"
            "    \"caseStudyRelevance\": string,\n"
            "    \"positiveObservations\": string\n"
            "  }\n"
            "}\n\n"
            "Do not return markdown. Do not add extra fields.\n"
            "All response text and spellings must be written in British English."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Case Study:\n{case_study}\n\n"
            f"Instructions:\n{instructions}\n\n"
            f"Pro Tips:\n{pro_tips}\n\n"
            f"Transcription of Candidate's Spoken Presentation:\n{written_submission}\n\n"
            "Please evaluate this spoken presentation transcription based on the criteria provided."
        )
    )

    temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=["sys_message", "hum_message"]
    )

    prompt = temp.invoke(
        input={
            "sys_message": sys_message.content,
            "hum_message": hum_message.content
        }
    )

    return prompt.text