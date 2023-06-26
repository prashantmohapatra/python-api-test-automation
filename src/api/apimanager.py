import requests
import allure
import os
import json
from environment import ENV


class ApiExecutor:

    @staticmethod
    def send(method, url, headers=None, request_body=None):
        final_request_headers = {}

        if headers is not None:
            final_request_headers.update(headers)

        options = {
            'data': request_body,
            'headers': final_request_headers
        }

        response = None

        if method.upper() == "GET":
            response = requests.get(url, **options)
        elif method.upper() == "POST":
            response = requests.post(url, **options)
        elif method.upper() == "PUT":
            response = requests.put(url, **options)
        elif method.upper() == "PATCH":
            response = requests.patch(url, **options)
        elif method.upper() == "DELETE":
            response = requests.delete(url, **options)

        ReportApiDetails.trace_api_calls(method.upper(), url, final_request_headers, request_body, response)
        
        return response


class ReportApiDetails:
    @staticmethod
    def get_headers_string(headers):
        headers_string = ""

        for key, value in headers.items():
            headers_string += f"{key}: {value}\n"

        return headers_string

    @staticmethod
    def trace_api_calls(method, url, request_headers, request_body, response):
        trace = os.getenv("TRACE_API_CALLS", None).lower()
        
        # When TRACE_API_CALLS environment variable is not defined is OS, get this value from environment.py
        if trace is None:
            trace = ENV["TRACE_API_CALLS"]

        # When trace is true, perform steps for reporting / tracing api calls
        if trace == "true":
            name = method.upper() + ": " + url

            # Convert headers to string when header is not None
            request_headers_tr = ReportApiDetails.get_headers_string(request_headers)

            # Get pretty json of request_body
            if request_body is not None:
                request_object = json.loads(request_body)
                request_body = json.dumps(request_object, indent=4)
            else:
                request_body = ""
    
            # Create request body to be reported
            request_body_det = "\nREQUEST BODY: \n" + request_body

            # Merge request headers and body to create request details
            request_details = "REQUEST HEADER(s): \n" + request_headers_tr + " " + request_body_det

            # Get response headers
            response_headers = ReportApiDetails.get_headers_string(response.headers)

            # Get response body
            response_body = json.dumps(response.json(), indent=4)

            # Merge API response headers and body to create response details
            response_details = (
                    "RESPONSE STATUS: " + str(response.status_code) +
                    "\n\nRESPONSE HEADER(s): \n" + response_headers +
                    "\nRESPONSE BODY: \n" + response_body
            )

            # Merge request and response details to create report
            report = request_details + "\n\n" + response_details + "\n"

            # Add API call details as attachment to allure report
            allure.attach(name=name, body=report)

            # Print API call details in console log
            # print(name, report)
