from model import get_hashtag_accounts, get_similar_screen_names


def test_get_hashtag_accounts():
    posts = [
        {"is_repost": False, "hashtags": ["#blessed"], "author_id": "1"},
        {"is_repost": False, "hashtags": ["#blessed"], "author_id": "2"},
        {"is_repost": False, "hashtags": None, "author_id": "3"},
        {"is_repost": True, "hashtags": ["#blessed"], "author_id": "4"},
    ]
    accounts = get_hashtag_accounts(posts, "#blessed")
    assert accounts == ["1", "2"]

def test_hashtag_search_works():
    posts = [
        {"is_repost": False, "hashtags": ["#blessed"], "author_id": "1"},
        {"is_repost": False, "hashtags": ["#blessed"], "author_id": "2"},
        {"is_repost": False, "hashtags": None, "author_id": "3"},
        {"is_repost": True, "hashtags": ["#blessed"], "author_id": "4"},
    ]
    accounts = get_hashtag_accounts(posts, "#covid")
    assert len(accounts) == 0


def test_similar_screen_names():
    accounts = [{"screen_name": "asdf"}, {"screen_name": "asdf"}]
    similar = get_similar_screen_names(accounts, min_similarity=0.5)
    assert len(similar) == 1


def test_dissimilar_screen_names():
    accounts = [{"screen_name": "barack obama"}, {"screen_name": "1001"}]
    similar = get_similar_screen_names(accounts, min_similarity=0.99)
    assert len(similar) == 0
