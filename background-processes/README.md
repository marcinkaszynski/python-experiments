Simple API at running multiple processes in background.

Proof of concept quality level.

Usage:

```python
import background as bg
import requests

# Start a group of processes in background before executing commands
# in the `with` block, kill those processes once the block is over.
with bg.shell_cmds(['python3 -m http.server 7890',
                    'redis-server -p 1234']):
    # Note that you're not guaranteed that those processes get to any
    # particular state by the time the next command runs.  The code
    # should handle it, for example by waiting for availability
    # of some port or retrying connections.
    resp = requests.get('http://localhost:7890')
```

Wishlist:

```python
with bg.shell_cmds(['python3 -m http.server 7890',
                    'redis-server -p 1234'],
                    wait_for_ports=[7890, 1234]) as procs:

    procs.kill()
    print("http server stdout:\n%s\n" % procs[0].stdout)
    print("http server stderr:\n%s\n" % procs[0].stderr)
```
