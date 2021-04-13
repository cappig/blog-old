#!/usr/bin/python3
import markdown, glob, os, yaml

#open the header and footer files
with open("src/assets/header.html", "r") as f:
    header = f.read()
with open("src/assets/footer.html", "r") as f:
    footer = f.read()
with open("src/assets/about_me.md", "r") as f:
    aboutme = f.read()

#get names of all posts in list 
posts = (glob.glob("src/posts/*.md"))
postn = os.listdir("src/posts/")

#generate individual html files for the articles
i = 0
for post in posts:
    with open(post, "r") as f:
        text = f.read()
        yamld, content = text[3:].split('---')
        y = yaml.safe_load(yamld)
        html = header + '\n<h1>' + y['title'] + '</h1>\n' + '<p class="text-muted text-left date">'+ y['date']+ '</p>\n'+ markdown.markdown(content) + '\n' + footer
        open("final/posts/"+postn[i][:-3]+".html", "w").write(html)
        i += 1

#make index page i.e parse yaml and list articles
feed = "\n"
j = 0
for post in posts:
    with open(post, "r") as f:
        text = f.read()
        yamld, content = text[3:].split('---')
        y = yaml.safe_load(yamld)
        #Add linked title
        feed += '<article>\n<a class="h3" href="posts/'+postn[j][:-3]+'.html">'+y['title']+'</a>' + "<br> \n"
        feed += '<p class="text-muted"><i>'+y['date']+ '</i>' +'   |   ' +y['description']+'</p><br>\n</article>\n'

#make about me page
am_html = '\n' + markdown.markdown(aboutme) + '\n'
open("final/about_me.html", "w").write(header+am_html+footer)

#pool it all together
final = (
    header +
    feed +
    footer
)

# and generate final index file
open("final/index.html", "w").write(final)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Generate RSS feed
# Code is based on https://github.com/vbuterin/blog/pull/10/files
import calendar, datetime

# Generate date from yaml
def getdate(datetext):
    monthday, year = datetext.split(', ')
    month, day = monthday.split(' ')
    date = datetime.datetime(int(year), list(calendar.month_abbr).index(month), int(day))
    return date.strftime('%a, %d %b %Y 00:00:00 +0000')

# Generate individual items for articles 
items = ""
k = 0
for post in posts:
    with open(post, "r") as f:
        text = f.read()
        yamld, content = text[3:].split('---')
        y = yaml.safe_load(yamld)

        items += """
    <item>
        <title>{title}</title>
        <link>{link}</link>
        <guid>{link}</guid>
        <description>{description}</description>
        <pubDate>{date}</pubDate>
    </item>\n""".format(
        title = y['title'],
        link = 'https://cappig.ga/posts/' + postn[k][:-3],
        description = y['description'],
        date = getdate(y['date']))

# Generate final RSS feed
rss = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>Matt's blog</title>
<link>https://cappig.ga/</link>
<description>Matt's personal blog</description>
    <image>
        <url>https://cappig.ga/assets/favicon.png</url>
        <title>Matt's blog</title>
        <link>https://cappig.ga/</link>
    </image>
{items}
</channel>
</rss>""".format(items = items)

# Write RSS feed to file
open("final/feed.xml", "w").write(rss)