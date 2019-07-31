class U2FClientDataValidationError(ValueError):
    """Exception class used to indicate a failure
    in the validation of client data errors.
    Each property should have its own type, e.g.:

    Wrong type:
        - message: 'Wrong type! Was: <X>, expecting <Y>'
        - property: 'type'

    Wrong challenge:
        - message: 'Wrong challenge! Was <X>, expecting <Y>'
        - property: 'challenge'

    Wrong facet:
        - message: 'Wrong facet! Was <X>, expecting <Y>'
        - property: 'facet'
    """
    def __init__(self, message, property):
        super(U2FClientDataValidationError, self).__init__(message)
        self.property = property

class U2FSignatureError(ValueError):
    """Exception class used to indicate a failure
    validating the SignatureData of a request."""
    pass

class U2FSignRequestError(ValueError):
    """Exception class used to indicate a failure
    when signing a request."""
    pass

class U2FRegisterRequestError(ValueError):
    """Exception class used to indicate a failure
    when registering a device."""
    pass
