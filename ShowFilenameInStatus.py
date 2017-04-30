import sublime_plugin

MAX_FILE_LENGTH = 100


class ShowFilenameInStatus(sublime_plugin.EventListener):
    def on_activated_async(self, view):
        filename = view.file_name()
        view.erase_status('_filename')
        if filename is not None:
            if len(filename) > MAX_FILE_LENGTH:
                filename = filename[-(MAX_FILE_LENGTH - 3):]
            view.set_status('_filename', 'File "...{}"'.format(filename))
