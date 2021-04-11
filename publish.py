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
am_html = markdown.markdown(aboutme)
open("final/about_me.html", "w").write(header+am_html+footer)

#pool it all together
final = (
    header +
    feed +
    footer
)

# and generate final index file
open("final/index.html", "w").write(final)
