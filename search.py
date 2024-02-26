import re

def search(ads, query):
    results = []
    for name in ads:
        if re.search(query, name, re.IGNORECASE):
            results.append(name)
    return results

async def process_ads(message):
    ad_names = ["Ad1", "Ad2", "Ad3", "AnotherAd"]
    query = "Ad"
    results = search(ad_names, query)

    await message.answer(f"Ads with the query '{query}' found: {results}")
