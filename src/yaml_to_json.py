import yaml
import json
import os
import shutil

def create_output_directories():
    """出力ディレクトリを作成"""
    # このスクリプトがあるディレクトリの親ディレクトリを基準にする
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    quizzes_dir = os.path.join(base_dir, 'data', 'quizzes')
    
    # 既存のquizzesディレクトリがあれば削除して再作成
    if os.path.exists(quizzes_dir):
        shutil.rmtree(quizzes_dir)
    os.makedirs(quizzes_dir, exist_ok=True)
    
    return quizzes_dir

def convert_question_format(question):
    """問題データを指定の軽量化フォーマットに変換"""
    options_dict = question.get("options", {})
    # オプションのキーをアルファベット順にソートして順序を固定
    option_keys = sorted(options_dict.keys())
    
    # "o" (options) のフォーマット変換: [["text", "explanation"], ...]
    formatted_options = []
    for key in option_keys:
        option_info = options_dict.get(key, {})
        formatted_options.append([
            option_info.get("text", ""),
            option_info.get("explanation", "")
        ])
        
    # "a" (answer) のフォーマット変換: ["C", "D"] -> [2, 3]
    answer_keys = question.get("answer", [])
    # キーの文字 ("A", "B"...) を 0 から始まるインデックスに変換
    formatted_answer = [option_keys.index(ans) for ans in answer_keys if ans in option_keys]

    result = {
        "n": question.get("number", ""),
        "q": question.get("question", "").strip(),
        "o": formatted_options,
        "a": formatted_answer,
        "e": question.get("full_explanation", "").strip()
    }
    image_path = question.get("image", None)
    if image_path:
        result["i"] = image_path
    return result

def generate_index_file(quizzes_dir, total_questions):
    """インデックスファイルを生成"""
    index_data = {
        "version": "2.0",
        "total_questions": total_questions,
        "file_format": {
            "n": "問題番号 (string)",
            "q": "問題文 (string)",
            "o": "選択肢の配列 [[text, explanation], ...]",
            "a": "正解のインデックス配列 (number[])",
            "e": "総合解説 (string)",
            "i": "画像パス (string, オプション)"
        },
        "question_files": [f"q{i+1:03d}.json" for i in range(total_questions)]
    }
    
    index_path = os.path.join(quizzes_dir, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    return index_path

def main():
    # このスクリプトがあるディレクトリを基準にパスを解決
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_yaml_path = os.path.join(script_dir, 'quiz_data_source.yaml')
    
    try:
        # 出力ディレクトリの作成
        quizzes_dir = create_output_directories()
        print(f"出力ディレクトリを作成: {quizzes_dir}")
        
        # YAMLファイルの読み込み
        with open(input_yaml_path, 'r', encoding='utf-8') as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
        
        if not isinstance(yaml_data, list):
            raise ValueError("YAMLデータはリスト形式である必要があります")
        
        questions_count = len(yaml_data)
        print(f"問題数: {questions_count}")
        
        # 各問題を個別ファイルに出力
        for i, question in enumerate(yaml_data):
            converted_question = convert_question_format(question)
            
            filename = f"q{i+1:03d}.json"
            filepath = os.path.join(quizzes_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as json_file:
                json.dump([converted_question], json_file, ensure_ascii=False, indent=2)
            
            if (i + 1) % 10 == 0 or i == questions_count - 1:
                print(f"進行状況: {i+1}/{questions_count} 問題を処理完了")
        
        # インデックスファイルの生成
        index_path = generate_index_file(quizzes_dir, questions_count)
        print(f"インデックスファイルを作成: {index_path}")
        
        print(f"\n✅ 変換完了!")
        print(f"📁 分割ファイル: {questions_count}個のJSONファイル -> {quizzes_dir}")
        print(f"📋 インデックス: {index_path}")

    except FileNotFoundError:
        print(f"❌ エラー: ファイルが見つかりません。'{input_yaml_path}' を確認してください。")
    except yaml.YAMLError as e:
        print(f"❌ YAMLパースエラー: {e}")
    except Exception as e:
        print(f"❌ 予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    main()