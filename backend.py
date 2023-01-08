from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

def retrieve(prompt:str):
    url = 'https://api.openai.com/v1/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {TOKEN}'
    }
    body = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'temperature': 0.5,
        'max_tokens': 4000-(len(prompt)//4)
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()
    print(data['choices'][0]['text'])
    return data['choices'][0]['text']




class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        # Send a response
        self.send_response(200)
        self.end_headers()

        rr=retrieve(body.decode('utf-8'))
        self.wfile.write(rr.encode('utf-8'))

import socket
ip_address=socket.gethostbyname(socket.gethostname())

print(f'hosting on {ip_address} on port 5999')

httpd = HTTPServer((ip_address, 5999), RequestHandler)
httpd.serve_forever()
