import sys
from loguru import logger as loguru

# Remove the default handler
loguru.remove()

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
            "sink": "DLog.log",
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
DramaticLoggerSecondLine = lambda x: (" " + (("─" * (92 - len(x)) + "─┤") if len(x) < 92 else ""))
DramaticLoggerBottomLine = ("\n╘" + ("═" * 96) + "╛\n")
DramaticLoggerContents = lambda x, y: DramaticLoggerTopLine + f"{x}" + DramaticLoggerSecondLine(x) + (f"\n{y}" if y else "") + DramaticLoggerBottomLine
DramaticLogger = {
    "Dramatic": {
        "success": lambda x, y=False: loguru.success(DramaticLoggerContents(x, y if y else "")),
        "trace": lambda x, y=False: loguru.trace(DramaticLoggerContents(x, y if y else "")),
        "debug": lambda x, y=False: loguru.debug(DramaticLoggerContents(x, y if y else "")),
        "info": lambda x, y=False: loguru.info(DramaticLoggerContents(x, y if y else "")),
        "warning": lambda x, y=False: loguru.warning(DramaticLoggerContents(x, y if y else "")),
        "error": lambda x, y=False: loguru.error(DramaticLoggerContents(x, y if y else "")),
        "critical": lambda x, y=False: loguru.critical(DramaticLoggerContents(x, y if y else ""))
    },
    "Normal": {
        "success": lambda x, y=False: loguru.success(f"{x} {y if y else ""}"),
        "trace": lambda x, y=False: loguru.trace(f"{x} {y if y else ""}"),
        "info": lambda x, y=False: loguru.info(f"{x} {y if y else ""}"),
        "debug": lambda x, y=False: loguru.debug(f"{x} {y if y else ""}"),
        "warning": lambda x, y=False: loguru.warning(f"{x} {y if y else ""}"),
        "error": lambda x, y=False: loguru.error(f"{x} {y if y else ""}"),
        "critical": lambda x, y=False: loguru.critical(f"{x} {y if y else ""}")
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