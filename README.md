# FactGPT
FactGPT is a project for CS 338 aimed at fact-checking ChatGPT's responses.

Due to ChatGPT's unreliability when it comes to generating facts, we wanted to create a product that would help our users, people who rely on ChatGPT for correct facts, feel secure in the responses they are given.

To fact-check a sentence, all you need to do is click on it. FactGPT will proceed to mark the sentence as either "Likely Correct," "Likely Wrong," or "Unclear" based on the Wikipedia evidence it gathered. FactGPT will provide a brief explanation for the former two cases. It will also present the link to the Wikipedia article that it utilized for reference.

**IMPORTANT NOTE**: Please assign an OpenAI API key to OPENAI_API_KEY in README.md before running the program