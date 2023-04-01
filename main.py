import os
import openai
from final_aricle import get_article
import re
from time import sleep

openai.api_key = "YOUR_API_KEY"


# MAKE SURE TO CREATE 2 FOLDER  NAMED ./blogs AND  ./titles


def get_data_chatGPT(title):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=title,
        temperature=0.7,
        max_tokens=450,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]["text"]


# The Role of Java in Building a Career in Blockchain Development

articles = [
    'Building a Career in Blockchain: The Importance of Learning a Dynamic Programming Language',
    'The Role of Ruby in Building a Career in Blockchain Development',
    'Building a Career in Blockchain: The Programming Languages of Distributed Systems',
    'Blockchain Development: The Programming Languages of Cryptography',
    'Building a Career in Blockchain: The Importance of Learning a Transpiled Language',
    'Blockchain Development: The Role of WebAssembly and Web3.js',
    'Building a Career in Blockchain: The Programming Languages of Consensus Algorithms',
    'Blockchain Development: Understanding the Role of Bytecode languages',
    'Building a Career in Blockchain: The Importance of Learning a Markup Language',
    'The Role of Swift in Building a Career in Blockchain Development'
]


def get_points(tmp):
    lst = tmp.split('\n\n')
    if len(lst[0]) == 0:
        return len(lst) - 1
    else:
        return len(lst)

# FUNCTION TO GET THE RELEVANT TAG FOR YOU POST
def get_tags(article):
    txt = "Provide me with SEO friendly post tags for the blog post on " + article
    r = get_data_chatGPT(txt)
    return r


tag = get_tags('The Role of Ruby in Building a Career in Blockchain Development')
tags = tag.split("#")


# print(tags)

def get_prompt(article):
    txt = "write an outline for an article about " + article
    res = get_data_chatGPT(txt)
    with open("./titles/" + article + " table", 'w') as f:
        f.write(res)
    lst = res.split('\n\n')
    count = get_points(res)
    post = ""
    clean_post = ""
    for i in range(count):
        tmp = "write a post about "
        heading = lst[i + 1].split("\n")[0]
        post += "<h1>" + heading + " </h1>" + "\n\n" + get_data_chatGPT(tmp + lst[i + 1]) + "\n\n"
        print(heading)
        # complete_post = get_article(post)
        #
        # clean_post += "\n" + "<h1>" + heading + " </h1>" + "\n\n" + complete_post + "\n"

    complete_post = get_article(post).replace("Presentation <", " Introduction <").replace("End <", "Conclusion <")
    clean_post = re.sub("\\\\", "", complete_post)
    with open("./blogs/" + article, 'w') as f:
        f.write(clean_post)


# art = "Crypto mining: A beginner's guide to mining different cryptocurrencies"
# # get_prompt(art)
# f = open("./blogs/Crypto mining: A beginner's guide to mining different cryptocurrencies")
# txt = f.read()
# txt = re.sub("\\\\","",txt)
# print(txt)


import os
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
import re


# CONNECTING TO THE WORDPRESS WEBSITE WITH USER CREDENTIALS
wp = Client('https://WORDPRESS_SITE_URL.COM/xmlrpc.php', 'USER_NAME', 'PASSWORD')
print("Wordpress logged in Success ")

for article in articles:
    print("Writing the article for :", article)
    get_prompt(article)

    with open("./blogs/" + article, 'r') as file:
        post_content = file.read()

    # Create a new WordPress post object
    post = WordPressPost()
    post.title = article
    post_content = re.sub(r"\\n", "\n", post_content)
    post.terms_names = {
        'post_tag': tags,
        'category': ['Blockchain']
    }
    post.content = post_content
    wp.call(NewPost(post))
    print("^^^^" * 23, "\n")
