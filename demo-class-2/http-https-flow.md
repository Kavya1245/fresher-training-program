# How HTTP/HTTPS Works — Browser to Server and Back

## The Full Journey (Step by Step)

```
[1] You type a URL          [2] DNS Lookup           [3] TCP Connection
    in the browser      →       (domain → IP)     →      established
        │                                                     │
        ▼                                                     ▼
[6] Browser renders  ←   [5] Server sends       ←   [4] Browser sends
    the response              response back            HTTP request
```

### Step 1: You Enter a URL
Example: `https://www.example.com/products`
Browser parses it: scheme (`https`), domain (`www.example.com`), path (`/products`).

### Step 2: DNS Lookup (Domain → IP Address)
Computers communicate using IP addresses, not domain names, so the browser needs to translate `www.example.com` into something like `93.184.216.34`.

Lookup order (browser checks each, stopping as soon as it finds an answer):
1. Browser cache
2. OS cache
3. Router cache
4. ISP's DNS resolver
5. Root → TLD → Authoritative DNS servers (if not cached anywhere)

### Step 3: TCP Connection (and TLS Handshake for HTTPS)
The browser opens a **TCP connection** to the server's IP on port 80 (HTTP) or 443 (HTTPS).

**If HTTPS:** before any data is exchanged, a **TLS handshake** happens:
- Browser and server agree on encryption method
- Server proves its identity using an **SSL/TLS certificate**
- A shared secret key is established
- All further communication is encrypted

This is the core difference from plain HTTP: **HTTPS = HTTP + encryption (TLS/SSL) + server identity verification.**

### Step 4: Browser Sends an HTTP Request
```
GET /products HTTP/1.1
Host: www.example.com
```
Includes method (GET/POST/PUT/DELETE), headers (cookies, auth tokens, content-type), and body (for POST/PUT).

### Step 5: Server Processes and Responds
The server's business layer processes the request (may query a database), then sends back:
```
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```
Includes a **status code** (200 OK, 404 Not Found, 500 Server Error, etc.), headers, and the response body.

### Step 6: Browser Renders the Response
The browser parses the HTML/CSS/JS and displays the page. If HTTPS, this entire response was encrypted in transit and decrypted only by your browser.

---

## HTTP vs HTTPS — Quick Comparison

| | HTTP | HTTPS |
|---|---|---|
| Port | 80 | 443 |
| Encryption | None — data sent in plain text | TLS/SSL encrypted |
| Certificate | Not required | Requires a valid SSL certificate |
| Data security | Vulnerable to interception | Protected from eavesdropping/tampering |
| Browser indicator | "Not Secure" warning | Padlock icon |

---

## Common Status Codes to Know

| Code | Meaning |
|---|---|
| 200 | OK — success |
| 201 | Created — resource successfully created |
| 301 / 302 | Redirect (permanent / temporary) |
| 400 | Bad Request — client sent invalid data |
| 401 | Unauthorized — authentication required |
| 403 | Forbidden — authenticated but not allowed |
| 404 | Not Found |
| 500 | Internal Server Error |
