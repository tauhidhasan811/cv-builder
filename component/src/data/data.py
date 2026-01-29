

def format_psychometric_data(api_data: dict) -> dict:
    data = api_data.get("data", {})
    test = data.get("test", {})

    # Extract category
    category = test.get("category")

    # Extract questions
    questions = []
    for q in test.get("allQuestions", []):
        questions.append({
            "question": q.get("question"),
            "options": q.get("options", []),
            "correctAnswer": q.get("answer"),
            "difficulty": q.get("difficulty")
        })

    # Extract answers
    answers = []
    for a in data.get("answers", []):
        answers.append({
            "questionId": a.get("questionId"),
            "userAnswer": a.get("userAnswer"),
            "isCorrect": a.get("isCorrect"),
            "timeTakenSec": a.get("timeTakenSec")
        })
    
    summary_text = f"Category: {test.get('category')}, Score: {data.get('score')}. " \
                   f"{len(test.get('allQuestions', []))} questions attempted."

    return {
        "category": category,
        "score": data.get("score"),
        "questions": questions,
        "answers": answers,
        "text": summary_text
    }





# def format_psychometric_data(api_data: dict) -> dict:
#     d = api_data["data"]

#     text = (
#         f"Test {d['test']['category']}\n"
#         f"Score {d['testScore']}/{d['totalQuestions']} "
#         f"({d['accuracyPct']}%)\n"
#         f"Time {d['timeAnalysis']['avgTimeSec']}s "
#         f"err{d['timeAnalysis']['timePressureErrors']}\n"
#         f"Diff E{d['difficultyBreakdown']['easyQuestions']} "
#         f"M{d['difficultyBreakdown']['mediumQuestions']} "
#         f"H{d['difficultyBreakdown']['hardQuestions']}\n"
#         f"Corrected {d['correctedAnswers']['totalCorrectedAnswers']}"
#     )

#     return {
#         "session_id": d["_id"],
#         "text": text
#     }

# formatted_data = format_psychometric_data(api_data)
