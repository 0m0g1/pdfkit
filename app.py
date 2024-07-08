import pdfkit

# Path to the wkhtmltopdf executable
path_to_wkhtmltopdf = '/path/to/wkhtmltopdf'

# Configure pdfkit to use the executable
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Convert HTML file to PDF
pdfkit.from_file('example.html', 'output.pdf', configuration=config)

# Convert HTML string to PDF
html_string = '''
<html>
<head><title>Test</title></head>
<body><h1>Hello, world!</h1></body>
</html>
'''
pdfkit.from_string(html_string, 'output_from_string.pdf', configuration=config)

# Convert a URL to PDF
pdfkit.from_url('http://example.com', 'output_from_url.pdf', configuration=config)
