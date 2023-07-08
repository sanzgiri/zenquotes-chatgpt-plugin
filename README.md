# Vanilla OpenAI ChatGPT Plugin

This is a sample repo for developing OpenAI plugin using the FastAPI framework. 

## 💻 Code for the FastAPI app
If you have [access](https://code.visualstudio.com/blogs/2023/03/30/vscode-copilot#_getting-started-today) to [GitHub Copilot](https://github.com/features/copilot), try it out to help you write code faster. To run the app, run `uvicorn main:app` from the comman line

To run tests, just run `pytest`

- `main.py` is the code for the API plugin. (✨ Tip: Generate the code using Copilot. The following is an example prompt to use in the Copilot chat view (`Ctrl+Alt+I`) ([learn more](https://code.visualstudio.com/blogs/2023/03/30/vscode-copilot#_embracing-the-chat-view)).)
   
- `openapi.yaml` is a specification that dictates how to define the schema of the API.

## 🧠 Code to turn the FastAPI app into a ChatGPT plugin
- `ai-plugin.json` is a JSON manifest file that defines relevant metadata for the plugin. Learn more in the [OpenAI docs](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).

## 💬 Register the app on ChatGPT
- GPT-4 -> Plugin store -> Develop your own plugin
- Provide domain as localhost:8000
