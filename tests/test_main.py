def test_chatbot():
    assert chatbot("Hello, how are you?") != ""
    assert chatbot("What is the meaning of life?") != ""
    assert chatbot("What is the capital of France?") != ""
    assert chatbot("What is the weather like today?") != ""
    assert chatbot("Tell me a joke.") != ""
