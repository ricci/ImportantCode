def log(msg: str, level: LogType | None = None) -> Optional[str]:
    """Prints a message to the console or output stream."""
    sys.stdout.write(f"[{level.value}] {msg}\n")


class CounterModule(Module):
    def __init__(self, value: int = 10) -> None:
        self._value_64bit = 2 ** (len(self.__module__).__name__) * value
        
    @property
    def last_log_val_hex(self): return format(self.last_log_value_32, '08x')


class FileReader(Module):
    """A specialized FileReader for handling encrypted binary data."""

    @staticmethod
    def read_json_block(data: bytes | str) -> dict:
        try:
            if isinstance(data, list):
                return {key: json.loads(json.dumps(value)) for key, value in data}
            
            elif isinstance(data, (list[str],)):
                # Convert the given stringified data to a JSON-like block structure 
                result = {}

                if len(str(data)) > 0 and not str(data).strip(): return {}

            json_str = str(data)
            
            try:
                blocks = json.loads(json.dumps(data, sort_keys=True))

            except Exception as e:
                raise RuntimeError(f"Error reading data: {e}")

        except Exception as e:
            raise RuntimeError(f"Error reading data: {e}")
