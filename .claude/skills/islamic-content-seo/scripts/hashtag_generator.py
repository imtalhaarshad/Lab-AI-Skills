#!/usr/bin/env python3
"""
Islamic Content Hashtag Generator
This script generates platform-specific hashtags for Islamic content.
"""

import random
from typing import List, Dict

def get_islamic_hashtags_by_category() -> Dict[str, List[str]]:
    """
    Get Islamic hashtags organized by category.
    """
    return {
        "general": [
            "#Islam", "#Muslim", "#Islamic", "#Quran", "#ProphetMuhammad",
            "#Allah", "#SubhanahuWaTaala", "#SWT", "#Bismillah", "#Alhamdulillah",
            "#MashaAllah", "#InshaAllah", "#Barakah", "#JazakAllahKhair"
        ],
        "worship": [
            "#Salah", "#Prayer", "#Namaz", "#Wudu", "#Fasting", "#Ramadan",
            "#Hajj", "#Umrah", "#Zakat", "#Charity", "#Dhikr", "#Meditation",
            "#Spirituality", "#Worship", "#Devotion", "#Faith"
        ],
        "values": [
            "#Mercy", "#Compassion", "#Justice", "#Forgiveness", "#Patience",
            "#Gratitude", "#Peace", "#Kindness", "#Truth", "#Integrity",
            "#Humility", "#Courage", "#Wisdom", "#Love"
        ],
        "knowledge": [
            "#IslamicKnowledge", "#Tafsir", "#Hadith", "#Sunnah", "#Fiqh",
            "#Aqeedah", "#IslamicStudies", "#Scholarship", "#Learning",
            "#Education", "#Teaching", "#Understanding", "#Wisdom"
        ],
        "community": [
            "#MuslimCommunity", "#Brotherhood", "#Sisterhood", "#Ummah",
            "#Unity", "#Support", "#Together", "#Family", "#Parenting",
            "#Marriage", "#Children", "#Elders", "#Respect"
        ],
        "lifestyle": [
            "#Halal", "#IslamicLifestyle", "#MuslimLife", "#IslamicFinance",
            "#IslamicBanking", "#HalalFood", "#ModestFashion", "#Hijab",
            "#IslamicArt", "#IslamicCulture", "#Tradition", "#Heritage"
        ],
        "contemplation": [
            "#Reflection", "#Contemplate", "#Mindful", "#Purpose", "#Meaning",
            "#Life", "#Death", "#Afterlife", "#Akhirah", "#Dunya", "#Balance"
        ]
    }

def get_platform_specific_guidelines() -> Dict[str, Dict]:
    """
    Get platform-specific hashtag guidelines for Islamic content.
    """
    return {
        "Instagram": {
            "max_hashtags": 30,
            "style": "Mix of popular and niche hashtags, include location if relevant",
            "tips": [
                "Use a mix of general Islamic hashtags and specific topic hashtags",
                "Consider adding 2-3 popular non-Islamic hashtags for broader reach",
                "Use Islamic art or calligraphy related hashtags if sharing visual content"
            ]
        },
        "Twitter": {
            "max_hashtags": 2,
            "style": "Fewer, highly relevant hashtags",
            "tips": [
                "Use only the most relevant hashtags",
                "Consider trending Islamic hashtags if appropriate",
                "Avoid hashtag stuffing"
            ]
        },
        "Facebook": {
            "max_hashtags": 5,
            "style": "Moderate use of relevant hashtags",
            "tips": [
                "Focus on 3-5 highly relevant hashtags",
                "Include community-specific hashtags if applicable"
            ]
        },
        "LinkedIn": {
            "max_hashtags": 5,
            "style": "Professional Islamic content hashtags",
            "tips": [
                "Use professional Islamic content hashtags",
                "Include industry-specific Islamic hashtags if applicable"
            ]
        },
        "TikTok": {
            "max_hashtags": 10,
            "style": "Mix of trending and Islamic hashtags",
            "tips": [
                "Include trending hashtags if relevant to Islamic content",
                "Use creative and engaging Islamic hashtags",
                "Combine Islamic hashtags with entertainment hashtags for reach"
            ]
        },
        "YouTube": {
            "max_hashtags": 15,
            "style": "Topic-focused hashtags",
            "tips": [
                "Use hashtags that describe your video content specifically",
                "Include series or channel-specific hashtags",
                "Mix general Islamic hashtags with specific topic hashtags"
            ]
        }
    }

