from unittest.mock import patch, mock_open

from html_pages import HtmlPagesConverter


@patch("builtins.open", new_callable=mock_open,
       read_data="quote: ' ")
def test_convert_quotes(fake_file):
    with HtmlPagesConverter(filename="filename.txt") as converter:
        converted_text = converter.get_html_page(0)
        assert converted_text == "quote: &#x27;<br />"
# Here we use monkeypatching to change the contents of the file by using a decorator and make use of the mock open, part of the unittest.mock package which is a fake file. We will then pass the contents of that file as the test in the quote, which will be passed to the test case. Afterwards we assert that the returned test has the correct text, allowing us to replace built in functionality within a class.