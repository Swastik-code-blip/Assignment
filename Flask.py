"""
PW Skills: Web API & Flask Assignment Solutions
All 40 questions answered in a single, executable Python script.
"""

answers = {
    1: "A Web API (Application Programming Interface) is a set of rules and protocols over the web that allows different software applications to communicate with each other[cite: 5].",
    2: "All Web APIs are web services, but not all web services are Web APIs. Web services require a SOAP protocol and XML, whereas Web APIs can use REST, HTTP, JSON, and XML and are more lightweight[cite: 5].",
    3: "Benefits include modularity, code reusability, decoupled frontend and backend systems, scalability, and easy integration with third-party services[cite: 5].",
    4: "SOAP uses XML and strictly follows protocol standards with built-in security, while REST is an architectural style that is flexible, lightweight, and typically uses JSON[cite: 5].",
    5: "JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is commonly used in Web APIs as the standard payload format for requests and responses[cite: 5].",
    6: "Other protocols include SOAP, GraphQL, gRPC, and WebSockets[cite: 5].",
    7: "HTTP methods define the desired action to be performed on a resource: GET (retrieve), POST (create), PUT (update/replace), PATCH (modify), and DELETE (remove)[cite: 5].",
    8: "Authentication verifies *who* the user is, while authorization determines *what* resources or actions the authenticated user is allowed to access[cite: 5].",
    9: "Versioning can be handled via URL path (/api/v1/resource), query parameters (?version=1), or custom request headers (Accept: application/vnd.app.v1+json)[cite: 5].",
    10: "An HTTP request consists of a Request Line (method + URI + version), Headers, and an optional Body. An HTTP response consists of a Status Line (version + status code + reason), Headers, and a Body[cite: 5].",
    11: "Rate limiting restricts the number of requests a client can make to an API within a specific time window to prevent abuse, DDoS attacks, and server overload[cite: 5].",
    12: "Errors are handled using standard HTTP status codes (e.g., 400 Bad Request, 404 Not Found, 500 Internal Server Error) combined with a descriptive JSON error payload[cite: 5].",
    13: "Statelessness means the server does not store any client state or session information between requests; every request from the client must contain all necessary authentication and context information[cite: 5, 6].",
    14: "Best practices include using meaningful nouns for endpoints, proper HTTP status codes, versioning, consistent error handling, and documentation using OpenAPI/Swagger[cite: 5, 6].",
    15: "API keys and tokens (like JWT) authenticate and authorize clients, ensuring that only trusted applications or users can access protected endpoints[cite: 5, 6].",
    16: "REST (Representational State Transfer) is an architectural style based on six guiding constraints: client-server, stateless, cacheable, layered system, code on demand, and uniform interface[cite: 6].",
    17: "RESTful APIs use standard HTTP methods and are lightweight (usually JSON), whereas traditional web services often rely on SOAP over XML with strict operational contracts (WSDL)[cite: 5, 6].",
    18: "GET (retrieve data), POST (create new resource), PUT (replace existing resource), PATCH (update resource partially), and DELETE (remove resource)[cite: 5, 6].",
    19: "Each request from a client must contain all the information needed to understand and process it, with zero session state maintained on the server[cite: 6].",
    20: "URIs uniquely identify resources on the server, allowing clients to locate and interact with them using standard HTTP methods[cite: 6].",
    21: "Hypermedia allows clients to dynamically navigate an API via links provided in the response. It relates to HATEOAS (Hypermedia As The Engine Of Application State)[cite: 6].",
    22: "Scalability, flexibility, loose coupling, cacheability, and widespread adoption/ease of use over HTTP[cite: 6].",
    23: "Resource representations are the data formats (like JSON or XML) in which a resource is transferred between client and server[cite: 6].",
    24: "Via a client-server architecture over the HTTP protocol using request-response cycles and stateless communication[cite: 6].",
    25: "JSON and XML are the most common formats, with JSON being the industry standard for modern web APIs[cite: 6].",
    26: "Status codes inform the client about the outcome of their request (e.g., 2xx success, 4xx client error, 5xx server error)[cite: 6].",
    27: "Versioning allows developers to introduce breaking changes without disrupting existing clients, typically managed via URI paths or headers[cite: 5, 6].",
    28: "Security is ensured using HTTPS, input validation, rate limiting, and authentication methods such as API keys, Basic Auth, OAuth 2.0, and JWT[cite: 6].",
    29: "Provide clear endpoint descriptions, request/response examples, authentication details, and interactive documentation tools like Swagger/OpenAPI[cite: 6].",
    30: "Return appropriate HTTP status codes along with descriptive error messages in a consistent JSON structure[cite: 6].",
    31: "SOAP (Simple Object Access Protocol) is a protocol with strict XML-based messaging standards, whereas REST is an architectural style that is lightweight and flexible[cite: 5, 6].",
    32: "A SOAP message is an XML document containing an Envelope (root element), an optional Header (metadata/security), and a Body (containing the call and response data)[cite: 6].",
    33: "SOAP handles communication via XML messages wrapped in HTTP, SMTP, or TCP, relying on WSDL (Web Services Description Language) contracts[cite: 6].",
    34: "Advantages: Built-in error handling, strict security, enterprise-grade standards. Disadvantages: Highly complex, heavier payload (XML), slower performance[cite: 6].",
    35: "SOAP ensures security through WS-Security standards, supporting XML encryption, XML digital signatures, and secure tokens[cite: 6].",
    36: "Flask is a lightweight micro-framework for Python. It provides the essentials (routing and request handling) without forcing a specific database or project layout, unlike opinionated frameworks like Django[cite: 6].",
    37: "A basic Flask app consists of importing the Flask class, initializing an app instance (`app = Flask(__name__)`), defining routes using decorators (`@app.route()`), and running the app (`app.run()`)[cite: 6].",
    38: "Flask can be installed locally via terminal using pip: `pip install flask`[cite: 6].",
    39: "Routing in Flask maps URLs to Python functions using the `@app.route('/path')` decorator so that executing a URL triggers the associated view function[cite: 6].",
    40: "Flask templates use the Jinja2 engine to render dynamic HTML pages by passing variables from backend Python routes into HTML templates[cite: 6]."
}

if __name__ == "__main__":
    print("======================================================")
    print("     PW SKILLS: WEB API & FLASK ASSIGNMENT SOLUTIONS  ")
    print("======================================================\n")
    
    for q_no, ans in answers.items():
        print(f"Q{q_no}: {ans}\n")
