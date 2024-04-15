from collections import defaultdict
from typing import Dict, List, Tuple

from rapidfuzz.distance.DamerauLevenshtein import normalized_similarity


def get_hashtag_accounts(posts: List[Dict], hashtag: str) -> List[str]:
    """
    From a set of posts, returns the IDs of all accounts that posted a
    particular hashtag (excluding reposts)

    Parameters
    ----------
    posts:
        A list of dictionary records, where each record corresponds to one post.
        Keys are metadata fields for a post, and values are the metadata itself
    hashtag:
        The hashtag by which to filter

    Returns
    -------
    accounts:
        The IDs of all accounts that posted the `hashtag` (excluding reposts)
    """
    hashtag_users = defaultdict(list)
    for post in posts:
        if not post["is_repost"]:
            post_hashtags = post["hashtags"]
            if post_hashtags:
                for post_hashtag in post_hashtags:
                    hashtag_users[post_hashtag].append(post["author_id"])
    return hashtag_users.get(hashtag, [])


def get_similar_screen_names(
    accounts: List[Dict], min_similarity: float
) -> List[Tuple[str, str, float]]:
    """
    From a set of accounts, returns pairs of accounts that have similar screen
    names according to the normalized Damerau-Levenshtein similarity

    Parameters
    ----------
    accounts:
        A list of account records, where each record corresponds to one account.
        Keys are metadata fields for an account, and values are the metadata
        itself
    min_similarity:
        A value between 0 and 1, indicating the minimum similarity needed to
        determine two accounts have similar screen names

    Returns
    -------
    similar_account_pairs:
        A list of tuples of the format (account_id1, account_id2) indicating
        which accounts have similar screen names
    """
    results = []
    # Intentionally runs in O(n^2)! We actually do want to compare every
    # item to every other item
    for i, a1 in enumerate(accounts):
        for j, a2 in enumerate(accounts):
            # Do not compare accounts to ones we've seen already
            if j > i:
                score = normalized_similarity(a1["screen_name"], a2["screen_name"])
                if score >= min_similarity:
                    results.append((a1["screen_name"], a2["screen_name"], score))
    return results
