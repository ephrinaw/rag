class StateManager:
    def __init__(self):
        self.state = {
            "question": "",
            "documents": [],
            "generation": "",
            "retries": 0,
            "web_search": False
        }

    def update_question(self, question):
        self.state["question"] = question

    def update_documents(self, documents):
        self.state["documents"] = documents

    def update_generation(self, generation):
        self.state["generation"] = generation

    def increment_retries(self):
        self.state["retries"] += 1

    def set_web_search_flag(self, value: bool):
        self.state["web_search"] = value
