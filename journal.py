import click
import time
import os
import subprocess
import settings

journal_dir = os.path.expanduser(settings.JOURNALDIR)


@click.command()
def cli():
    buff_fn = '.'+time.strftime("%Y-%m-%d", time.localtime())+".buffer.md"
    subprocess.Popen([settings.EDITORCMD, "-w", buff_fn]).wait()
    buff = '\n'+open(buff_fn).read()
    ts = time.strftime(settings.TSFORMAT, time.localtime())
    write_to_journal(ts+'\t'+buff)
    os.remove(buff_fn)


def write_to_journal(text, timestamp=None):
    a = None
    today = time.strftime("%Y-%m-%d", time.localtime())
    filename = journal_dir+today+'.journal'
    click.echo(filename)
    with open(filename, "a") as journal_fp:
        a = journal_fp.write('\n'+text)
    return a
