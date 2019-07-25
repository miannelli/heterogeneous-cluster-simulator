class ResponseDirectory(object):
    pass




class Response(object):
    """ An abstract base class for responses within the datacenter """
    def __init__(self, code, description):
        self.code = code
        self.description = description




class Success(Response):
    """ An abstract base class for success responses within the datacenter """
    def __init__(self, description):
        code = 0
        super(Success, self).__init__(code, description)

class SuccessfulVMCreation(Success):
    """ Response that indicates successful creation of VM """
    pass

class SuccessfulVMResize(Success):
    """ Response that indicates successful resizing of VM """
    pass






class Error(Response):
        """ An abstract base class for error responses within the datacenter """
    def __init__(self, code, description):
        assert code > 0, "Errors must have code > 0"
        super(Error, self).__init__(code, description)

class InsufficientResourcesError(Error):
        """ Response that indicates insufficient resources to perform operation """
    def __init__(self):
        code = 1
        description = "Insufficient Resources"
        super(InsufficientResourcesError, self).__init__(code, description)
