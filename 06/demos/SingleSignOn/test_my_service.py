from unittest.mock import Mock

from my_service import MyService, Request
from single_sign_on import SSOToken, SingleSignOnRegistry


def test_hello_name():
    stub_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(stub_sso_registry)
    response = service.handle(Request("Emily"), SSOToken())
    assert response.text == "Hello Emily!"
    #this acts as a stub so it will not fail the test at the end of the assertion

def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken()
    service.handle(Request("Emily"), token)
    spy_sso_registry.is_valid.assert_called_with(token)
    #this acts as a spy because its possible to fail as it calls for the token and will check the name agaisnt it

def test_single_sign_on_with_invalid_token():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    spy_sso_registry.is_valid.return_value = False
    service = MyService(spy_sso_registry)
    token = SSOToken()
    response = service.handle(Request("Emily"), token)
    spy_sso_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"
    #this will give the assertion that the user is properly signed in and if they are not it will fail the test if they dont get the message to sign in

def confirm_token(correct_token):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError("wrong token received")
    return is_valid
    #this fucntion is needed for the mock listed below by replacing the single sign on in the reg

def test_single_sign_on_receives_correct_token():
    mock_sso_registry = Mock(SingleSignOnRegistry)
    correct_token = SSOToken()
    mock_sso_registry.is_valid = Mock(side_effect=confirm_token(correct_token))
    service = MyService(mock_sso_registry)
    service.handle(Request("Emily"), correct_token)
    mock_sso_registry.is_valid.assert_called()
    #Using this mock it will recieve the mock to the constructor and then will handle the request. This will also asser that the isvalid request is called and it will pass. It will fail if it doesnt recieve the call form isvalid, or that if its passed the wrong sso token. The wrong sso token will fail for different reasons, the spy will fail because its getting the wrong sso and will point to the line in the test case. The mock will fail when it is handling the sso token, and will point directly to where the error is being generated in the code itself not in the test.