from django.http import HttpResponse

# def CustomFunctionMiddleware(get_response):
#     # One time configuration or initialization
#     print("One time Configuration")

#     def middleware(request):
#         # Executed before 'view' is called - request
#         print("Executed before the view")
#         response = get_response(request)
#         print("Executed after the view")
#         # Executed after view is called - response
#         return response

#     return middleware


class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One time configuration or initialization
        print("One time Configuration")

    def __call__(self, request):
        # Executed before 'view' is called - request
        print("Executed before the view")
        response = self.get_response(request)
        print("Executed after the view")
        # Executed after view is called - response
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Called before calling the view")
        return None
