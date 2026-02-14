from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

def word_count(text):

    text_len  = len(text.strip().split())
    return text_len

COMP_RATE = {
    "min_words": 120,
    "ideal_words": 260,
    "max_words": 300
}

def completion_rate(text):
    words = word_count(text)

    if words < COMP_RATE["min_words"]:
        return round((words / COMP_RATE["min_words"]) * 100)

    if words > COMP_RATE["max_words"]:
        return round((COMP_RATE["max_words"] / words) * 100)
    if words < COMP_RATE["ideal_words"]:
        return round((words / COMP_RATE["ideal_words"]) * 100)

    return 100


def overall_grade(score):
    if score >= 85:
        return "A"  
    elif score >= 70:
        return "B"  
    elif score >= 50:
        return "C"  
    elif score >= 35:
        return "D"  
    else:
        return "F"  
    

def generate_question_prompt():
    sys_message = SystemMessage(
        content="\n".join([
            "You are a legal assessment content generator for an online legal study and job preparation platform.",
            "",
            "Your task is to generate a COMPLETE, REALISTIC legal written assessment consisting of TWO parts (for the student to answer):",
            "",
            "1. roleContext",
            "2. caseStudy",
            "",
            "The generated content must be suitable for law students or early-career legal professionals.",
            "",
            "GENERAL RULES:",
            "- All content must be law-related and professionally realistic.",
            "- The scenario must resemble real-world legal assessments used in internships, trainee roles, or written exams.",
            "- Avoid giving the answer; the student will provide their own response.",
            "- Maintain professional tone and realistic details.",
            "",
            "CONTENT REQUIREMENTS:",
            "ROLE CONTEXT:",
            "- Clearly define the role (e.g., law student, legal intern, junior associate).",
            "- Mention the setting (law firm, corporate legal team, chambers, legal aid organization).",
            "- State the expectation level (e.g., basic legal analysis, structured reasoning, professional tone).",
            "",
            "CASE STUDY:",
            "- Present a detailed but realistic legal scenario.",
            "- Focus on common legal domains such as Contract law, Tort law, Employment law, Company/Commercial law, Property law.",
            "- Include enough facts to allow legal issue identification and analysis.",
            "- Avoid giving the legal answer.",
            "",
            "OUTPUT FORMAT:",
            "Return a VALID JSON object with EXACTLY the following keys:",
            "{",
            "  \"roleContext\": string,",
            "  \"caseStudy\": string",
            "}",
            "",
            "Do NOT add explanations, headings, or extra fields.",
            "Return JSON only."
            "Important Reminder: All response text must be written in British English."
        ])
    )

    hum_message = HumanMessage(
        content="Generate a complete legal written assessment as per the above instructions."
    )

    return [sys_message, hum_message]

  

def WTprompt(role_context, case_briefing, written_submission):
    sys_message = SystemMessage(
        content=(
            "You are a professional legal written assessment evaluator.\n\n"

            "You will be provided with:\n"
            "1. Role context (e.g., law student, junior associate, legal intern)\n"
            "2. Case briefing or legal scenario\n"
            "3. A written legal submission based on the case\n\n"

            "The submission may be an email, case brief, legal memo, problem answer, "
            "or any other form of legal writing.\n\n"

            "Evaluate the submission ONLY on the following criteria:\n"
            "- Role alignment and appropriateness for the legal position\n"
            "- Legal issue identification and case understanding\n"
            "- Application of legal principles, precedent, or reasoning (where applicable)\n"
            "- Tone, professionalism, and legal writing standards\n"
            "- Clarity, structure, and logical flow\n\n"

            "Do NOT rewrite, correct, summarize, or respond to the submission.\n"
            "Do NOT assume a specific document format unless explicitly stated.\n"
            "Do NOT introduce new legal arguments, authorities, or facts.\n\n"

            "Return a VALID JSON object with EXACTLY the following fields:\n"
            "- contentScore (integer from 0 to 100)\n"
            "- feedback (string summarizing overall performance)\n"
            "- recommendations (array of specific, actionable improvement suggestions as strings)\n"
            "- successTips (array of general tips for succeeding in legal written case studies)\n\n"

            "Do NOT calculate word count, grades, completion rate, or academic scores.\n"
            "Return JSON only. No markdown. No explanations outside JSON."
            "Important Reminder: All response text and spellings must be written in British English ."
        )
    )



    hum_message = HumanMessage(
        content=(
            f"Role Context:\n{role_context}\n\n"
            f"Case Briefing:\n{case_briefing}\n\n"
            f"Email Draft:\n{written_submission}"
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


#testing the functions with dummy text data
# if __name__ == "__main__":

#     sample_text = "This is a sample cover letter text to test the word count and completion rate functions."
#     print("Word Count:", word_count(sample_text))
#     print("Completion Rate:", completion_rate(sample_text))