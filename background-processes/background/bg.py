import honcho.compat
import honcho.manager


class ProcessManager(honcho.manager.Manager):
    # This uses way too much of honcho inner API and copy-pasted code.
    # Doing it right will require refactoring honcho.

    def handle_event(self):
        try:
            msg = self.events.get_nowait()
        except honcho.compat.Empty:
            return False

        if msg.type == 'line':
            self._printer.write(msg)
        elif msg.type == 'start':
            self._processes[msg.name]['pid'] = msg.data['pid']
            self._system_print("%s started (pid=%s)\n"
                               % (msg.name, msg.data['pid']))
        elif msg.type == 'stop':
            self._processes[msg.name]['returncode'] = msg.data['returncode']
            self._system_print("%s stopped (rc=%s)\n"
                               % (msg.name, msg.data['returncode']))

        return True

    def handle_all_events(self):
        while True:
            if not self.handle_event():
                return

    def start(self):
        self._start()


class BgContextManager(object):
    def __init__(self, cmds):
        self.cmds = cmds

    def __enter__(self):
        self.manager = ProcessManager()
        for (i, cmd) in enumerate(self.cmds):
            self.manager.add_process('p%d' % i, cmd)

        self.manager.start()

    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: potentially print output on exception
        self.manager.handle_all_events()
        self.manager.kill()


shell_cmds = BgContextManager
