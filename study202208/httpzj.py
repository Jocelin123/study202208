"""An addon using the abbreviated scripting syntax."""

from mitmproxy import http
from io
def request(flow.http.HTTPFlow):
    flow.request.headers["myheader"] = "value"
    flow.request.url=='/search'