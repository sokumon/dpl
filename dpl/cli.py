import click
from dpl.appscript import send_to_sheet
from dpl.config import writer
import sys

@click.command()
@click.option('-t', '--task', help='The task to be added')
@click.option('-r', '--remarks', help='Remarks for the task')
@click.option('-e', '--eod_status', help='End of day status for the task')
@click.option('-c', '--change', help='Change URL of the deployed app script')
def cli(task, remarks, eod_status, change):
    """Simple program to add tasks to Google Sheets or change the URL of the app script."""
    if change:
        # Implement the logic to change the URL
        writer(change)
        click.echo(f"URL changed to '{change}'")
    elif task and remarks and eod_status:
        response = send_to_sheet(task, remarks, eod_status)
        if response is None:
            click.echo("Configure url using 'dpl -c URL'")
            sys.exit(0)
        if response["status"] == "done":
            click.echo(f"Task '{task}' added with remarks '{remarks}' and EOD status '{eod_status}'.")
    else:
        click.echo("Please provide a task, remarks, and EOD status or use the --change option to change the URL.")

if __name__ == '__main__':
    cli()
