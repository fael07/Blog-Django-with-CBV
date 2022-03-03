from .authors import create_cache_page_for_authors
from .post import create_cache_page_for_posts
from .list_subcategories import create_cache_page_for_list_subcategories
from .subcategories import create_cache_page_for_subcategories



def create_cache_pages(context):
    create_cache_page_for_subcategories(context)
    create_cache_page_for_list_subcategories(context)
    create_cache_page_for_posts(context)
    create_cache_page_for_authors(context)