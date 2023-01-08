from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

def retrieve(prompt:str):
    url = 'https://api.openai.com/v1/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
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
        self.wfile.write(body)

import ipaddress,socket

# Get the first available network interface
interface = ipaddress.ip_interface(ipaddress.ip_network(socket.gethostname()))

# Get the IP address of the interface
ip_address = interface.ip

print(f'hosting on {ip_address} on port 5999')

httpd = HTTPServer((ip_address, 5999), RequestHandler)
httpd.serve_forever()
