from langchain_core.prompts import PromptTemplate
from langchain.messages import SystemMessage, HumanMessage


def MockQuesPrompt(domain_name, topic_name, num_of_question, def_level):
    out_temp = '[{"question": "<question_text>"}]'

    sys_message = SystemMessage(
        content=(
            f"You are an examiner creating a mock test in the domain '{domain_name}' and topic '{topic_name}'. "
            f"Generate exactly {num_of_question} questions of difficulty '{def_level}'. "
            "All questions must be strictly relevant to this domain and topic, with no hallucinations or extra text. "
            "Return the result as a valid JSON array of objects, with exactly the following format and using **double quotes**:\n"
            f"{out_temp}\n"
            "Do NOT include explanations, numbering, markdown, or any extra text. Only valid JSON array."
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


"""def AnswerAnalyzPrompt(domain_name, topic_name, question, answer):
    sys_message = SystemMessage(
        content=f"You are a expert eximiner on domain {domain_name} and on topic {topic_name}"
                "Your task is check the answer is correct or not "
                "if answer is cortrect more then 80% then conside it as correct answe otherway wrong answer"
                )
    hum_message = HumanMessage(
        content=f"Question was : {question}\n\n Naswer: {answer}"
    )

    temp = PromptTemplate(
        template="{sys_message} \n\n {hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'hum_message': hum_message.content
        }
    )

    return prompt.text
    """


def MockAnsPrompt(domain_name, topic_name, question, answer):

    out_temp = '{"result": "CORRECT or WRONG", "score": "<percentage>%", "correct_answer": "<short explanation>"}'

    sys_message = SystemMessage(
        content=(
            f"You are an expert examiner in the domain of '{domain_name}' "
            f"and specifically in the topic '{topic_name}'.\n\n"
            "Your task is to evaluate the student's answer based on factual correctness, "
            "conceptual accuracy, and relevance to the question.\n\n"
            "Evaluation Rules:\n"
            "1. Compare the answer directly with the question requirements.\n"
            "2. If the answer is at least 80% correct, classify it as CORRECT.\n"
            "3. If the answer is less than 80% correct, classify it as WRONG.\n"
            "4. Be strict but fair in your judgment.\n\n"
            f"Return the result in the following format only as a JSON:\n{out_temp}"
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Question:\n{question}\n\n"
            f"Student Answer:\n{answer}"
        )
    )

    temp = PromptTemplate(
        template="{sys_message}\n\n{hum_message}",
        input_variables=["sys_message", "hum_message"]
    )

    prompt = temp.invoke(
        {
            "sys_message": sys_message.content,
            "hum_message": hum_message.content
        }
    )

    return prompt.text 

#update prompt as needed 
def MokeEvaluatePrompt(segment, question, answer):

    prompt = f"""
        You are an interview evaluator.

        interview Segment: {segment}

        Question: {question}
        Candidate Answer:
        {answer}

        Evaluate The answer on a scale of 0-100 for each catagory:

        1.Content_Quality 
        2.Clarity_Structure
        3.Communication
        4.Professional_Attitude

        Return ONLY Valid JSON in this format : 

        {{
        "content_quality": number,
        "clarirty_structure": number,
        "communication": number,
        "professional_attitude": number,
        "feedback": {{
            "content_quality": "text",
            "clarirty_structure": "text",
            "communication": "text",
            "professional_attitude": "text",
        }}
        }}
        """
    
    return prompt