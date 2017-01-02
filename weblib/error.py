import logging


class WeblibError(Exception):
    """
    Base class for all custom exceptions
    defined in weblib package.
    """


class DataNotFound(WeblibError, IndexError):
    """
    Raised when it is not possible to find requested
    data.
    """


class ResponseNotValid(WeblibError):
    pass


# ********************
# Errors inside weblib
# ********************

class RuntimeConfigError(WeblibError):
    """
    Raised when passed parameters do not makes sense
    or conflict with something.
    """


# *****************************
# ResponseNotValid based Classes
# *****************************

class DataNotValid(ResponseNotValid):
    pass


class RequestBanned(ResponseNotValid):
    pass


class CaptchaRequired(ResponseNotValid):
    pass


class PageNotFound(ResponseNotValid):
    pass


class AccessDenied(ResponseNotValid):
    pass


# *****************************
# ResponseNotValid based Classes
# specific to HTTP code errors
# *****************************

class HttpCodeNotValid(ResponseNotValid): 
    pass


class HttpCodeZero(HttpCodeNotValid):
    pass


# ********************
# Other Errors
# ********************
class NextPageNotFound(WeblibError):
    pass
