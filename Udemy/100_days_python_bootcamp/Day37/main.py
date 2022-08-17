import requests



user_parameters = {
    "token": "skdflsdfjbrfsdsdj",
    "username": "mqondisi",
    "notMinor": "yes",
    "agreeTermsOfService": "yes"
}

response = requests.post(url="https://pixe.la/v1/users", json=user_parameters)
print(response.text)