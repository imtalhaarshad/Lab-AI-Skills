#!/usr/bin/env python3
"""
Islamic Content Optimizer
This script helps optimize Islamic content for SEO while maintaining authenticity and adherence to Islamic principles.
"""

import re
from typing import Dict, List, Tuple

def analyze_content(content: str) -> Dict:
    """
    Analyze the Islamic content for SEO elements.
    """
    analysis = {
        "word_count": len(content.split()),
        "sentence_count": len(re.split(r'[.!?]+', content)),
        "paragraph_count": len([p for p in content.split('\n\n') if p.strip()]),
        "keyword_density": {},
        "readability_score": 0,
        "islamic_keywords_found": [],
        "suggestions": []
    }

    # Basic readability approximation
    avg_sentence_length = analysis["word_count"] / max(analysis["sentence_count"], 1)
    analysis["readability_score"] = max(0, 100 - (avg_sentence_length * 2))

    return analysis

def optimize_title(title: str, primary_keywords: List[str]) -> str:
    """
    Optimize the title for Islamic content with primary keywords.
    """
    # Ensure Islamic values are maintained
    if not title.lower().startswith(('islamic', 'muslim', 'quranic', 'prophetic')):
        # Add relevant prefix if not already present
        if any(kw in title.lower() for kw in ['prayer', 'fasting', 'ramadan', 'hajj', 'zakat']):
            prefix = "Islamic "
        elif any(kw in title.lower() for kw in ['good', 'virtue', 'character', 'morality']):
            prefix = "Islamic "
        else:
            prefix = "Islamic "

        if not title.startswith(prefix):
            title = f"{prefix}{title}"

    # Ensure title length is appropriate (50-60 characters for SEO)
    if len(title) > 60:
        # Find a good breaking point
        words = title.split()
        optimized_title = ""
        for word in words:
            if len(optimized_title + word) <= 60:
                optimized_title += word + " "
            else:
                break
        title = optimized_title.strip() + "..."

    return title

def optimize_description(description: str, primary_keywords: List[str], max_length: int = 160) -> str:
    """
    Optimize the meta description for Islamic content.
    """
    # Add Islamic context if not present
    if not any(kw in description.lower() for kw in ['islam', 'muslim', 'quran', 'prophet', 'allah']):
        # Add appropriate Islamic context at the beginning
        if any(kw in description.lower() for kw in ['prayer', 'salah', 'namaz']):
            description = f"Islamic guidance on {description.lower()}"
        elif any(kw in description.lower() for kw in ['fast', 'ramadan', 'hajj', 'zakat']):
            description = f"Islamic practices: {description.lower()}"
        elif any(kw in description.lower() for kw in ['good', 'virtue', 'character']):
            description = f"Islamic values: {description.lower()}"
        else:
            description = f"Islamic perspective: {description.lower()}"

    # Ensure description is within SEO limits
    if len(description) > max_length:
        # Find a good breaking point
        sentences = re.split(r'[.!?]+', description)
        optimized_desc = ""
        for sentence in sentences:
            sentence = sentence.strip()
            if len(optimized_desc + sentence + ".") <= max_length - 3:
                optimized_desc += sentence + ". "
            else:
                break
        description = optimized_desc.strip() + "..."

    return description

def optimize_content_structure(content: str, primary_keywords: List[str]) -> str:
    """
    Optimize the structure of Islamic content for SEO.
    """
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    optimized_content = []

    for i, paragraph in enumerate(paragraphs):
        # Add primary keywords naturally in the first paragraph
        if i == 0:
            # The introduction should contain primary keywords
            words = paragraph.split()
            keyword_added = False
            for j, word in enumerate(words):
                if not keyword_added and any(kw.lower() in word.lower() for kw in primary_keywords):
                    # Keyword already exists, continue
                    keyword_added = True
                elif not keyword_added and j > 2:  # Add keyword after first few words
                    words.insert(j, f" {primary_keywords[0]} " if primary_keywords else "")
                    keyword_added = True
            paragraph = " ".join(words)

        # Ensure good paragraph structure
        if len(paragraph) > 300:  # If paragraph is too long, consider splitting
            sentences = re.split(r'(?<=[.!?]) +', paragraph)
            temp_paragraph = ""
            sub_paragraphs = []

            for sentence in sentences:
                if len(temp_paragraph + sentence) < 200:
                    temp_paragraph += sentence + " "
                else:
                    sub_paragraphs.append(temp_paragraph.strip())
                    temp_paragraph = sentence + " "

            if temp_paragraph.strip():
                sub_paragraphs.append(temp_paragraph.strip())

            if len(sub_paragraphs) > 1:
                optimized_content.extend(sub_paragraphs)
            else:
                optimized_content.append(paragraph)
        else:
            optimized_content.append(paragraph)

    return "\n\n".join(optimized_content)

