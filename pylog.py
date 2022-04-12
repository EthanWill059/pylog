### CUSTOM EXCEPTIONS
class logerror(Exception):
    pass
####


class log:
    def out(self, msg='', type='msg'):
        """
        Output log message to the log

        msg = the message the log should display

        type = msg or error
        """
        types = ['msg', 'error']

        if type.lower().strip() == types[0]:
            print(f"\033[1;32;40m [{type}]: {msg} \033[1;37;40m")
        elif type.lower().strip() == types[1]:
            print(f"\033[1;31;40m [{type}]: {msg} \033[1;37;40m")
        else:
            raise logerror(f'[{type}] invalid arg for type, must be type msg or error')