from langchain.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate

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



def AnswerAnalyzPrompt(domain_name, topic_name, question, answer):

    out_temp = '{"Result": "CORRECT or WRONG", "Score": "<percentage>%", "Reason": "<short explanation>"}'

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

