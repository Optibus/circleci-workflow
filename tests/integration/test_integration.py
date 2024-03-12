from circle_workflow.code import integration_function

def test_integration_function():
    assert integration_function("foo") == "FOO"
