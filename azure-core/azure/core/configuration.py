# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from azure.core.pipeline.transport import TransportConfiguration

class Configuration(object):
    """Add proxy.

    :param str protocol: Protocol for which proxy is to be applied. Can
        be 'http', 'https', etc. Can also include host.
    :param str proxy_url: The proxy URL. Where basic auth is required,
        use the format: http://user:password@host
    """

    def __iter__(self):
        dict_values = dict(self.__dict__)
        for attr, value in dict_values.items():
            try:
                yield attr, dict(value)
            except TypeError:
                yield attr, value


    def __init__(self, **kwargs):
        # Communication configuration - applied per transport.
        self.connection = TransportConfiguration(**kwargs)

        # Headers (sent with every request)
        self.headers = None

        # Proxy settings (Currently used to configure transport, could be pipeline policy instead)
        self.proxy = None
 
        # Redirect configuration
        self.redirect = None

        # Retry configuration
        self.retry = None

        # Logger configuration
        self.logging = None

        # User Agent configuration
        self.user_agent = None