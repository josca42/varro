import signal
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.utils.capture import capture_output

TerminalInteractiveShell.orig_run = TerminalInteractiveShell.run_cell


def run_cell(self, cell, timeout=None):
    "Wrapper for original `run_cell` which adds timeout, memory limit, and output capture"
    if timeout:

        def handler(*args):
            raise TimeoutError()

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
    try:
        with capture_output() as io:
            result = self.orig_run(cell)
        result.stdout = io.stdout
        return result
    except TimeoutError as e:
        result = self.ExecutionResult(error_before_exec=None, error_in_exec=e)
    finally:
        if timeout:
            signal.alarm(0)


TerminalInteractiveShell.run_cell = run_cell


def get_shell() -> TerminalInteractiveShell:
    "Get a `TerminalInteractiveShell` with minimal functionality"
    sh = TerminalInteractiveShell()
    sh.logger.log_output = sh.history_manager.enabled = False
    dh = sh.displayhook
    dh.finish_displayhook = dh.write_output_prompt = dh.start_displayhook = lambda: None
    dh.write_format_data = lambda format_dict, md_dict=None: None
    sh.logstart = sh.automagic = sh.autoindent = False
    sh.autocall = 0
    sh.system = lambda cmd: None
    return sh
