from app.guardrails.output_guardrail import validate_output

def test_normal_output():

    answer = (
        "You may cancel your subscription at any time."
    )

    assert validate_output(answer) is True

def test_sensitive_output():

    answer = (
        "Your API key is 123."
    )

    assert validate_output(answer) is False

def test_empty_output():

    assert validate_output("") is False