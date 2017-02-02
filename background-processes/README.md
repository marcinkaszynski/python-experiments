Simple API at running multiple processes in background.

Usage:

```python
import background as bg
import requests

# Start a group of processes in background before executing commands
# in the `with` block, kill those processes once the block is over.
with bg.shell_cmds(['python -M SimpleHttpServer 7890',
                    'redis-server -p 1234']):
    # Note that you're not guaranteed that those processes get to any
    # particular state by the time the next command runs.  The code
    # should handle it, for example by waiting for availability
    # of some port or retrying connections.
    resp = requests.get('http://localhost:7890')
```
