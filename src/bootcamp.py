import datetime

def get_mission_start_time() -> str:
    """
    Returns the current timestamp in ISO format.
    Serves as the Genesis Block for the 90-Day Challenge.
    """
    return datetime.datetime.now().isoformat()

def announce_start():
    """
    Prints the official start message.
    """
    start_time = get_mission_start_time()
    print(f"🚀 MISSION STARTED: {start_time}")
    print("The Green Graph protocol is active.")

if __name__ == "__main__":
    announce_start()
