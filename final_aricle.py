from article_rewrite import rewrite_article
from check_ai import is_article_valid
import re


def get_article(text):
    article = rewrite_article(True, text)
    article2 = rewrite_article(True, text)
    if is_article_valid(article) and is_article_valid(article)['isHuman']:
        return re.sub(r'"', '', article)
    elif is_article_valid(article2) and is_article_valid(article2)['isHuman']:
        return re.sub(r'"', '', article2)
    else:
        print("Niter of the articles are valid...")
        return False
