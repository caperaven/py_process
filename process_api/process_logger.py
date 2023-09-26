import logging
import io


class ProcessLogger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger("process_api")
        self.log_buffer = io.StringIO()

        self.stream_handler = logging.StreamHandler(self.log_buffer)
        self.stream_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.stream_handler.setFormatter(formatter)
        self.logger.addHandler(self.stream_handler)

    def __del__(self):
        self.stream_handler.close()
        self.log_buffer.close()

    def clear_log(self):
        # Reset the content of the log buffer
        self.log_buffer.truncate(0)
        self.log_buffer.seek(0)

    def print(self):
        log_content = self.log_buffer.getvalue()
        print(log_content)

    def save_to_file(self, file_name):
        log_content = self.log_buffer.getvalue()

        try:
            with open(file_name, 'a') as file:
                file.write(log_content)
            print(f"Log content saved to {file_name}")
        except Exception as e:
            print(f"Error saving log content to {file_name}: {str(e)}")

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def fatal(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