def generate_hashtags_for_topic(topic: str, platform: str = "Instagram", count: int = 10) -> List[str]:
    """
    Generate platform-specific hashtags for a given Islamic topic.
    """
    all_hashtags = get_islamic_hashtags_by_category()
    platform_guidelines = get_platform_specific_guidelines()

    # Determine max hashtags based on platform
    max_count = platform_guidelines.get(platform, {}).get("max_hashtags", 5)
    count = min(count, max_count)

    selected_hashtags = []

    # Add topic-relevant hashtags
    topic_lower = topic.lower()

    for category, hashtags in all_hashtags.items():
        if topic_lower in category:
            selected_hashtags.extend(hashtags[:count])
            break

    # If no direct match, add some general and worship-related hashtags
    if not selected_hashtags:
        selected_hashtags.extend(all_hashtags["general"][:3])
        selected_hashtags.extend(all_hashtags["worship"][:3])

        # Add topic-related hashtags if possible
        if "pray" in topic_lower or "salah" in topic_lower:
            selected_hashtags.extend(all_hashtags["worship"])
        elif "learn" in topic_lower or "study" in topic_lower:
            selected_hashtags.extend(all_hashtags["knowledge"])
        elif "family" in topic_lower or "marriage" in topic_lower:
            selected_hashtags.extend(all_hashtags["community"])
        elif "fast" in topic_lower or "ramadan" in topic_lower:
            selected_hashtags.extend(all_hashtags["worship"])

    # Add variety if we don't have enough
    while len(selected_hashtags) < count and len(selected_hashtags) < len([item for sublist in all_hashtags.values() for item in sublist]):
        for category, hashtags in all_hashtags.items():
            if len(selected_hashtags) >= count:
                break
            for hashtag in hashtags:
                if hashtag not in selected_hashtags:
                    selected_hashtags.append(hashtag)
                    if len(selected_hashtags) >= count:
                        break

    # Randomly select the requested number
    if len(selected_hashtags) > count:
        selected_hashtags = random.sample(selected_hashtags, count)

    return selected_hashtags

def suggest_hashtag_strategy(content_type: str, platform: str, topic: str) -> Dict:
    """
    Provide a complete hashtag strategy for specific content.
    """
    platform_guidelines = get_platform_specific_guidelines()

    platform_info = platform_guidelines.get(platform, {})
    suggested_hashtags = generate_hashtags_for_topic(topic, platform,
                                                   platform_info.get("max_hashtags", 5))

    return {
        "platform": platform,
        "content_type": content_type,
        "topic": topic,
        "suggested_hashtags": suggested_hashtags,
        "guidelines": platform_info.get("style", ""),
        "tips": platform_info.get("tips", [])
    }

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python hashtag_generator.py <platform> <topic> [content_type]")
        print("Example: python hashtag_generator.py Instagram 'daily prayer'")
        print("Platforms supported: Instagram, Twitter, Facebook, LinkedIn, TikTok, YouTube")
        sys.exit(1)

    platform = sys.argv[1]
    topic = " ".join(sys.argv[2:]) if len(sys.argv) > 3 else sys.argv[2]
    content_type = sys.argv[3] if len(sys.argv) > 3 else "General Islamic Content"

    strategy = suggest_hashtag_strategy(content_type, platform, topic)

    print(f"Islamic Content Hashtag Strategy for {strategy['platform']}")
    print("=" * 60)
    print(f"Content Type: {strategy['content_type']}")
    print(f"Topic: {strategy['topic']}")
    print(f"Guidelines: {strategy['guidelines']}")
    print()
    print("Suggested Hashtags:")
    for i, hashtag in enumerate(strategy['suggested_hashtags'], 1):
        print(f"{i:2d}. {hashtag}")
    print()
    print("Tips:")
    for tip in strategy['tips']:
        print(f"- {tip}")