import click
from appscript import  send_to_sheet

@click.command()
@click.option('-t', '--task', required=True, help='The task to be added')
@click.option('-r', '--remarks', required=True, help='Remarks for the task')
@click.option('-e', '--eod_status', required=True, help='End of day status for the task')
def cli(task, remarks, eod_status):
    """Simple program to add tasks to Google Sheets."""
    response = send_to_sheet(task, remarks, eod_status)
    if response["status"] == "done":
        click.echo(f"Task '{task}' added with remarks '{remarks}' and EOD status '{eod_status}'.")

if __name__ == '__main__':
    cli()