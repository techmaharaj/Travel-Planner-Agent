# Travel Planner Agent with Weather Integration

This project showcases an agent built using Obot that is designed to assist users in planning trips by leveraging real-time weather conditions at their desired destinations. By integrating a custom Python tool for weather information, the agent dynamically suggests optimal travel plans considering weather forecasts and user preferences.

## Features

- **Trip Planning**: The agent creates comprehensive travel itineraries based on user preferences and prevailing weather conditions. It considers factors such as temperature, precipitation, and wind speed to suggest suitable activities and destinations.
- **Custom Weather Tool**: A custom-built Python tool that gathers weather information. This tool is integral to the agent's decision-making process, ensuring accurate and relevant weather data is always considered.
  

## Prerequisites

Before you begin, ensure you have met the following requirements:

-   **Obot Platform**: This agent is designed to function within the Obot environment.
-   **Python**: Ensure you have Python 3.6 or higher installed to test the tool.
-   **Weather API Key**: API key from http://api.weatherapi.com
-   **AI Model API Key**: API key for the AI model you plan to use. Eg: OpenAI API Key

## Installation

Follow these steps to set up the project:

1.  **Install Obot**: Follow the steps mentioned in the [Obot docs](https://docs.obot.ai/installation/overview)
2.  **Add a custom tool**: On Obot, add a custom tool, by providing the URL of this git repo as [mentioned here](https://docs.obot.ai/tools/first-tool#adding-the-hash-tool-to-obot-python).

## Configuration

Configure the weather tool by setting up the required environment variables.

-   **Environment Variables**: Set the environment variables for the weather tool to function correctly. If the tool uses an API key, set it as follows:

    ```bash
    export API_KEY="your_api_key"
    ```

## Usage

To use the travel planner agent within Obot to plan a trip based on weather conditions:

1.  **Add the Weather Tool to the Agent**: In Obot's agent edit page, add the weather tool to the agent tools or user tools section.
2.  **Interact with the Agent**: Provide prompts to the agent, such as: "I want to visit Bengaluru".

Note: This repo was a part of a talk presented by me at the Toolhouse AI Meetup held in Hyderabad on February 15, 2025.
