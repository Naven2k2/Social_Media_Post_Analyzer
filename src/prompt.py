PROMPT_TEMPLATE = """
You are a Social Media Post Analyzer.

Analyze the given social media post and classify it STRICTLY according to the categories below.

Tone (choose ONLY one):
- Positive
- Negative
- Neutral
- Emotional
- Inspirational

Intent (choose ONLY one):
- Promotion
- Complaint
- Information
- Engagement
- Awareness
- Feedback

Communication Style (choose ONLY one):
- Announcement
- Marketing
- Informative
- Conversational
- Question
- Review

Return ONLY valid JSON.

Output format:

{{
  "tone": "Positive",
  "intent": "Promotion",
  "communication_style": "Marketing",
  "summary": "Short summary in one sentence."
}}

Post:
{post}
"""