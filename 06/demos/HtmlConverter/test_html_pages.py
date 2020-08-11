import io

from html_pages import HtmlPagesConverter

#Fakes have the same characteristics as stubs in that they are copys of the object, but they are different that have realistic implementations inside and are suitable for production cases. In this example, a file was repalced with a stirngIO file, but can also have faked databases or web servers.

def test_convert_quotes():
    fake_file = io.StringIO("quote: ' ")
    converter = HtmlPagesConverter(open_file=fake_file)
    converted_text = converter.get_html_page(0)
    assert converted_text == "quote: &#x27;<br />"
    #checks that a converter will escape quotes correctly, these are what will be passed to the file. We then call the method we want to test checking that its converted to HTML. We then take the actual value as the assertion value to test the use of this converter.

def test_access_second_page():
    fake_file = io.StringIO("""\
page one
PAGE_BREAK
page two
PAGE_BREAK
page three
""")
    converter = HtmlPagesConverter(open_file=fake_file)
    converted_text = converter.get_html_page(1)
    assert converted_text == "page two<br />"
    #This test is to check that we are able to access the second page, convering the text and then reading the page breaks to allow access to the second text. This will pull up the second page, page(1)