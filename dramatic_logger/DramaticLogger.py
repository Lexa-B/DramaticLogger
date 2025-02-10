import sys
import os
from loguru import logger as loguru

# Remove the default handler
loguru.remove()

# Create logging directory if it doesn't exist
os.makedirs("DLogging", exist_ok=True)

DramaticLoggerConfig = {
    "loguru": {
        "level": "INFO",

        "enqueue": True,
        "catch": True,
    },
    "level": {
        "stderr": "TRACE",
        "file": "INFO",
        "remote": "WARNING",
    },

    "startupMessage": "brief"
}

loguru.configure(
    handlers=[
        {
            "sink": sys.stderr,
            "level": DramaticLoggerConfig["level"]["stderr"],
            "format": "<cyan>{time:YYYY-MM-DD HH:mm:ss} </cyan>|<level> {level.name:<8} </level>|<level> {level.icon} {message}</level>",
        },
        {
            "sink": "DLogging/dramatic.log",
            "level": DramaticLoggerConfig["level"]["file"],
            "format": "{time:YYYY-MM-DDTHH:mm:ss.SSS!UTC}Z - {level.icon} {level.name:<8} - {message}",
            "encoding": "utf-8",
            "rotation": "500 KB",
            #"retention": "10 days",
            "compression": "zip",
        },
    ],
    levels=[
        {"name": "SUCCESS", "icon": "✅", "color": "<green>"},
        {"name": "TRACE", "icon": "🔍", "color": "<dim>"},
        {"name": "DEBUG", "icon": "🐞", "color": "<light-blue>"},
        {"name": "INFO", "icon": "💬", "color": "<white>"},
        {"name": "WARNING", "icon": "🚨", "color": "<yellow>"},
        {"name": "ERROR", "icon": "⛔", "color": "<red>"},
        {"name": "CRITICAL", "icon": "🔥", "color": "<red><bg #ff0000>"}  # White text on a red background
    ]
)

DramaticLoggerTopLine = ("\n╒" + ("═" * 96) + "╕\n├─ ")
DramaticLoggerSecondLine = lambda x, **kwargs: (" " + (("─" * (92 - len(x)) + "─┤") if len(x) < 92 else ""))
DramaticLoggerBottomLine = ("\n╘" + ("═" * 96) + "╛\n")

def safe_format_log_message(message, details=False, **kwargs):
    """Safely format a log message with error handling"""
    try:
        # Convert message to string if it isn't already
        message = str(message)
        
        # If exc_info is present in kwargs, handle it
        if 'exc_info' in kwargs:
            # Remove it from kwargs to prevent it from being passed twice
            kwargs.pop('exc_info')
        
        # If this is a dramatic message (with box formatting)
        if kwargs.pop('dramatic', True):
            try:
                formatted = (DramaticLoggerTopLine + 
                           str(message) + 
                           DramaticLoggerSecondLine(message) +
                           (f"\n{details}" if details else "") +
                           DramaticLoggerBottomLine)
            except Exception as e:
                # Fallback if box formatting fails
                formatted = f"[Formatting Error] {message} {details if details else ''}"
        else:
            # Normal message formatting
            formatted = f"{message} {details if details else ''}"
            
        return formatted
    except Exception as e:
        # Ultimate fallback
        return f"[Logger Error: {str(e)}] Unable to format message"

DramaticLogger = {
    "Dramatic": {
        "success": lambda x, y=False, **kwargs: loguru.success(safe_format_log_message(x, y, **kwargs)),
        "trace": lambda x, y=False, **kwargs: loguru.trace(safe_format_log_message(x, y, **kwargs)),
        "debug": lambda x, y=False, **kwargs: loguru.debug(safe_format_log_message(x, y, **kwargs)),
        "info": lambda x, y=False, **kwargs: loguru.info(safe_format_log_message(x, y, **kwargs)),
        "warning": lambda x, y=False, **kwargs: loguru.warning(safe_format_log_message(x, y, **kwargs)),
        "error": lambda x, y=False, **kwargs: loguru.error(safe_format_log_message(x, y, **kwargs)),
        "critical": lambda x, y=False, **kwargs: loguru.critical(safe_format_log_message(x, y, **kwargs))
    },
    "Normal": {
        "success": lambda x, y=False, **kwargs: loguru.success(safe_format_log_message(x, y, dramatic=False, **kwargs)),
        "trace": lambda x, y=False, **kwargs: loguru.trace(safe_format_log_message(x, y, dramatic=False, **kwargs)),
        "debug": lambda x, y=False, **kwargs: loguru.debug(safe_format_log_message(x, y, dramatic=False, **kwargs)),
        "info": lambda x, y=False, **kwargs: loguru.info(safe_format_log_message(x, y, dramatic=False, **kwargs)),
        "warning": lambda x, y=False, **kwargs: loguru.warning(safe_format_log_message(x, y, dramatic=False, **kwargs)),
        "error": lambda x, y=False, **kwargs: loguru.error(safe_format_log_message(x, y, dramatic=False, **kwargs)),
        "critical": lambda x, y=False, **kwargs: loguru.critical(safe_format_log_message(x, y, dramatic=False, **kwargs))
    }
}

# startup message

if DramaticLoggerConfig["startupMessage"] == "full":
    loguru.success("Starting up DramaticLogger...\n" + ("-" * 96) + "\n")
    loguru.success("This is an example success message")
    loguru.trace("This is an example trace message")
    loguru.debug("This is an example debug message")
    loguru.info("This is an example info message")
    loguru.warning("This is an example warning message")
    loguru.error("This is an example error message")
    loguru.critical("This is an example critical message")   
elif DramaticLoggerConfig["startupMessage"] == "brief":
    loguru.success("Starting up DramaticLogger...")