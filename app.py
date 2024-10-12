from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

arabic_to_yezidi = {
    'ا': '𐺀', 'أ': '𐺀', 'إ': '𐺀', 'ة': '𐺀', 'ى': '𐺀',
    'ب': '𐺁', 'پ': '𐺂', 'ت': '𐺄', 'ث': '𐺗',
    'ج': '𐺆', 'چ': '𐺇', 'ح': '𐺉', 'خ': '𐺊',
    'د': '𐺋', 'ذ': '𐺌', 'ر': '𐺍', 'ڕ': '𐺎',
    'ز': '𐺏', 'ژ': '𐺐', 'س': '𐺑', 'ش': '𐺒',
    'ص': '𐺓', 'ض': '𐺔', 'ط': '𐺕', 'ظ': '𐺖',
    'ع': '𐺗', 'غ': '𐺘', 'ف': '𐺙', 'ڤ': '𐺚', 'ڤ': '𐺛',
    'ق': '𐺜', 'ك': '𐺝', 'ك': '𐺞', 'گ': '𐺟', 'ل': '𐺠',
    'م': '𐺡', 'ن': '𐺢', 'و': '𐺣', 'و': '𐺤', 'ۆ': '𐺥', 'ؤ': '𐺥',
    'ه': '𐺧', 'ي': '𐺨', 'ێ': '𐺩', 'ئ': '𐺩'
}

yezidi_to_arabic = {
    '𐺀': 'ا', '𐺁': 'ب', '𐺂': 'پ', '𐺃': 'پ',
    '𐺄': 'ت', '𐺗': 'ع', '𐺆': 'ج', '𐺇': 'چ', '𐺈': 'چ',
    '𐺉': 'ح', '𐺊': 'خ', '𐺋': 'د', '𐺌': 'ذ',
    '𐺍': 'ر', '𐺎': 'ڕ', '𐺏': 'ز', '𐺐': 'ژ',
    '𐺑': 'س', '𐺒': 'ش', '𐺓': 'ص', '𐺔': 'ض',
    '𐺕': 'ط', '𐺖': 'ظ', '𐺘': 'غ', '𐺙': 'ف',
    '𐺚': 'ڤ', '𐺛': 'ڤ', '𐺜': 'ق', '𐺝': 'ك', '𐺞': 'ك',
    '𐺟': 'گ', '𐺠': 'ل', '𐺡': 'م', '𐺢': 'ن',
    '𐺣': 'و', '𐺤': 'و', '𐺥': 'ۆ', '𐺧': 'ه',
    '𐺨': 'ي', '𐺩': 'ێ'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.json
    input_text = data['text']
    direction = data['direction']
    output_text = ''

    if direction == 'toYezidi':
        output_text = ''.join([arabic_to_yezidi.get(char, char) for char in input_text])
    else:
        output_text = ''.join([yezidi_to_arabic.get(char, char) for char in input_text])

    return jsonify({'output': output_text})

if __name__ == '__main__':
    app.run(debug=True)
