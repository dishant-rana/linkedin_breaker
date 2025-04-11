# LinkedIn Breaker

A powerful tool that helps you find and analyze LinkedIn profiles using AI. This project combines web scraping, AI-powered analysis, and profile lookup capabilities to provide insightful information about professionals.

## Features

- 🔍 LinkedIn Profile Lookup: Find LinkedIn profiles using just a person's name
- 🤖 AI-Powered Analysis: Get AI-generated summaries and interesting facts about professionals
- 🔗 Profile Scraping: Extract relevant information from LinkedIn profiles
- 🧠 Smart Summarization: Generate concise summaries and key insights

## Prerequisites

- Python 3.8+
- OpenAI API key
- Tavily API key (for profile lookup)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/linkedin_breaker.git
cd linkedin_breaker
```

2. Install dependencies using pipenv:
```bash
pipenv install
```

3. Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Usage

The project provides two main functionalities:

1. **LinkedIn Profile Lookup**
```python
from agents.linkedin_lookup_agent import lookup

# Find a LinkedIn profile URL
profile_url = lookup(name="John Doe")
```

2. **Profile Analysis**
```python
from linkedin_breaker import ice_break_with

# Get AI-generated summary and interesting facts
analysis = ice_break_with(name="John Doe")
```

## Project Structure

```
linkedin_breaker/
├── agents/              # AI agents for different tasks
├── tools/              # Utility functions and tools
├── third_parties/      # External service integrations
├── linkedin_breaker.py # Main application script
├── Pipfile            # Python dependencies
└── .env               # Environment variables
```

## Dependencies

- langchain
- langchain-openai
- python-dotenv
- tavily-python

## License

This project is licensed under the terms specified in the LICENSE file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is intended for professional and research purposes only. Please ensure you comply with LinkedIn's terms of service and respect privacy guidelines when using this tool.