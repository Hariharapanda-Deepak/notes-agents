from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Identify the content related to {topic}."
    "Focus on identifying the topic with examples if present."
    "Your final report should clearly articulate the key points,"
    "its topics and examples if present."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the topic.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the topic given. The paragraph should start with explanation of topic followed by examples if present"
    "This article should be easy to understand, engaging, and positive with examples."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)