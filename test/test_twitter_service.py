from app.services.twitter_service import search_twitter

def test_search_twitter():
    result = search_twitter("cybersecurity")
    assert result == "Searching Twitter for keyword: cybersecurity"
