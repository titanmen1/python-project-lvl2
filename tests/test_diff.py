from gendiff import generate_diff


def test_gendiff_json():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    output = './tests/fixtures/output.json'
    assert generate_diff(file1, file2, 'json') == open(output, 'r').read()


def test_gendiff_input_yaml():
    file1 = './tests/fixtures/file1.yml'
    file2 = './tests/fixtures/file2.yml'
    output = './tests/fixtures/output.yml'
    assert generate_diff(file1, file2, 'json') == open(output, 'r').read()


def test_gendiff_output_format_plain():
    file1 = './tests/fixtures/file1.yml'
    file2 = './tests/fixtures/file2.yml'
    output = './tests/fixtures/test_plain'
    assert generate_diff(file1, file2, 'plain') == open(output, 'r').read()
