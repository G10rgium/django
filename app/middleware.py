class OurMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)

    def __call__(self, request):
        # print(f"hello from middleware \n", request)
        response = self.get_response(request)
        return response