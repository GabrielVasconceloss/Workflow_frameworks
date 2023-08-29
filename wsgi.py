from app import manager

if __name__ == "__main__":
    manager.run()


@manager.command
def runserver():
    """
    Inicia o servidor Gunicorn.
    """
    host = '192.168.0.48'  # Ou qualquer outro host desejado
    port = 5000  # Ou qualquer outra porta desejada
    workers = 4  # Número de workers do Gunicorn

    # Comando para iniciar o servidor Gunicorn
    cmd = f'gunicorn -w {workers} -b {host}:{port} your_module:manager'

    # Executa o comando
    subprocess.call(cmd, shell=True)