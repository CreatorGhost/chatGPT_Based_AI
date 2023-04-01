import os
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
import re

# Connect to your website using the API endpoint and your WordPress credentials
wp = Client('https://bitbybit.in/xmlrpc.php', 'adityapratap2307@gmail.com', 'B!tByB!t@12345')

print("loged in")
# Read the post from a text file
with open(
        '/Users/adi/Documents/Youtube/artiicle_by_ai/blogs/Blockchain in Government: Enhancing Security and Improving Transparency',
        'r') as file:
    post_content = file.read()

# Create a new WordPress post object
post = WordPressPost()
post.title = "Blockchain in Government: Enhancing Security and Improving Transparency"
post_content = re.sub(r"\\n", "\n", post_content)

#
post.content = post_content
# post.terms_names = {
#     'post_tag': ['python', 'wordpress'],
#     'category': ['Tech']
# }
#
# # Publish the post on your website
wp.call(NewPost(post))
#
# # print the post URL
# print(post.title)
