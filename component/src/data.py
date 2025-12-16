formatted_data = {
    "user_id": "user111",
    "session_id": "sess_abc123",
    "test_type": "verbal_reasoning",
    "performance": {
        "overall": {
            "score": 10,
            "total": 15,
            "accuracy_pct": 66.7
        },
        "skill_breakdown": {
            "reading_comprehension": 60,
            "critical_reasoning": 66.7,
            "vocabulary": 75
        },
         "time_analysis": {
    "avg_time_sec": 55,
    "time_pressure_errors": 4
  },
  "difficulty_breakdown": {
    "easy": 90,
    "medium": 60,
    "hard": 30
  },
    }
}

def format_test_result(test_result):
    return (
        f"Overall: score={test_result['performance']['overall']['score']}/"
        f"{test_result['performance']['overall']['total']}, "
        f"accuracy={test_result['performance']['overall']['accuracy_pct']}\n"
        f"Skills: RC={test_result['performance']['skill_breakdown']['reading_comprehension']}, "
        f"CR={test_result['performance']['skill_breakdown']['critical_reasoning']}, "
        f"Vocab={test_result['performance']['skill_breakdown']['vocabulary']}\n"
        f"Time: avg={test_result['performance']['time_analysis']['avg_time_sec']}s, "
        f"errors={test_result['performance']['time_analysis']['time_pressure_errors']}\n"
        f"Difficulty: easy={test_result['performance']['difficulty_breakdown']['easy']}, "
        f"medium={test_result['performance']['difficulty_breakdown']['medium']}, "
        f"hard={test_result['performance']['difficulty_breakdown']['hard']}"
    )
# # Original verbose formatting function

# def format_test_result(test_result: dict) -> str:
#     return (
#         f"User ID: {test_result['user_id']}\n"
#         f"Session ID: {test_result['session_id']}\n"
#         f"Test Type: {test_result['test_type']}\n\n"

#         "Overall Performance:\n"
#         f"- Score: {test_result['performance']['overall']['score']} / "
#         f"{test_result['performance']['overall']['total']}\n"
#         f"- Accuracy: {test_result['performance']['overall']['accuracy_pct']}%\n\n"

#         "Skill Breakdown:\n"
#         f"- Reading Comprehension: {test_result['performance']['skill_breakdown']['reading_comprehension']}%\n"
#         f"- Critical Reasoning: {test_result['performance']['skill_breakdown']['critical_reasoning']}%\n"
#         f"- Vocabulary: {test_result['performance']['skill_breakdown']['vocabulary']}%\n\n"

#         "Time Analysis:\n"
#         f"- Average Time per Question: {test_result['performance']['time_analysis']['avg_time_sec']} sec\n"
#         f"- Time Pressure Errors: {test_result['performance']['time_analysis']['time_pressure_errors']}\n\n"

#         "Difficulty Breakdown:\n"
#         f"- Easy: {test_result['performance']['difficulty_breakdown']['easy']}%\n"
#         f"- Medium: {test_result['performance']['difficulty_breakdown']['medium']}%\n"
#         f"- Hard: {test_result['performance']['difficulty_breakdown']['hard']}%\n"
#     )


# print(format_test_result(formatted_data))
