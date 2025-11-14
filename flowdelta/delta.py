class DeltaTracker:
    def __init__(self, source_name: str, checkpoint_id: str, *, initial_timestamp=None):
        self.source = source_name
        self.checkpoint = checkpoint_id
        self.initial = initial_timestamp

    def last_timestamp(self):
        return self.initial or "1970-01-01"

def run_delta(source_name: str, since_timestamp: str, verbose: bool = False):
    if verbose:
        print(f"[delta] running {source_name} from {since_timestamp}")
    return {"status": "ok", "from": since_timestamp}
