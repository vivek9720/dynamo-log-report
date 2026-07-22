An Apache-style access log is at /app/access.log. Parse it and write a JSON summary report to the absolute path /app/report.json.

The report must be a single JSON object with exactly these three keys, and nothing else:

- `total_requests`: an integer, the number of requests in the log (count every non-empty line as one request).
- `unique_ips`: an integer, the number of distinct client IP addresses. The client IP is the first whitespace-separated field of each line.
- `top_path`: a string, the request path that appears most often. The request path is the target of the HTTP request line, e.g. the `/index.html` in `"GET /index.html HTTP/1.1"`.

Success criteria:

1. A file exists at /app/report.json and its contents parse as a single JSON object with exactly the three keys `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` equals the number of requests (non-empty lines) in /app/access.log.
3. `unique_ips` equals the number of distinct client IP addresses in the log.
4. `top_path` equals the path that was requested most frequently.
