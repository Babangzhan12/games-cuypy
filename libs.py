import  socket
from time import sleep
PC_NAME = socket.gethostname()

def welcome_mesage():
    style = "*" * (len(PC_NAME) + 6)
    print(style)
    print(f"** {PC_NAME} **")
    print(style)
    
def exit_program():
    print('program akan dihentikan!')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    print('program berhasil dihentikan!')
    
if __name__ == '__main__':
    welcome_mesage()
    exit_program()