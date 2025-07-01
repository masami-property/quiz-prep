import yaml
import json
import os

# Define input and output file paths
input_yaml_path = os.path.join(os.path.dirname(__file__), 'quiz_data_source.yaml')
output_json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'quiz_data.json')

try:
    # Read YAML file
    with open(input_yaml_path, 'r', encoding='utf-8') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    # Write JSON file
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(yaml_data, json_file, ensure_ascii=False, indent=2)

    print(f"変換成功: {input_yaml_path} → {output_json_path}")

except FileNotFoundError:
    print(f"エラー: ファイルが見つかりません。'{input_yaml_path}' または '{output_json_path}' を確認してください。")
except yaml.YAMLError as e:
    print(f"YAMLパースエラー: {e}")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
