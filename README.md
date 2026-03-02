# cv-builder

![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white) ![License](https://img.shields.io/badge/license-LICENSE-green)

## Description

cv-builder is a streamlined Python-based application designed to simplify the process of creating professional resumes. By automating the layout and formatting of career data, this tool allows users to generate polished, high-quality CVs with ease. Whether you are looking to maintain a consistent professional identity or need a scriptable way to update your credentials, cv-builder provides a robust foundation for building structured and visually appealing documents tailored for the modern job market.

## Tech Stack

- Python

## Key Dependencies

```
bs4
dotenv
openai
moviepy
pymupdf 
python-docx
langchain
pymongo[srv]
langchain-openai
fastapi[standard]
langchain-google-genai
google-generativeai
uvicorn
```

## Project Structure

```
.
├── LICENSE
├── check.py
├── component
│   ├── __init__.py
│   ├── config
│   │   ├── audio_model.py
│   │   ├── db_config.py
│   │   ├── gemini_model.py
│   │   ├── hug_model.py
│   │   └── openai_model.py
│   ├── core
│   │   ├── check_valid_json.py
│   │   ├── clear_data.py
│   │   ├── job_scrape.py
│   │   ├── speech_text.py
│   │   └── video_to_audio.py
│   ├── parameters.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── case_law_summary.py
│   │   ├── db_service.py
│   │   ├── file_reader.py
│   │   ├── get_psycho_data.py
│   │   ├── in_tray_email.py
│   │   ├── prompt_coverletter.py
│   │   ├── prompt_cv_maker.py
│   │   ├── prompt_mock_test.py
│   │   ├── prompt_recom_jobpost.py
│   │   ├── psycho_prompt.py
│   │   ├── ques_generations.py
│   │   ├── wrapper.py
│   │   ├── written_presentation.py
│   │   └── written_test.py
│   └── src
│       ├── __init__.py
│       ├── app.py
│       ├── data
│       │   ├── __init__.py
│       │   └── data.py
│       └── openai_generator.py
├── main(backup).py
├── main.py
├── model
│   └── insert.py
├── requirements.txt
└── test.py
```

## Development Setup

### Python Setup

1. Install Python (v3.10+ recommended)
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## How to Run

1. Clone the Repository
```bash
git clone https://github.com/tauhidhasan811/cv-builder.git
cd cv-builder

```
2. Make sure you are in the base directory of the project (where `main.py` is located).

3. Activate your virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

   ```

6. The application will be accessible at:
   ```
   http://127.0.0.1:8000
   
   ```

7. For interactive API documentation, visit:
   ```
   http://127.0.0.1:8000/docs
   
   ```

## License

This project is licensed under the Apache-2.0 License.

---
