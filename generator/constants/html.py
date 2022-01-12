HTML_BASE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    <header class="header">
        {h1}
        {header_paragraph}
    </header>

    <main class="main">
        <section class="">
            {h2}
            {section_paragraph}
        </section>
    </main>

    <footer class="footer">
        {a}
    </footer>

</body>
</html>
"""

H1 = "<h1>{}</h1>"
H2 = "<h2>{}</h2>"
P = "<p>{}</p>"
A = "<a>{}</a>"
