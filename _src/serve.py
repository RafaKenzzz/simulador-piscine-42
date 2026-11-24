"""Servidor local que imita o alojamento: /servicos serve servicos.html.

Uso:  python _src/serve.py [porta]   (por omissão 8123; depois abra http://localhost:8123)
"""
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def send_head(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        local = self.translate_path(path)
        if not path.endswith("/") and os.path.exists(local.rstrip("\/") + ".html"):
            self.path = path + ".html" + self.path[len(path):]
        elif not os.path.exists(local) and not path.endswith("/"):
            self.send_error(404)
            return None
        return super().send_head()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
    print(f"http://localhost:{port}")
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
