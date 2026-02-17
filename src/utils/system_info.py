import psutil

def get_system_stats():
    """
    Retrieves current system CPU and Memory usage.
    Returns:
        dict: {'cpu_percent': float, 'memory_percent': float}
    """
    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent
    }
