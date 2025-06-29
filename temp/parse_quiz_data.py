import json
import re

def parse_quiz_data(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    quiz_blocks = re.split(r'---\nNo: (.*?)\n---', content)[1:] # Split by '---' and capture ID

    quizzes = []
    for i in range(0, len(quiz_blocks), 2):
        quiz_id = quiz_blocks[i].strip()
        block_content = quiz_blocks[i+1].strip()

        question_match = re.search(r'Q\. (.*?)(?=\n\d+\. |\nA\. |\nEX\. )', block_content, re.DOTALL)
        question = question_match.group(1).strip() if question_match else ""

        options = []
        option_matches = re.findall(r'(\d+)\. (.*?)(?=\n\d+\. |\nA\. |\nImage: |$)', block_content, re.DOTALL)
        for key, text in option_matches:
            options.append({"key": key.strip(), "text": text.strip()})

        answer_match = re.search(r'A\. (.*?)(?=\nEX\. |\nImage: |$)', block_content, re.DOTALL)
        answer_keys = []
        if answer_match:
            # Split by semicolon and strip whitespace, then extract digits
            raw_answers = answer_match.group(1)
            answers = [key.strip() for key in raw_answers.split(';') if key.strip()]
            # Extract only the numeric part from each answer
            answer_keys = [re.match(r'\d+', ans).group() for ans in answers if re.match(r'\d+', ans)]


        image_match = re.search(r'Image: (.*)', block_content)
        image = image_match.group(1).strip() if image_match else ""
        if image:
            # Replace .png with .webp if present, otherwise just append .webp
            image = re.sub(r'\.png$', '.webp', image, flags=re.IGNORECASE)
            if not image.endswith('.webp'): # Ensure it ends with .webp
                image += '.webp'

        explanation_match = re.search(r'EX.\s*(.*?)(?=\n---\nNo: |$)', block_content, re.DOTALL)
        explanation = explanation_match.group(1).strip() if explanation_match else ""

        quizzes.append({
            "question": question,
            "options": options,
            "answer_keys": answer_keys,
            "id": quiz_id,
            "image": image,
            "explanation": explanation
        })

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_file = 'temp/quiz_data_temp.txt'
    output_file = 'data/quiz_data.json'
    parse_quiz_data(input_file, output_file)
