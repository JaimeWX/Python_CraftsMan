conn = create_conn(host, port, timeout=None)
try:
    conn.send_text('Hello, world!')
except Exception as e:
    print(f'Unable to use connection: {e}')
finally:
    conn.close()