import click
import os
from click_shell import shell

"""
Initialize The Shell Script
This script provides a command-line interface for various Operations.

"""

@shell(prompt = "$shell > " , intro="""
Welcome to the shell! Type 'help' for a list of commands.
Type 'exit' to leave the shell.
       """)
def shell_script() :
    pass



@shell_script.command(name = "--help")
def help() :
    """Display this help message."""
    click.echo("""
Available commands: 
          
- help: Display this help message.
- lc: List all available commands.
- lt: List all files and directories in the current directory.
- cl: Clear the shell screen. 
- cfile : Create a new file with the specified name.
- dfile : Delete a file with the specified name. 
- rfile : Rename a file from old_name to new_name.
- exit: Exit the shell.  
- cdn: Get the current working directory.      
          """)
    
@shell_script.command()
def cl() :
    os.system('cls' if os.name == 'nt' else 'clear')


@shell_script.command(name= "lc")
def list_of_commands() :
    """
    List all available commands.
    """
    click.echo("Available commands:")
    for command in shell_script.commands:
        click.echo(command)




"""
----------------- Working With Files And Directories -------------
"""

@shell_script.command(name = '--lt')
def get_items_in_current_dir() :
    """
    List all files and directories in the current directory.
    """
    for item in os.listdir(os.getcwd()):
        click.echo(item)

@shell_script.command(name = '--cdn')
def current_working_dir() :
    """
    Get The current working directory.
    """
    click.echo(os.getcwd())

@shell_script.command(name = 'cf')
@click.option('-f', prompt='Enter the file name', type=str, required=False)
def create_file(f) :
    """
    Create a new file with the specified name.
    """
    
    if os.path.exists(f):
        click.echo(f"File '{f}' already exists.")
        return
    
    try:
        with open(f , 'w') as file :
            file.write("")
        click.echo(f"File '{f}' created successfully.")

    except Exception as e:
        click.echo(f"Error creating file '{f}': {e}")



@shell_script.command(name = 'df')
@click.option('-f', prompt='Enter the file name', type=str, required=False)
def delete_file(f) :
    """
    Delete a file with the specified name.
    """
    
    if not os.path.exists(f):
        click.echo(f"File '{f}' does not exist.")
        return
    
    try:
        os.remove(f)
        click.echo(f"File '{f}' deleted successfully.")
    except Exception as e:
        click.echo(f"Error deleting file '{f}': {e}")


@shell_script.command(name = "rn")
@click.option('--old_name', prompt='Enter the old file name', type=str, required=False)
@click.option('--new_name', prompt='Enter the new file name', type=str, required=False)
def rename_file(old_name, new_name) :
    """
    Rename a file from old_name to new_name.
    """
    
    if not os.path.exists(old_name):
        click.echo(f"File '{old_name}' does not exist.")
        return
    

    try:
        os.rename(old_name, new_name)
        click.echo(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except Exception as e:
        click.echo(f"Error renaming file '{old_name}': {e}")

