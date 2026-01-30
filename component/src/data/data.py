def format_psychometric_data(raw_data):
    """
    Format psychometric test data from API response
    """
    print(f"Raw data received: {raw_data}")
    
    # Handle different API response structures
    if 'data' in raw_data:
        data = raw_data['data']
        # Check if it's the new structure with 'attempt'
        if 'attempt' in data:
            attempt = data['attempt']
            user = attempt.get('user', {})
            test = attempt.get('test')
            answers = attempt.get('answers', [])
            score = attempt.get('score', 0)
            total_time = attempt.get('totalTime', 0)
            test_id = attempt.get('_id')
        else:
            # Old structure without 'attempt'
            user = data.get('user', {})
            test = data.get('test')
            answers = data.get('answers', [])
            score = data.get('score', 0)
            total_time = data.get('totalTime', 0)
            test_id = data.get('_id')
    else:
        raise ValueError("Invalid API response structure")
    
    # Validate test data
    if not test:
        raise ValueError("No test data found in response")
    
    # Extract test details
    category = test.get('category', 'Unknown')
    total_questions = len(answers)
    
    # Analyze answers
    correct_answers = sum(1 for ans in answers if ans.get('isCorrect', False))
    incorrect_answers = total_questions - correct_answers
    
    # Calculate average time per question
    avg_time = round(total_time / total_questions, 2) if total_questions > 0 else 0
    
    # Analyze difficulty performance
    difficulty_stats = {}
    all_questions = test.get('allQuestions', [])
    
    for answer in answers:
        q_id = answer.get('questionId')
        difficulty = 'unknown'
        
        # Try to find difficulty from allQuestions
        for q in all_questions:
            if q.get('_id') == q_id:
                difficulty = q.get('difficulty', 'unknown')
                break
        
        # If not found in allQuestions, check if question is embedded in answer
        if difficulty == 'unknown' and 'question' in answer:
            difficulty = answer['question'].get('difficulty', 'unknown')
        
        is_correct = answer.get('isCorrect', False)
        
        if difficulty not in difficulty_stats:
            difficulty_stats[difficulty] = {'correct': 0, 'total': 0}
        
        difficulty_stats[difficulty]['total'] += 1
        if is_correct:
            difficulty_stats[difficulty]['correct'] += 1
    
    # Format the data for the prompt
    formatted_data = {
        'test_id': test_id,
        'user_name': f"{user.get('firstName', '')} {user.get('lastName', '')}".strip(),
        'category': category,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'score': score,
        'total_time_seconds': total_time,
        'average_time_per_question': avg_time,
        'difficulty_breakdown': difficulty_stats,
        'performance_percentage': round((correct_answers / total_questions * 100), 2) if total_questions > 0 else 0
    }
    
    print(f"Formatted data: {formatted_data}")
    return formatted_data



# def format_psychometric_data(api_data: dict) -> dict:
#     attempt = api_data["data"]["attempt"]
    
#     # Extract basic info
#     test = attempt["test"]
#     answers = attempt["answers"]
    
#     # Calculate metrics
#     total_questions = len(answers)
#     correct_answers = sum(1 for ans in answers if ans["isCorrect"])
#     accuracy_pct = round((correct_answers / total_questions * 100), 1) if total_questions > 0 else 0
#     avg_time = round(attempt["totalTime"] / total_questions, 1) if total_questions > 0 else 0
    
#     # Difficulty breakdown
#     difficulty_count = {"easy": 0, "medium": 0, "hard": 0}
#     for ans in answers:
#         q_id = ans["questionId"]
#         # Find matching question in allQuestions
#         for q in test["allQuestions"]:
#             if q["_id"] == q_id:
#                 difficulty = q.get("difficulty", "easy")
#                 difficulty_count[difficulty] += 1
#                 break
    
#     # Build text
#     text = (
#         f"Test {test['category']}\n"
#         f"Score {attempt['score']}/{total_questions} "
#         f"({accuracy_pct}%)\n"
#         f"Time {avg_time}s avg\n"
#         f"Diff E{difficulty_count['easy']} "
#         f"M{difficulty_count['medium']} "
#         f"H{difficulty_count.get('hard', 0)}"
#     )

#     return {
#         "session_id": attempt["_id"],
#         "text": text
#     }


