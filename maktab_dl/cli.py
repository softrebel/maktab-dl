import argparse
import os
from maktab_dl.handler import MaktabkhoonehCrawler
from maktab_dl.utils import (
    get_cookies_default_file_path,
    get_boolean_manual,
)

cookies_default_path = get_cookies_default_file_path()
output_default_path = os.getcwd()


def main():
    """
    A simple command-line interface for interacting with Maktabkhooneh.
    """
    parser = argparse.ArgumentParser(
        description="A simple command-line interface for interacting with Maktabkhooneh."
    )
    subparsers = parser.add_subparsers(
        title="Commands", dest="command", help="Available commands"
    )

    # Download Subcommand
    download_parser = subparsers.add_parser(
        "download", help="Loads course info and downloads videos"
    )

    download_parser.add_argument(
        "-u",
        "--url",
        required=True,
        type=str,
        help="Course URL in Maktabkhooneh",
    )
    download_parser.add_argument(
        "-c",
        "--cookies",
        required=False,
        type=str,
        default=cookies_default_path,
        help=f"Path to the cookies file [Default: {cookies_default_path}]",
    )
    download_parser.add_argument(
        "-o",
        "--output",
        required=False,
        type=str,
        default=output_default_path,
        help=f"Path to the output directory [Default: {output_default_path}]",
    )
    args = parser.parse_args()

    if args.command == "download":
        download_videos(args.url, args.cookies, args.output)


def download_videos(url: str, cookies: str, output: str):
    """Loads course information from a URL and downloads videos for that course."""
    try:
        if not os.path.exists(cookies):
            print(
                "Cookies file not found. You must Enter Maktabkhooneh Username and Password."
            )
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            crawler = MaktabkhoonehCrawler(
                username=username,
                password=password,
                cookies_path=cookies,
                output_path=output,
            )

            force_save_cookies = get_boolean_manual(
                f"If you want to save cookies on the path `{cookies}` you selected?"
            )
            crawler.login(force_save_cookies=force_save_cookies)
        else:
            crawler = MaktabkhoonehCrawler(
                cookies_path=cookies,
                output_path=output,
            )
            crawler.init_cookies()
            if len(crawler.client.cookies.jar) == 0:
                print("No Cookies. Please login first.")
                return

        course_info = crawler.crawl_course_link(input_link=url)
        cleaned_link = course_info.link
        crawler.enroll_course_link(cleaned_link)
        crawler.download_course_videos(course_info)
        print(f"Finished downloading course videos from: {cleaned_link}")
    except Exception as e:
        print(f"Error downloading videos: {e}")


if __name__ == "__main__":
    main()
