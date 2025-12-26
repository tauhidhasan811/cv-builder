from langchain_core.prompts import PromptTemplate
from langchain.messages import SystemMessage, HumanMessage


def MockTestPrompt(domain_name, num_of_question, def_level):
    out_temp = "[{'question': '<question_text>'}]"

    sys_message = SystemMessage(
        content=(
            f"You are an examiner creating a mock test in the domain of {domain_name}. "
            f"Generate exactly {num_of_question} questions. "
            f"The difficulty level of all questions must be {def_level}. "
            f"All questions must be standard, relevant, and strictly limited to the {domain_name} domain. "
            f"Do not include content from outside this domain and do not hallucinate facts. "
            f"Return ONLY valid list of JSON in the following format, with no extra text:\n"
            f"{out_temp}"
        )
    )

    temp = PromptTemplate(
        template="{sys_message}",
        input_variables=['sys_message']
    )
    prompt = temp.invoke({
        'sys_message': sys_message.content
    }).text

    return prompt
