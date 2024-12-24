# DramaticLogger

DramaticLogger is a powerful logging tool built on top of Loguru, designed to provide enhanced and visually appealing log messages for your Python applications.

## Features

- Custom log levels with unique icons and colors
- Multiple handlers for different logging outputs (stderr, file)
- Easy integration with existing projects

## Installation

You can install DramaticLogger directly from GitHub using `pip`:

```bash
pip install git+https://github.com/Lexa-B/DramaticLogger.git
```

## Usage

To use DramaticLogger in your project, simply import it and configure it as needed.

```python
from dramatic_logger import DramaticLogger

logger = DramaticLogger()
logger.info("Dramatic log message")
```
