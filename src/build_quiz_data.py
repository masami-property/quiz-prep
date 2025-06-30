import json
import re

def parse_quiz_data(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by '---' blocks and capture quiz ID
    quiz_blocks = re.split(r'---\nNo: (.*?)\n---', content)[1:]

    quizzes = []
    for i in range(0, len(quiz_blocks), 2):
        quiz_id = quiz_blocks[i].strip()
        block_content = quiz_blocks[i+1].strip()

        # Parse question (Q.) - can be multiple lines
        question_match = re.search(r'Q\.\s*(.*?)(?=\n\d+\.\s|\nA\.\s|\nSX\.\s|\nEX\.\s|\nImage:\s|$)', block_content, re.DOTALL)
        question = question_match.group(1).strip() if question_match else ""

        # Parse options (numbered items)
        options = []
        option_matches = re.findall(r'(\d+)\.\s+(.*?)(?=\n\d+\.\s|\nA\.\s|\nSX\.\s|\nEX\.\s|\nImage:\s|$)', block_content, re.DOTALL)
        for key, text in option_matches:
            options.append({"key": key.strip(), "text": text.strip()})

        # Parse answer (A.)
        answer_match = re.search(r'A\.\s+(.*?)(?=\nSX\.\s|\nEX\.\s|\nImage:\s|$)', block_content, re.DOTALL)
        answer_keys = []
        if answer_match:
            raw_answers = answer_match.group(1).strip()
            # Split by semicolon and extract numeric parts
            answers = [key.strip() for key in raw_answers.split(';') if key.strip()]
            answer_keys = [re.match(r'\d+', ans).group() for ans in answers if re.match(r'\d+', ans)]

        # Parse image (Image:) - can appear anywhere after A.
        image_match = re.search(r'Image:\s+(.*?)(?=\nSX\.\s|\nEX\.\s|$)', block_content, re.DOTALL)
        image = ""
        if image_match:
            image = image_match.group(1).strip()
            # Replace .png with .webp if present, otherwise append .webp
            image = re.sub(r'\.png$', '.webp', image, flags=re.IGNORECASE)
            if not image.endswith('.webp'):
                image += '.webp'

        # Parse short explanation (SX.) - only content after SX.
        short_explanation_match = re.search(r'SX\.\s*(.*?)(?=\nEX\.\s|$)', block_content, re.DOTALL)
        short_explanation = short_explanation_match.group(1).strip() if short_explanation_match else ""

        # Parse explanation (EX.)
        explanation_match = re.search(r'EX\.\s*(.*?)(?=\n---\nNo:|$)', block_content, re.DOTALL)
        explanation = explanation_match.group(1).strip() if explanation_match else ""

        # Remove "解説: " prefix from explanation if it exists
        if explanation.startswith("解説: "):
            explanation = explanation[len("解説: "):].strip()

        # Build quiz data
        quiz_data = {
            "question": question,
            "options": options,
            "answer_keys": answer_keys,
            "id": quiz_id,
            "image": image,
            "explanation": explanation
        }
        
        # Add short_explanation only if it exists
        if short_explanation:
            quiz_data["short_explanation"] = short_explanation

        quizzes.append(quiz_data)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(quizzes, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_file = 'src/quiz_data_source.txt'
    output_file = 'data/quiz_data.json'
    parse_quiz_data(input_file, output_file)