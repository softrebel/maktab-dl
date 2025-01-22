
# maktab-dl

A command-line tool to download videos from Maktabkhooneh courses.

## Installation


1. **Install using pip**

   ```bash
   pip install maktab-dl
   ```

1. **Clone the Repository (Optional):**

   If you have access to the repository, you can clone it:

   ```bash
   > git clone https://github.com/softrebel/maktab-dl.git
   > cd maktab-dl
   > pip install .
   ```

## Usage

The `maktab-dl` tool provides a `download` subcommand for downloading course videos.

```bash
maktab-dl download [options]
```

### Command

- `download`: This subcommand is used to download course videos.

### Options

The `download` subcommand accepts the following options:

- `-u`, `--url` (Required): The URL of the Maktabkhooneh course page.
- `-c`, `--cookies` (Optional): The path to the cookies file. Defaults to a `cookies.json` file in a suitable user data directory as specified by `appdirs` package.
- `-o`, `--output` (Optional): The path to the output directory where videos will be saved. Defaults to the current directory the script is called from.

## Examples

Here are some examples of how to use `maktab-dl`:

1.  **Basic Download with Default Options:**

    If you have saved cookies, it will automatically use it to download the course video. This will save the course in the current directory

    ```bash
    maktab-dl download -u <your_course_url>
    ```
    for example:
    ```bash
    maktab-dl download -u https://maktabkhooneh.org/course/آموزش-سی-شارپ-c-mk9558/
    ```


2.  **Download with custom cookies and output directories:**

    ```bash
    maktab-dl download -u <your_course_url> -c /path/to/my/cookies.json -o /path/to/my/output
    ```

3.  **First time login and save cookies:**

    If you run this command and cookies file does not exist in the defined path, it will ask username, password, and confirmation to save cookies.

    ```bash
    maktab-dl download -u <your_course_url> -c /path/to/my/cookies.json
    ```

4.  **When cookies is not valid:**

    If you run the script with invalid cookie file, it will ask you to login again

    ```bash
    maktab-dl download -u <your_course_url> -c /path/to/my/invalid_cookie.json
    ```

6.  **Using relative path for cookies**

    ```bash
    maktab-dl download -u <your_course_url> -c ./my_cookies.json -o ./videos
    ```
    This command will save the cookies in current directory and video in the videos subdirectory.

7.  **Help Message:**

    To see the available options and usage information, run:

    ```bash
    maktab-dl download --help
    ```
    or
    ```bash
     maktab-dl --help
    ```

## Explanation

### First time Login

-   If you run the script with a cookies file path that does not exist, it will prompt you for your Maktabkhooneh username and password.
-   After logging in successfully, it will ask you if you would like to save the cookies to the specified path.
-   Subsequent executions can reuse the saved cookie to make the script work seamlessly.
- If cookies are present but not valid it will ask you to relogin.

### Default Paths

-   **Cookies File:** If you don't provide the path to the cookies file, it will save `cookies.json` to suitable user data directory. The exact location will depend on your operating system (Linux, macOS, or Windows). The location is handled by `appdirs` package.
-   **Output Directory:** If you don't specify the output directory, it will save the video in the current directory the command was run from.

## Error Handling

-   The script includes basic error handling to catch exceptions that might happen during the downloading process. The error is printed to console with descriptive message.
-   You will be informed if cookies file can not be found or invalid.
-   If the course does not have any video, it will log the message into console.

## Dependencies

-   `requests`: Used for making HTTP requests.
-   `beautifulsoup4`: Used for parsing HTML content.
-  `appdirs`: Used for finding user specific os paths.

## Important Notes

-   This script requires a Maktabkhooneh account to download courses.
-   The script will create output directory automatically when you are saving videos there.

This documentation should provide a good starting point for users of your `maktab-dl` package. Let me know if you have any other questions!

