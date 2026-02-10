from jinja2 import Template


class TemplateEngineService:
    _news_template = Template(
        """{{ emoji }} *{{ title }}*\n\n{{ body }}\n\n`Impact: {{ impact }}/10` | `Sentiment: {{ sentiment }}`"""
    )

    @classmethod
    def render_news(cls, title: str, body: str, impact: int, sentiment: str) -> str:
        emoji = '🚨' if impact >= 8 else '📊'
        return cls._news_template.render(emoji=emoji, title=title, body=body, impact=impact, sentiment=sentiment)
