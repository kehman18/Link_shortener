````markdown
# Link Shortener

A simple web application that allows users to shorten their URLs, making them easier to share. The application takes a long URL and generates a shortened version of it.

## Features

- **URL Shortening:** Input a long URL to get a shortened version.
- **Custom URL:** Users can customize the short URL.
- **Responsive Design:** Works well on both desktop and mobile devices.

## Screenshots

![Home Page](./screenshots/homepage.png)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/link-shortener.git
   cd link-shortener
   ```
````

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root and add the following:

   ```
   API_KEY=your_api_key
   ```

5. **Run the application:**

   ```bash
   python server.py
   ```

   The application should now be running on `http://localhost:5000`.

## Usage

- Navigate to the homepage.
- Paste the URL you want to shorten into the input field.
- (Optional) Customize the shortened URL.
- Click "Send" to generate the shortened link.
- Copy and share the shortened link.

## Project Structure

- `server.py`: The main server file handling requests and generating shortened URLs.
- `templates/`: Contains the HTML templates (`index.html`, `shortened.html`).
- `static/`: Contains static assets like the favicon.
- `.env`: Environment variables (not included in the repository).

## Contributing

Contributions are welcome! If you have suggestions for improvements or find a bug, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- Inspired by [Bit.ly](https://bitly.com/)
- Favicon by [flaticon.com](https://www.flaticon.com/)
