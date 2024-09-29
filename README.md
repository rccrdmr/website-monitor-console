
# Website Monitor Console

A console-based Python application that monitors the performance and availability of websites. Users can define websites and specify check intervals, and the application continuously tracks the uptime and response times for each website.

## Features

- Monitor the uptime and response time of multiple websites.
- Customizable check intervals for each website.
- Console-based interface.
- Colored output for success, warnings, and errors.
- URL validation to ensure valid website entries.

## Installation

### Using Poetry (Recommended)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/website-monitor-console.git
   cd website-monitor-console
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

### Using pip

If you prefer to use `pip`, you can also install the dependencies via a `requirements.txt` file:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/website-monitor-console.git
   cd website-monitor-console
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Enter the website URLs you want to monitor. Make sure the URLs start with `http://` or `https://`. You can enter multiple websites.

3. For each website, enter the check interval (in seconds) for how often the app should check that website.

4. Once you're done entering websites, type `done` to start the monitoring process.

5. The app will continuously monitor each website, providing colored output for:
   - **Green**: Website is UP with response time.
   - **Yellow**: Website is DOWN but returned an HTTP status code.
   - **Red**: Website is DOWN due to a network or connection error.

### Example

```bash
$ python main.py
Enter a website URL (or type 'done' to finish): https://example.com
Enter the check interval in seconds for https://example.com: 30
Enter a website URL (or type 'done' to finish): https://anotherwebsite.com
Enter the check interval in seconds for https://anotherwebsite.com: 60
Enter a website URL (or type 'done' to finish): done

Starting website monitoring... Press Ctrl+C to stop.

Website https://example.com is UP. Response time: 120 ms.
Website https://anotherwebsite.com is DOWN. Status Code: 404.
```

### Stopping the Application

To stop monitoring, press `Ctrl+C` in the terminal.

## Dependencies

- `requests` - For making HTTP requests.
- `colorama` - For colored output in the terminal.
- `validators` - For URL validation.
- `charset-normalizer`, `certifi`, `idna`, and `urllib3` - Dependency libraries used by `requests`.

These dependencies are automatically installed when using `poetry install` or `pip install -r requirements.txt`.

## Contributing

If you'd like to contribute, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
