// business/server.js
// BUSINESS LAYER: handles requests, validates data, talks to storage layer
const http = require('http');
const fs = require('fs');
const path = require('path');

const STORAGE_FILE = path.join(__dirname, '..', 'storage', 'data.json');
const PRESENTATION_FILE = path.join(__dirname, '..', 'presentation', 'index.html');

// ---- Business Logic: Validation ----
function validateUser(name, email) {
  if (!name || name.trim().length < 2) {
    return { valid: false, message: 'Name must be at least 2 characters.' };
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email || !emailRegex.test(email)) {
    return { valid: false, message: 'Please enter a valid email address.' };
  }
  return { valid: true };
}

// ---- Storage Layer helpers ----
function readData() {
  if (!fs.existsSync(STORAGE_FILE)) return [];
  const raw = fs.readFileSync(STORAGE_FILE, 'utf-8');
  return raw ? JSON.parse(raw) : [];
}

function writeData(records) {
  fs.writeFileSync(STORAGE_FILE, JSON.stringify(records, null, 2));
}

// ---- Server (routes requests between presentation and storage) ----
const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/') {
    const html = fs.readFileSync(PRESENTATION_FILE);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
    return;
  }

  if (req.method === 'GET' && req.url === '/data') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(readData()));
    return;
  }

  if (req.method === 'POST' && req.url === '/submit') {
    let body = '';
    req.on('data', chunk => (body += chunk));
    req.on('end', () => {
      const { name, email } = JSON.parse(body || '{}');
      const validation = validateUser(name, email);

      if (!validation.valid) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: false, message: validation.message }));
        return;
      }

      const records = readData();
      records.push({ name, email });
      writeData(records);

      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ success: true, message: 'User saved successfully!' }));
    });
    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('Not found');
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Business layer server running at http://localhost:${PORT}`);
});
