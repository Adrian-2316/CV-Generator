import json
from pathlib import Path

import json
from pathlib import Path
from docxtpl import DocxTemplate


def generate_cv_from_json():
    template_path = Path('./resource/layout.docx')
    json_file_path = Path('./resource/cv_en_info.json')
    output_path = Path('./resource/output.docx')
    doc = DocxTemplate(template_path)
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    print(json_data)
    doc.render(json_data)
    doc.save(output_path)
    print(f"Report generated: {output_path}")


if __name__ == '__main__':
    generate_cv_from_json()
