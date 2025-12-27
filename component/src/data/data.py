# data.py
# api_data = {
#     "user_id": "user111",
#     "session_id": "sess_abc123",
#     "test_type": "verbal_reasoning",
#     "performance": {
#         "overall": {"score": 10, "total": 15, "accuracy_pct": 66.7},
#         "skill_breakdown": {
#             "reading_comprehension": 60,
#             "critical_reasoning": 66.7,
#             "vocabulary": 75
#         },
#         "time_analysis": {"avg_time_sec": 55, "time_pressure_errors": 4},
#         "difficulty_breakdown": {"easy": 90, "medium": 60, "hard": 30}
#     }
# }

# from sqlalchemy import true


api_data = {
    "statusCode": 201,
    "success": True,
    "message": "Psychometric test created successfully",
    "data": {
        "_id": "694b7db326ecb3faba1bd729",
        "user": "69366af45f4eab38f19b579a",
        "test": {
            "_id": "69425360bf7573f3427adba9",
            "title": "Verbal Reasoning Test"
        },
        "answers": [
            {
                "questionId": "69425360bf7573f3427adbaa",
                "userAnswer": "Sharing progress and challenges before being asked",
                "isCorrect": True,
                "timeTakenSec": 12,
                "_id": "694b7db326ecb3faba1bd72a"
            },
            {
                "questionId": "69425360bf7573f3427adbab",
                "userAnswer": "All managers are leaders, John is a leader, therefore John is a manager",
                "isCorrect": False,
                "timeTakenSec": 8,
                "_id": "694b7db326ecb3faba1bd72b"
            },
            {
                "questionId": "69425360bf7573f3427adbac",
                "userAnswer": "They support the conclusion implicitly",
                "isCorrect": True,
                "timeTakenSec": 8,
                "_id": "694b7db326ecb3faba1bd72c"
            }
        ],
        "testScore": 2,
        "totalQuestions": 3,
        "accuracyPct": 66.67,
        "timeAnalysis": {
            "avgTimeSec": 9.33,
            "timePressureErrors": 1
        },
        "difficultyBreakdown": {
            "easyQuestions": 1,
            "mediumQuestions": 1,
            "hardQuestions": 1
        },
        "correctedAnswers": {
            "totalCorrectedAnswers": 2,
            "easyCorrectedAnswers": 1,
            "mediumCorrectedAnswers": 0,
            "hardCorrectedAnswers": 1
        },
        "createdAt": "2025-12-24T05:44:19.727Z",
        "updatedAt": "2025-12-24T05:44:19.727Z",
        "__v": 0
    }
}


# def compress_test_result(data: dict) -> str:
#     p = data["performance"]

#     return (
#         f"Overall {p['overall']['score']}/{p['overall']['total']} "
#         f"({p['overall']['accuracy_pct']}%)\n"
#         f"Skills RC{p['skill_breakdown']['reading_comprehension']} "
#         f"CR{int(p['skill_breakdown']['critical_reasoning'])} "
#         f"V{p['skill_breakdown']['vocabulary']}\n"
#         f"Time {p['time_analysis']['avg_time_sec']}s "
#         f"err{p['time_analysis']['time_pressure_errors']}\n"
#         f"Diff E{p['difficulty_breakdown']['easy']} "
#         f"M{p['difficulty_breakdown']['medium']} "
#         f"H{p['difficulty_breakdown']['hard']}"
#     )

def format_psychometric_data(api_data: dict) -> dict:
    d = api_data["data"]

    text = (
        f"Test {d['test']['title']}\n"
        f"Score {d['testScore']}/{d['totalQuestions']} "
        f"({d['accuracyPct']}%)\n"
        f"Time {d['timeAnalysis']['avgTimeSec']}s "
        f"err{d['timeAnalysis']['timePressureErrors']}\n"
        f"Diff E{d['difficultyBreakdown']['easyQuestions']} "
        f"M{d['difficultyBreakdown']['mediumQuestions']} "
        f"H{d['difficultyBreakdown']['hardQuestions']}\n"
        f"Corrected {d['correctedAnswers']['totalCorrectedAnswers']}"
    )

    return {
        "session_id": d["_id"],
        "text": text
    }

formatted_data = format_psychometric_data(api_data)
