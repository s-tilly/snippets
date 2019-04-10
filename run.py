import sys
import shlex
import subprocess


def run(command, debug=False):
    """Run shell command

    On retourne le code retour de la fonction, stdout et stderr dans
    une liste (et dans cet ordre)
    """
    args = shlex.split(command)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if debug:
        print()
        print('command: ', command)
        print('Return code :', p.poll())
        print('stdout:\n', stdout)
        print('stderr:\n', stderr)
        sys.stdout.flush()
    return p.poll(), stdout, stderr

