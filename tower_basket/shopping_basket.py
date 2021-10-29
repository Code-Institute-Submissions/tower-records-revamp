


class Basket():
    """
    class for default behaviors that can be overrided or inherited.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket