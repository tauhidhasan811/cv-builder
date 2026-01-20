import re
import ast

def CleanData(text):
    # Step 1: Remove all literal backslashes
    cleaned = text.replace("\\", "")

    # Step 2: Remove backticks (` or ``` )
    cleaned = re.sub(r"`{1,3}", "", cleaned)

    # Step 3: Remove code language keywords (json, bash, python, etc.)
    cleaned = re.sub(r'\b(json|bash|python)\b', '', cleaned, flags=re.IGNORECASE)

    # Step 4: Remove newlines and extra spaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    print(cleaned)
    cleaned = ast.literal_eval(cleaned)
    return cleaned