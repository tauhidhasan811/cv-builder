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
    if score >=85:
        return "A"
    elif score >=70:
        return "B"
    elif score >=50:
        return "C"
    else:
        return "D"

def WTprompt(role_contex , case_briefing, email_draft):
    sys_message = SystemMessage(
    content=(
        "You are a professional written assessment evaluator."
        "Evaluate the quality of the email draft ONLY in terms of:"
        "- Role alignment"
        "- Case understanding"
        "- Tone and professionalism"
        "- Clarity and structure"

        "Return a JSON object with:"
        "- contentScore (integer 0–100)"
        "- feedback (string)"
        "- recommendations (array of strings)"
        "- Written CaseStudy SuccessTips as successTips (array of strings)"

        "Do NOT calculate word count, completion rate, or grades."
        "Return valid JSON only."

    )
)


    hum_message = HumanMessage(
        content=(
            f"Role Context:\n{role_contex}\n\n"
            f"Case Briefing:\n{case_briefing}\n\n"
            f"Email Draft:\n{email_draft}"
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