def ensure_islamic_authenticity(content: str) -> Tuple[str, List[str]]:
    """
    Ensure the content maintains Islamic authenticity and provide suggestions if needed.
    """
    suggestions = []

    # Check for common issues in Islamic content
    if re.search(r'\b(god|lord|creator)\b', content, re.IGNORECASE) without 'Allah' in content:
        suggestions.append("Consider using 'Allah' when referring to the Islamic concept of God")

    if re.search(r'\b(jesus|christ|son of god)\b', content, re.IGNORECASE) without 'Isa' in content:
        suggestions.append("Use 'Prophet Isa (Jesus)' when referring to Jesus in Islamic context")

    if 'bible' in content.lower() and 'quran' not in content.lower():
        suggestions.append("For Islamic content, consider referencing the Quran as the primary source")

    if 'trinity' in content.lower():
        suggestions.append("Ensure content aligns with Islamic monotheistic beliefs (Tawhid)")

    # Add Islamic blessings when appropriate
    if 'prophet' in content.lower() and 'blessings be upon him' not in content.lower():
        suggestions.append("Consider adding 'peace be upon him' (PBUH) after mentioning prophets")

    return content, suggestions

def optimize_content(content: str, title: str, description: str, primary_keywords: List[str]) -> Dict:
    """
    Complete optimization of Islamic content.
    """
    # Analyze original content
    original_analysis = analyze_content(content)

    # Optimize each component
    optimized_title = optimize_title(title, primary_keywords)
    optimized_description = optimize_description(description, primary_keywords)
    optimized_content = optimize_content_structure(content, primary_keywords)

    # Ensure Islamic authenticity
    optimized_content, authenticity_suggestions = ensure_islamic_authenticity(optimized_content)

    # Final analysis
    final_analysis = analyze_content(optimized_content)

    return {
        "original": {
            "title": title,
            "description": description,
            "content": content,
            "analysis": original_analysis
        },
        "optimized": {
            "title": optimized_title,
            "description": optimized_description,
            "content": optimized_content,
            "analysis": final_analysis
        },
        "suggestions": authenticity_suggestions,
        "keywords_used": primary_keywords
    }

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage: python content_optimizer.py <title> <description> <content_file_path> [keyword1 keyword2 ...]")
        print("Example: python content_optimizer.py 'Daily Prayer' 'Learn about daily prayers' content.txt prayer islam")
        sys.exit(1)

    title = sys.argv[1]
    description = sys.argv[2]
    content_file = sys.argv[3]
    keywords = sys.argv[4:] if len(sys.argv) > 4 else []

    # Read content from file
    try:
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = content_file  # Treat as direct content if not a file

    result = optimize_content(content, title, description, keywords)

    print("OPTIMIZATION RESULTS")
    print("=" * 50)
    print("OPTIMIZED TITLE:")
    print(result["optimized"]["title"])
    print()
    print("OPTIMIZED DESCRIPTION:")
    print(result["optimized"]["description"])
    print()
    print("KEYWORDS USED:", ", ".join(result["keywords_used"]))
    print()
    if result["suggestions"]:
        print("AUTHENTICITY SUGGESTIONS:")
        for suggestion in result["suggestions"]:
            print(f"- {suggestion}")
        print()
    print("OPTIMIZED CONTENT PREVIEW (first 500 chars):")
    print(result["optimized"]["content"][:500] + "..." if len(result["optimized"]["content"]) > 500 else result["optimized"]["content"])