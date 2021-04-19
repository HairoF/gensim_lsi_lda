class Question(object):

    def __init__(self,title='',price='',acquired_compet='', descr='', required_compet=''):
        self.title = title
        self.price = price
        self.acquired_compet = acquired_compet
        self.descr = descr
        self.required_compet = required_compet

    def __str__(self):

        return f"{self.title} {self.price} {self.acquired_compet} {self.descr} {self.required_compet}"