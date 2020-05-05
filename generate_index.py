# coding: utf-8
from horoscope import generate_prophecies, times, generate_listing, advices, promises
from datetime import datetime as dt

def generate_page(head, body):
	page = f"""<html>
	{head}
	{body}
	</html>"""
	return page

def generate_head(title):
	head = f"""<title>
	{title}
	</title>"""
	return f"""<head>
	{head}
	</head>"""

def generate_body(header, paragraphs):
	body = f"""<h1>
	{header}
	</h1>"""
	for p in paragraphs:
		body = body + f"""<p>
		{p}
		</p>"""
	return f"""<body>
	{body}
	</body>
	<footer>
	<hr>
	<p><a href="about.html">О реализации</a></p>
	</footer>"""
	
def save_page(title, header, paragraphs, output="index.html"):
	fp= open(output, "w")
	today = dt.now().date()
	page = generate_page(
		head = generate_head(title),
		body = generate_body(header = header, paragraphs=paragraphs))
	print(page, file=fp)
	fp.close()

def generate_list(header, listing):
	list1 = ""

	for p in listing:
		list1 = list1 + f"<li>{p}</li>"
	list2 = ""
	for a in advices:
		list2 = list2 + f"<li>{a}</li>"
	list3 = ""
	for r in promises:
		list3 = list3 + f"<li>{r}</li>"
	return f"""<body>
	<h1>{header}</h1>
	<ol>
	<li> Времена </li>
		<ul> {list1}</ul>
	<li> Глаголы </li>
	<ul> {list2}</ul>
	<li> Обещания </li>
	<ul> {list3}</ul>
	</ol>
</body>
<footer>
<hr>
<p><a href="index.html">Гороскоп</a></p>
</footer>
</html>
"""

def save_about(title, header, listing, output="about.html"):
	fp= open(output, "w")
	today = dt.now().date()
	page = generate_page(
		head = generate_head(title),
		body = generate_list(header = header, listing=listing))
	print(page, file=fp)
	fp.close()

today = dt.now().date()
save_page(
	title = "Гороскоп на сегодня",
	header = f"Ваши предасказания на {today}:",
	paragraphs = generate_prophecies()
)

save_about(
	title = "О чём это",
	header = "О чём это",
	listing = generate_listing()
	)



