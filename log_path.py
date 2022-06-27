import os



class log_file_path():

   def get_log_file_dir(self):
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd, 'Logs')
        return file_path

