#!/usr/bin/env python3
"""
Islamic Content Keyword Research Tool
This script helps research and generate relevant keywords for Islamic content SEO.
"""

import json
import re
from typing import List, Dict

def load_islamic_keywords() -> Dict[str, List[str]]:
    """
    Load a comprehensive list of Islamic keywords organized by categories.
    """
    return {
        "ibadah": [
            "salah", "prayer", "namaz", "wudu", "ablution", "fasting", "sawm",
            "ramadan", "hajj", "umrah", "zakat", "charity", "dhikr", "remembrance"
        ],
        "knowledge": [
            "tafsir", "interpretation", "hadith", "sunnah", "fiqh", "jurisprudence",
            "aqeedah", "creed", "islamic law", "sharia", "islamic studies",
            "islamic education"
        ],
        "values": [
            "mercy", "rahma", "justice", "adl", "compassion", "forbearance",
            "patience", "sabr", "gratitude", "shukr", "forgiveness", "tawakkul"
        ],
        "history": [
            "prophets", "anbiya", "companions", "sahaba", "caliphs", "khulafa",
            "islamic history", "seerah", "biography", "islamic civilization"
        ],
        "contemporary": [
            "muslim life", "islamic lifestyle", "halal", "islamic finance",
            "islamic banking", "muslim family", "islamic parenting"
        ]
    }

def generate_keyword_variants(keyword: str) -> List[str]:
    """
    Generate different variants of an Islamic keyword for SEO purposes.
    """
    variants = []

    # Add the original keyword
    variants.append(keyword.lower())

    # Add plural forms if applicable
    if not keyword.endswith('s'):
        variants.append(keyword.lower() + 's')

    # Add hyphenated forms
    if ' ' in keyword:
        variants.append(keyword.replace(' ', '-').lower())
        variants.append(keyword.replace(' ', '_').lower())

    # Add transliterated Arabic forms if applicable
    arabic_transliteracies = {
        "prayer": "salah",
        "fasting": "sawm",
        "charity": "zakat",
        "pilgrimage": "hajj",
        "faith": "iman",
        "islam": "al-islam",
        "god": "allah",
        "prophet": "rasul",
        "holy book": "quran",
        "mosque": "masjid",
        "islamic law": "sharia",
        "islamic jurisprudence": "fiqh",
        "islamic creed": "aqeedah",
        "islamic interpretation": "tafsir",
        "islamic tradition": "hadith"
    }

    if keyword.lower() in arabic_transliteracies:
        variants.append(arabic_transliteracies[keyword.lower()])
        if not arabic_transliteracies[keyword.lower()].endswith('s'):
            variants.append(arabic_transliteracies[keyword.lower()] + 's')

    return list(set(variants))

def research_keywords(topics: List[str], max_results: int = 20) -> List[str]:
    """
    Research and return relevant Islamic keywords based on provided topics.
    """
    all_keywords = []
    keyword_categories = load_islamic_keywords()

    # Find keywords matching the provided topics
    for topic in topics:
        topic_lower = topic.lower()
        for category, keywords in keyword_categories.items():
            for keyword in keywords:
                if topic_lower in keyword or keyword in topic_lower:
                    all_keywords.extend(generate_keyword_variants(keyword))

    # If no specific matches found, return general Islamic keywords
    if not all_keywords:
        for category, keywords in keyword_categories.items():
            for keyword in keywords[:3]:  # Take first 3 from each category
                all_keywords.extend(generate_keyword_variants(keyword))

    # Remove duplicates and return top results
    unique_keywords = list(set(all_keywords))
    return unique_keywords[:max_results]

def suggest_long_tail_keywords(primary_keywords: List[str]) -> List[str]:
    """
    Generate long-tail keywords based on primary Islamic keywords.
    """
    long_tail_keywords = []

    for kw in primary_keywords:
        # Add common prefixes and suffixes
        prefixes = ["how to", "what is", "meaning of", "benefits of", "importance of", "guide to"]
        suffixes = ["explained", "meaning", "benefits", "importance", "steps", "examples", "pdf", "free"]

        for prefix in prefixes:
            long_tail_keywords.append(f"{prefix} {kw}")

        for suffix in suffixes:
            long_tail_keywords.append(f"{kw} {suffix}")

        # Combine multiple keywords
        for other_kw in primary_keywords:
            if kw != other_kw:
                long_tail_keywords.append(f"{kw} and {other_kw}")
                long_tail_keywords.append(f"{kw} vs {other_kw}")

    return list(set(long_tail_keywords))[:50]

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python keyword_research.py <topic1> [topic2] ...")
        print("Example: python keyword_research.py prayer ramadan")
        sys.exit(1)

    topics = sys.argv[1:]
    print(f"Researching Islamic keywords for topics: {', '.join(topics)}")
    print("-" * 50)

    primary_keywords = research_keywords(topics)
    print("Primary Keywords:")
    for i, kw in enumerate(primary_keywords, 1):
        print(f"{i:2d}. {kw}")

    print("\nLong-tail Keywords:")
    long_tail = suggest_long_tail_keywords(primary_keywords)
    for i, kw in enumerate(long_tail[:15], 1):  # Show first 15
        print(f"{i:2d}. {kw}")